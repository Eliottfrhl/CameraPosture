import cv2
import numpy as np
import os

def getImages(folder_path):
    image_files = os.listdir(folder_path)
    images = []

    for file in image_files:
        image_path = os.path.join(folder_path, file)
        image = cv2.imread(image_path)
        images.append(image)

    return images

def CalibrateCamera(images, chessboard_size=(9, 6)):
    # Create arrays to store object points and image points from all the images
    object_points = []  # 3D points in real world space
    image_points = []   # 2D points in image plane

    # Generate the object points
    object_points_grid = np.zeros((chessboard_size[0] * chessboard_size[1], 3), np.float32)
    object_points_grid[:, :2] = np.mgrid[0:chessboard_size[0], 0:chessboard_size[1]].T.reshape(-1, 2)

    # Iterate over the images
    for image in images:
        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Find the chessboard corners
        ret, corners = cv2.findChessboardCorners(gray, chessboard_size, None)

        # If corners are found, add object points and image points
        if ret:
            object_points.append(object_points_grid)
            image_points.append(corners)

    # Calibrate the camera
    ret, camera_matrix, distortion_coeffs, rvecs, tvecs = cv2.calibrateCamera(
        object_points, image_points, gray.shape[::-1], None, None
    )

    return ret, camera_matrix, distortion_coeffs ,rvecs, tvecs

# Define the chessboard size
chessboard_size = (9, 6)

# Load the images
images = getImages('CalibrationPics/Final')