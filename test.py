import os
import shutil

InitialFrames = sorted(os.listdir("CalibrationPics/Initial"))
for number in range(0,601,50):
    shutil.copy(f"CalibrationPics/Initial/frame{number}.jpg",f"CalibrationPics/Final/frame{number}.jpg")