"""
    Date: Sat-28-Sept-2024

    This episode demonstrates getting camera and videocapture (making videos)
"""

import cv2
import numpy as np

def img_effect1_grid(frame: np.array, frame_width, frame_height):
    canvas_img = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    #   Top Left
    canvas_img[:frame_height//2, :frame_width//2] = smaller_frame
    #   Bottom Left
    canvas_img[frame_height//2:, :frame_width//2] = smaller_frame
    #   Top Right
    canvas_img[:frame_height//2, frame_width//2:] = smaller_frame
    #   Bottom Right
    canvas_img[frame_height//2:, frame_width//2:] = smaller_frame

    return canvas_img

def img_effect2_grid_rotate(frame: np.array, frame_width, frame_height):
    """
        Couldn't do GREYSCALE because it has no RGB, hence its shape gave (240, 320)
        so I couldn't put it into the `canvas_img` that had shape of (240, 320, 3)
        ANd though I could resize it, which I'll do later
    """
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    greyscale = cv2.cvtColor(smaller_frame, cv2.COLOR_RGB2GRAY)

    canvas_img = np.zeros(frame.shape, np.uint8)
    #   Top Left
    canvas_img[:frame_height//2, :frame_width//2] = cv2.cvtColor(smaller_frame, cv2.COLOR_HSV2BGR)
    #   Bottom Left
    canvas_img[frame_height//2:, :frame_width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    #   Top Right
    canvas_img[:frame_height//2, frame_width//2:] = cv2.cvtColor(smaller_frame, cv2.COLOR_RGB2LAB)
    #   Bottom Right
    canvas_img[frame_height//2:, frame_width//2:] = cv2.cvtColor(smaller_frame, cv2.COLOR_RGB2BGR)
    #   Bottom Left

    return canvas_img




def main():
    ##  Adding the 0 brings up the camera
    ##  Else, adding a video file name will load that video
    cap = cv2.VideoCapture(0)
    
    #   Loop to get frame from video capture devide
    while True:
        """
           frame is the current frame/pixel data of the video (live or recorded)
           ret tells if the capture works properly.
           For example, if another app is using one's video camera, this app cannot.
           Hence the `cap.read()`'s first return value will be False.

        """
        ret, frame = cap.read()
        width = int(cap.get(3))
        height = int(cap.get(4))

        """
            The Special Effect
        """

        #   Create a blank image array 
        #   Make its shape same as the shape of the frame
        # canvas_img = img_effect1_grid(frame, width, height)

        canvas_img = img_effect2_grid_rotate(frame, width, height)


        cv2.imshow("Current Video Frame", canvas_img)

        #   The .waitKey waits 1 millisecond
        #   After 1 millisecond, it goes to next iteration
        #   But if a key is pressed, .waitKey() returns the ASCII value
        #   of that key, also called the Ordinal value.
        #   if that key is same as 'q', according to that logic, the loop is
        #   broken out of
        if cv2.waitKey(1) == ord('q'):
            break
    
    #   Once loop is broken off, release the camera resource
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()