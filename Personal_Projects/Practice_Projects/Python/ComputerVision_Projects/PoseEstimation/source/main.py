"""
    Implement the curl counting logic.
    Ideally there's a certain agnle threshold that is passed to indicate a curl
"""

import cv2
import mediapipe as mp
import numpy as np


#   This provides all drawing utilities to visualise poses
mp_drawing = mp.solutions.drawing_utlis
print(type(mp_drawing))
#   This imports the pose estimation model
#   It gets the Pose Estimation Model in the solutions library
mp_pose = mp.solutions.pose
print(type(mp_pose))


def calculate_angle(a, b, c):
    """Used Some Trig to Calculate Angle"""
    a = np.array(a) #   First
    b = np.array(b) #   Mid
    c = np.array(c) #   End

    #   Calculate radians for joint
    """
        E.g. Angle between connections of left shoulder (LS) and left elbow (LE), and left elbow (LE) and left wrist (LW)
        arctan2(LW.y-LE.y, LW.x-LE.y) - arctan2(LS.y - LE.y, LS.x - LE.x)

    """
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    #   Then convert to angle
    angle = np.abs(radians*180.0 / np.pi)

    #   Max angle is 180 degrees
    if angle > 180.0:
        angle = 360 - angle

    return angle



def proj_main():
    #   Get feed from webcam
    cap = cv2.VideoCapture(0)

    #   Curl Counter Variables
    counter = 0
    stage = None


    ##  Setup Mediapipe Pose Estimation Model Instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():

            ret, frame = cap.read()

            #   Detect stuff and render
            #   The Pose model needs the image color format to be RGB, hence the following line
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            #   This line saves some memory once passed to the Pose estimation model
            image.flags.writeable = False

            #   This makes the detection using the pose model object
            #   the detection results are returned in an array
            results = pose.process(image)

            #   Set it back to true
            image.flags.writeable = True
            #   Recolor image back to BGR from RGB
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            #   Extract Landmarks/Joints
            try:
                #   This returns a list of landmarks.
                landmarks = results.pose_landmarks.landmark
                # print(landmarks)
                # shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                # elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                # wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                #   Left Hip, Shoulder, Elbow
                left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]

                #   Calculate angle
                # angle = calculate_angle(shoulder, elbow, wrist)
                #   Left Hip, Shoulder, Elbow
                angle = calculate_angle(left_hip, left_shoulder, left_elbow)

                #   Visualize Angle
                ##  The angle is made to appear by the elbow; by passing `elbow` into the np array, it gets the elbow's
                ##  coordinates, specifically the normalized coordinates, and then scale it to screen/feed size
                #   Then it converts the coordinates into an integer
                # cv2.putText(image, str(angle),
                #             tuple( np.multiply(elbow, [640, 480]).astype(int),
                #                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (56, 56, 255), cv2.LINE_AAA)
                #             )
                cv2.putText(image, str(angle),
                            tuple( np.multiply(left_shoulder, [640, 480]).astype(int)),
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (56, 56, 255), cv2.LINE_AA
                            )
                
                #   Curl Logic
                ##  Keep in mind that the angle becomes less when one makes a curl
                if angle > 160:
                    stage = "down"
                if angle < 30 and stage == "down":
                    stage = "up"
                    counter += 1
                    print(counter)

            except:
                #   Happens if the model detects no landmark
                #   so it just passes through
                pass
                            
            #   Render Curl Counter
            #   Setup status box
            cv2.rectangle(image, (0, 0), (255, 73), (245, 117, 16), -1)

            #   Add Data to box
            cv2.putText(image, "REPS:", (15, 12),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

            cv2.putText(image, str(counter), (10, 63),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (25, 25, 0), 2, cv2.LINE_AA)

            cv2.putText(image, "STAGE:", (65, 12),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

            cv2.putText(image, stage, (60, 63),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (25, 25, 0), 2, cv2.LINE_AA)
      
            #   Applied detection, adding image, joints data, connections data, and joint and connection
            #   lines' colors
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(245, 117, 96), thickness=2, circle_radius=2),
                                      mp_drawing.DrawingSpec(color=(245, 109, 230), thickness=2, circle_radius=2),
                                      )

            cv2.imshow("Mediapipe Feed", frame)


            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        
        

        cap.release()
        cv2.destroyAllWindows()




def main():
    proj_main()


if __name__ == "__main__":
    main()