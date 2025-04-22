"""
    Date: Sat-28-Sept-2024

    Demonstrates getting the color of an object in an image by algorithm

    Uses HSV color channel: Hue, Saturation, and Lighting/Brightness 
    The method needed to extract the color from image requires HSV

    Hue, Saturation and Value or
    Hue, Saturation and Brightness or
    Hue, Saturation and Intensity

    NOTE and DISCOVERY:
        The HSV look of an image looks like those things in the AI graphics
        stuff.
        HSV is able to use Hue, Saturation and Brightness to properly distinguish
        between objects and their properties.
        From the video with TWT, his clothing, face, and different body
        parts where clearly distinguishable by the color on them.

        WIth this, one can easily separate the different objects based on hues similarities
        and differences.
        The depth data might even come from this!
"""

import cv2
import numpy as np


def EG1_Manual_Color_Conversion():
    """
        This is an alternative to doing:
        cv2.cvtColor(frame,cv2.COLOR_bgr)
    """    
    BGR_color = np.array[[[255, 0, ]]]
    x = cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV)
    # x[0][0]

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        width = int(cap.get(3))
        height = int(cap.get(4))

        # hsv = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR_FULL)
        # hsv = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
        # hsv = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGBA)
        # hsv = cv2.cvtColor(hsv, cv2.COLOR_RGB2HSV)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV_FULL)
        #   The below are used to filter out pixels

        lower_blue = np.array([90, 50, 50])
        upper_blue = np.array([150, 255, 255])

        #   this creates a mask that filters only blue colors
        #   The mask only allows the pixels that are within the range
        #   to be displayed
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        #   Then, the mask and frame are compared, and any pixel in
        #   the frame that has color blue displayed.
        #   Now, those not within the range are made to be black
        result = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow("Color Detection Result", result)
        cv2.imshow("Mask", mask)
        cv2.imshow("HSV", hsv)

        ##  The argument of waitKey has to be greater than 0 to refresh
        ##  because waitKey pauses execution
        if cv2.waitKey(1) == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

    


if __name__ == "__main__":
    main()