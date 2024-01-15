# import the opencv library 
import cv2 
import time
import os
import shutil

filesInitial = os.listdir("CalibrationPics/Initial")
filesFinal = os.listdir("CalibrationPics/Final")

for frame in filesInitial:
    os.remove("CalibrationPics/Initial/"+frame)
for frame in filesFinal:
    os.remove("CalibrationPics/Final/"+frame)
    
# define a video capture object 
vid = cv2.VideoCapture(2) 

boolean = True
count = 0
ret,frame = vid.read()
while(not ret):
    ret,frame=vid.read()
print("Recording has started. Proceed to film your chessboard for 20 seconds.")
startTimer=time.time()
endTimer=time.time()
while(endTimer-startTimer<20):

	# Capture the video frame 
	# by frame 
    ret, frame = vid.read()

	# Display the resulting frame 
    cv2.imshow('frame', frame)
    if ret: 
        cv2.imwrite("CalibrationPics/Initial/frame%d.jpg" % count,frame)
        count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
    
    endTimer=time.time()
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 

InitialFrames = os.listdir("CalibrationPics/Initial")
for number in range(0,len(InitialFrames),50):
    shutil.copy(f"CalibrationPics/Initial/frame{number}.jpg",f"CalibrationPics/Final/frame{number}.jpg")