"""
    Date: Sat-28-Sept-2024

    Demonstrating Drawing Lines, Images, Circles, Text
"""

import cv2
import numpy as np

cap = cv2.VideoCapture()

def main():

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        width = int(cap.get(3))
        height = int(cap.get(4))

        #   Drawing Lines
        ##  Draws a line on image and returns an image with the line on the screen
        img = cv2.line(frame, (0, 0), (width, height), (207, 45, 180), 10)
        img = cv2.line(img, (0, height), (width, 0), (180, 27, 207), 10)

        ##  Draw Rectangle
        #   The -1 means fill everything; any other thing changes outline thickness
        img = cv2.rectangle(img, (100, 100), (200, 200), (45, 109, 96), -1)
        ##  Circle
        img = cv2.circle(img, (100, 300), 60, (0, 96, 96), -1)

        ##  Drawing Fonts
        font = cv2.FONT_HERSHEY_SIMPLEX
        #   The coordinate placing for fonts is bottom left corner of the Text Box
        #   the `cv2.LINE_AA` is antialiasing for Line Type, making text look better
        img = cv2.putText(img, "Deji is Amazing!", (100, int(height - 15)), font,
                          2, (0, 207, 220), 5, cv2.LINE_AA)


        
        
        cv2.imshow("Current Video Frame", frame)

        if cv2.waitKey(1) == ord("q"):
            break


    cap.release()
    cv2.destroyAllWindows()
    

if __name__ == "__main__":
    main()