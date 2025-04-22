"""
    The opencv for python utilizes deep learning for the face detection and
    distance estimation.

    But the algorithms are done on the CPU rather than the GPU

    The whole point of MiDaS model is that it can compute an estimate
    of relative inverse depth from an image.


    I tried to run it, but there is an issue with either the `path_model`
    or the `model_name`
    I checked online but didn't find the solution.
    Will most likely revisit this again -- most likely.

    This is the error it gave:
    cv2.error: OpenCV(4.10.0) D:\a\opencv-python\opencv-python\opencv\modules\dnn\src\onnx\onnx_importer.cpp:277: error: (-5:Bad argument)
    Can't read ONNX file: models\model-small.onnx in function 'cv::dnn::dnn4_v20240521::ONNXImporter::ONNXImporter'
"""

import cv2
import mediapipe as mp
import time
import os
mp_facedetector = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils

path_model = "models"

#   Read Network
# model_name = "model-f6b98070.onnx";    #   MiDaS v2.1 Large
model_name = "model-small.onnx"        #   MiDaS v2.1 Small

#   Load the DNN Model
model = cv2.dnn.readNet(os.path.join(path_model, model_name))

if (model.empty()):
    print("Could not load the neural net! - Checkpath")


#   Set backend and target to CUDA to use GPU
model.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
model.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)


def depth_to_distance(depth):
    return -1.7 * depth + 2


cap = cv2.VideoCapture(0)

with mp_facedetector.FaceDetection(min_detection_confidence=0.7) as face_detection:
    while cap.isOpened():
        success, img = cap.read()
        imgHeight, imgWidth, channels = img.shape
        #   timer to get frame rate
        start = time.time()

        # ------------------------------------------------------------------

        #   Convert the BGR image to RGB because the neural network
        #   works with it in RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # ------------Process the image and find faces with mediapipe ----------
        results = face_detection.process(img)

        if results.detections:
            #   Goes through each detected face
            for id, detection in enumerate(results.detections):
                mp_draw.draw_detection(img, detection)
                #print(id, detection)

                #   Get bounding box around the face
                #   the bounding box of this will be normalized between 0 and 1
                bBox = detection.location_data.relative_bounding_box

                #   
                h, w, c = img.shape

                #   The multiplications are just scaling the bounding box pixel values
                boundBox = (int(bBox.xmin * w), int(bBox.ymin * h), int(bBox.width * w),
                            int(bBox.height * h))

                center_point = ((boundBox[0] + boundBox[2]) / 2,
                                (boundBox[1] + boundBox[3]) / 2)
                
                cv2.putText(img, f'{int(detection.score[0] * 100)}%',
                                    (boundBox[0], boundBox[1] - 20),
                                    cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (0, 196, 255), 3)

        # --------------------Depth Map from Neural Network ------------------------------
        #   Create Blob from Input Image

        #   MiDas v2.1 Large (Scale: 1/255, Size: 384 x 384, Mean Subtraction: (123.675, 116.28), 103.53)
        #blob = cv2.dnn.blobFromImage(img, 1/255., (384, 384), (123.675, 116.28, 103.53), True, False)

        #   MiDas c2.1 Small (Scale: 1/255, Size: 256 x 256, Mean Subtraction: (123.675, 116.28, 103.53))
        """
        (function) def blobFromImage(
            image: MatLike,
            scalefactor: float = ...,
            size: Size = ...,
            mean: Scalar = ...,
            swapRB: bool = ...,
            crop: bool = ...,
            ddepth: int = ...
        ) -> MatLike
        """
        blob = cv2.dnn.blobFromImage(img, 1/255., (256, 256), (123.675, 116.28, 104.53), True, False)

        #   Set input to the model
        model.setInput(blob)

        #   Make Forward Pass in Model
        depth_map = model.forward()

        depth_map = depth_map[0,:,:]
        depth_map = cv2.resize(depth_map, (imgWidth, imgHeight))

        #   Normalize the output to get values between 0 and 1
        depth_map = cv2.normalize(depth_map, None, 0, 1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

        #   Convert the image color back before displaying
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        # ------------------------------------------------------------------------------------------------------


        #   Depth to Face
        depth_face = depth_map[int(center_point[1]), int(center_point[0])]

        #   Actual distance to face in metres
        depth_face = depth_to_distance(depth_face)
        print("Depth to Face: ", depth_face)
        cv2.putText(img, "Depth in cm: " + str(round(depth_face, 2) * 100),
                    (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 2, (196, 0, 196), 3)

        #   Depth Converted to Distance


        # -----------------------------------------------------------------------------------------------------
        totalTime = time.time() - start

        fps = 1/totalTime
        #print("FPS: ", fps)

        #   Print out the frames per second
        cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2) 

        cv2.imshow("Face Detection", img)
        cv2.imshow("Depth Map", depth_map)

        #   This is for hitting 'q'
        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()