"""
    Detecting Faces and Bodies utilizes the Haar Cascade.

    Doing the classification needs the grayscale form of the image
"""

import cv2
import time
import datetime



def main():
    #   The index depends on the number of video capture devices
    #   one has
    cap = cv2.VideoCapture(0)

    #   This is a CascadeClassifier, and it takes as an argument the classifier's directory
    #   The `cv2.data.haarcascades` is the base directory
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullybody.xml")

    detection = False
    detection_stopped_time = None
    timer_started = False
    SECONDS_TO_RECORD_AFTER_DETECTION = 5

    frame_size = int(cap.get(3)), int(cap.get(4))
    # format: it accepts four characters: 'm' 'p' '4' 'v'
    #   fourcc == four character code
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    #   20 is the frame rate
    #   The below is the output stream
    out = cv2.VideoWriter("surv_videos/surv_vid1.mp4", fourcc, 20, frame_size)

    while True:
        _, frame = cap.read()

        gray_form = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        """
           arg1: grayscale frame
           arg2: Scale factor -- should be between 1 and 1.5
           arg3: min number of neighbors  -- the algorithm uses lots of boxes to detect a face.
            This argument specifies the minimum number of boxes that should be around a feature for it
            to be considered to be the target feature -- in this case, 5 boxes should be around
            what the algorithm is calling a face for it to be a face.
            It should be something between 3 and 6
        """
        faces = face_cascade.detectMultiScale(gray_form, 1.05, 4)
        bodies = face_cascade.detectMultiScale(gray_form, 1.05, 5)

        #   Now use it to draw the boxes for the faces on *coloured* surface
        #   Remember that color is BGR.
        #   last arg is thickness
        # for x, y, width, height in faces:
        #     cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 255), 3)
        
        """
            The goal is to detect if a body or a face is in the camera
            to start recording.
            And to ensure that if the Face or Body stops being detected, the code should wait 5 seconds before
            actually stopping the recording.
            But if the the Face or Body is re-detected within this 5 seconds, keep recording.

            So it does not stop the recording unless it's been 5 seconds since someone entered the frame.
        """
        
        if len(faces) + len(bodies) > 0:
            #   First, this is False
            #   This checks if a body or face had previously been detected before this iteration
            if detection:
                timer_started = False
            #   This starts new recording once face has just newly been detected
            else:
                detection = True
                current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                out = cv2.VideoWriter(f"saved_data/{current_time}.mp4", fourcc, 20, frame_size)
                print("Started Recording")
        #   If no body or face was detected but there had been a detection before
        elif detection:
            #   the below condition checks if the "Stop Recording" countdown timer had started
            #   Basically, if the timer had not started in the previous iteration...
            #   it's because this iteration is where detection of a Face or Body had stopped.
            #   wait/delay some seconds before stopping recording, when no face is detected
            if timer_started:
                #   when the time elapsed is greater than 5 seconds (SECONDS_TO_READ_AFTER...)
                if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                    detection = False
                    timer_started = False
                    out.release()
                    print("Stop Recording!")
            #   So if it is this iteration where no Face or Body was being detected,
            #   the first time, then start the "Stop Recording" countdown timer
            else:
                timer_started = True
                detection_stopped_time = time.time()
            

        ##  Only write to the output stream when a Face or Body is detected.
        ##  write in each frame continually
        if detection:
            out.write(frame)

        cv2.imshow("Security Camera", frame)

        if cv2.waitKey(1) == ord('q'):
            break
    
    out.release()   #   Saves the video once stream is released
    cap.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()