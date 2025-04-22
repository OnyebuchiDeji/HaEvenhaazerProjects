"""
    Date: Fri-04-Oct-2024

    
"""

import cv2
import imutils
import threading
import winsound


"""Alarm Parameters"""
g_alarm = False
g_alarm_mode = False
#   This stacks to keep how long a movement occurs.
#   When this is above a limit, it causes an alarm
g_alarm_counter = 0

"""
    Instead of just an alarm, you could do it, Eben, such that
    it sends an email.

    This function causes the beep to happen 5 times
"""
def beep_alarm():
    global g_alarm, g_alarm_mode
    for _ in range(5):
        if not g_alarm_mode:
            break
        print("ALARM!")
        #   arg1 -- frequency
        #   arg2 -- duration in milliseconds
        winsound.Beep(2500, 1000)

    g_alarm = False
    

def main():
    global g_alarm_counter, g_alarm, g_alarm_mode

    #   the cv2.CAP_DSHOW helps startup to be proper
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)   #   index represents your camera device

    #   Changing the frame width and height
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    """
        Logic:
            Get a frame and save it.
            Then in the frame of next iteration, compare this iteration's frame
            with the previous iteration's stored frame.
            The more the number of differences, the more likely the alarm will sound
        
        The GaussianBlur smoothens an image
    """

    """Initial Starting Frame"""
    _, start_frame = cap.read()
    #   This scales the `start_frame` to width of 500
    start_frame = imutils.resize(start_frame, width=500)
    #   cvtColor means convert color
    #   Below converting the frame to grayscale
    start_frame = cv2.cvtColor(start_frame, cv2.COLOR_BGR2GRAY)
    #   The is applied. The tuple is the size
    
    start_frame = cv2.GaussianBlur(start_frame, (21, 21), 0)

    while True:
        _, frame = cap.read()
        frame = imutils.resize(frame, width=500)

        if g_alarm_mode:
            frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame_bw = cv2.GaussianBlur(frame_bw, (5, 5), 0)

            #   The difference between this frame and the initial frame (start_frame)
            difference = cv2.absdiff(frame_bw, start_frame)
            """
                Defines a Grayscale pixel threshold. Any grayscale pixel whose brightness
                is above the threshold is changed to white (255); but if below the threshold, it's
                changed to black (0).

                arg1: the frame map
                arg2: the threshold
                arg3: the max_val
                arg4: the type

                Anything above 25 is set to 255
                Anything below is set to 0
            """
            #   Returns a tuple
            #   so get the second element
            threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]

            #   In next iteration, the next frame's difference from this frame will be gotten
            start_frame = frame_bw

            """
                If the threshold map difference for that iteration
                is greater than 300, increase the alarm counter
                meaning the difference is significant

                Can tweak the thresh_val. It affects the sensitivity to motion
                Make it 100000 or more.

                tweaking this allows more large movement; the samller it is, the more sensitive it is
                to slight motion
            """
            thresh_val = 300
            if threshold.sum() > thresh_val:
                g_alarm_counter += 1
            #   If the difference is not more than 300, and consecutive iterations are
            #   the same, it means there's not much movement. Hence, decrease the alarm_counter
            else:
                if g_alarm_counter > 0:
                    g_alarm_counter -= 1
            
            cv2.imshow("Motion Cam", threshold)
        else:
            cv2.imshow("Motion Cam", frame)
        
        """
            Change the `alarm_feed_speed`; the higher it is, the more time it takes for the
            alarm to sound due to motion, as it depends on `g_alarm_counter` to accummulate to a certain sum
        """
        alarm_feed_speed = 50
        if g_alarm_counter > 20:
            if not g_alarm:
                g_alarm = True
                threading.Thread(target=beep_alarm).start()
        

        key_pressed = cv2.waitKey(30)
        if key_pressed == ord("t"):
            g_alarm_mode = not g_alarm_mode
            g_alarm_counter = 0
        if key_pressed == ord("q"):
            g_alarm_mode = False
            break
    
    cap.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()