"""
    Date: Sat-28-Sept-2024

    Introduction to openCV for Python
"""

import cv2


#   By Default, cv2 loads image as BGR format, not RGB
"""
    Here are some modes that affect how cv2 interprets the image it reads:

    cv2.IMREAD_COLOR or -1: Loads a color image. Any transparency of image will be neglected. it is the default flag.
    cv2.IMREAD_GRAYSCALE or 0: Loads image in grayscale form
    cv2.IMREAD_UNCHANGED or 1: Loads image as it is , including th ealpha channel
"""

def EG1_ResizeImage(img):
    #   Resize to chosen dimensions
    return cv2.resize(img, (400, 600))

def EG1B_ResizeImage(img):
    #   Resize but in a more uniformly scalable way
    #   by using functions to modify the width and height
    #   This method can maintain the aspect ratio of the image.
    #   This halves the image's dimensions by 2
    return cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)

def EG1C_RotateImage(img):
    # return cv2.rotate(img, cv2.ROTATE_180)
    # return cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    return cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

def EG2_SaveImage(name, path, img):
    cv2.imwrite(path + "/" + name, img)

def main():
    img = cv2.imread("resources/images/2003873.jpg", 1)
    #   Resize the image
    img = EG1B_ResizeImage(img)
    img = EG1C_RotateImage(img)

    EG2_SaveImage("ep1-trex_90_clockwise.jpg", "_output", img)
    #   The `imshow` creates a window to display the image
    cv2.imshow("Image", img)
    #   This pauses execution at this point waiting infinitely (when the argument is 0)
    #   If any number greater than 0 is entered, it waits for that many seconds
    #   Once a key is clicked or time passes
    cv2.waitKey(0)
    #   It destroys all
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()