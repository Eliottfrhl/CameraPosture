
import numpy
import cv2
import pickle
import glob
import os


objpoints = []
imgpoints = [] 


CHESSBOARD_CORNERS_ROWCOUNT = 9
CHESSBOARD_CORNERS_COLCOUNT = 6

objp = numpy.zeros((CHESSBOARD_CORNERS_ROWCOUNT*CHESSBOARD_CORNERS_COLCOUNT,3), numpy.float32)
objp[:,:2] = numpy.mgrid[0:CHESSBOARD_CORNERS_ROWCOUNT,0:CHESSBOARD_CORNERS_COLCOUNT].T.reshape(-1, 2)

images = glob.glob('CalibrationPics/Final/frame*.jpg')
imageSize = None 

for iname in images:
    img = cv2.imread(iname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    board, corners = cv2.findChessboardCorners(gray, (CHESSBOARD_CORNERS_ROWCOUNT,CHESSBOARD_CORNERS_COLCOUNT), None)

    if board == True:
        objpoints.append(objp)
        
        corners_acc = cv2.cornerSubPix(
                image=gray, 
                corners=corners, 
                winSize=(11, 11), 
                zeroZone=(-1, -1),
                criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001))
        imgpoints.append(corners_acc)

        if not imageSize:
            imageSize = gray.shape[::-1]
    
        img = cv2.drawChessboardCorners(img, (CHESSBOARD_CORNERS_ROWCOUNT, CHESSBOARD_CORNERS_COLCOUNT), corners_acc, board)
        cv2.imshow('Chessboard', img)
        cv2.waitKey(0)
    else:
        print("Not able to detect a chessboard in image: {}".format(iname))

cv2.destroyAllWindows()

if len(images) < 1:
    print("Calibration was unsuccessful. No images of chessboards were found. Add images of chessboards and use or alter the naming conventions used in this file.")
    exit()

if not imageSize:
    print("Calibration was unsuccessful. We couldn't detect chessboards in any of the images supplied. Try changing the patternSize passed into findChessboardCorners(), or try different pictures of chessboards.")
    exit()

calibration, cameraMatrix, distCoeffs, rvecs, tvecs = cv2.calibrateCamera(
        objectPoints=objpoints,
        imagePoints=imgpoints,
        imageSize=imageSize,
        cameraMatrix=None,
        distCoeffs=None)
    
print(cameraMatrix)
print(distCoeffs)

CalibsFiles = os.listdir("CalibrationParams")

if len(CalibsFiles) == 0:
    path = "CalibrationParams/CalibrationParams0.pckl"
else:
    path = "CalibrationParams/CalibrationParams" + str(len(CalibsFiles)) + ".pckl"
    
with open(path, 'wb') as f:
    pickle.dump((cameraMatrix, distCoeffs, rvecs, tvecs), f)
    
print('Calibration successful. Calibration file used: {}'.format(path))
