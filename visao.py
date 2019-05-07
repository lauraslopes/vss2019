#!/usr/bin/python

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

#cap.set(3,640); cap.set(4,480);
#cap.set(3,1280);cap.set(4,720);
cap.set(3,1280);cap.set(4,960);

# USB 3.0: 1280x960 @45fps, 1280x720 @60fps, 640x480 @80fps, 320x240 @160fps
# USB 2.0: 1280x960 @22.5fps, 1280x720 @30fps, 640x480 @80fps, 320x240 @160fps

while(1):
    ret, frame = cap.read()
    if ret==True:
	frame = cv2.resize(frame, (640,480)) 

        # write the flipped frame
        #cv2.imwrite('frame.jpg',frame)
	#frame2 = cv2.medianBlur(frame,5)
        cv2.imshow('frame',frame)
	#cv2.imshow('frame2',frame2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
# out.release()
cv2.destroyAllWindows()
