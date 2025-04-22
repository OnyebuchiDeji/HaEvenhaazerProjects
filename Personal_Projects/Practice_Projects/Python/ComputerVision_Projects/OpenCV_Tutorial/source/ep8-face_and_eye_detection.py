"""
    Date: Sat-29-Sept-2024

    This episode shows how to perform a live face and eye detection and tracking in
    openCV

    this face detextion is done with the Haar Cascade
    It's a pre-trained classifier that looks at an image and tries to detect
    certain features in that image.
    Features such as:
        1.  Distance between two centroids
        2.  Various colors present in the region
        3.  Edges and shapes present.
    They've been trained on hundreds of thousands of images, so it knows
    which features indicate a face or eye, etc.

"""

import cv2
import numpy as np



def main():
    cap = cv2.VideoCapture(0)
    #3  Load the haar cascades
    #   cv2.data.haarcascades is the path
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    

    while True:
        ret, frame = cap.read()
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #   This results all the locations of all faces' positions
        """
            This Stack Overflow answe shows the arguments to be
            passed in here.
            Args:
                1. scaleFactor: how much the image size is refuced at each image scale.
                    the smaller this value, the more accurate is the detection, 
                    but the slower the rate of detection.
                    If larger, the less accurate, but a faster detection rate.
                    So choose one that is suitable: not too slow, and accurate.
                    Start from 1.05 -- reduces image by 5%
                2.  minNeighbors: the minimum number of neighbors each candidate rectangle should
                    have to retain that rectangle choice.
                    It is part of the determination algorithm. Potential rectangle ocations for faces
                    are gotten. They should have about minNeighbors number of neighbors next to it.
                3.  minSize: The minimum possible object rectangle size. Objects smaller than this size are ignored.
                4.  maxSize: maximum possible object rectangle size. Objects larger than this are ignored.
                the last two are optional 

        """
        #   returns an array of rectangles
        faces = face_cascade.detectMultiScale(
            gray_image, 1.3, 5
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x,y), (x + w, y + h), (255, 255, 0), 5)
            """Grabbing Face Image Data to Get Eyes Data"""
            #   Now grab the area around the face to get where the eyes are
            #   roi == region of interest
            roi_gray = gray_image[y: y + h, x: x + w]
            roi_color = frame[y: y + h, x: x + w]

            """Getting The Eyes"""
            #   Look in the gray_scale image for 'eyes'
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255))

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()