import cv2
import numpy as np


def GetCameraPosture(camera_matrix,dist_coeffs):
    # Create Aruco dictionary
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)

    # Create Aruco parameters
    aruco_params = cv2.aruco.DetectorParameters_create()

    # Marker length
    marker_length = 0.09

    # Create video capture object
    cap = cv2.VideoCapture(0)  # Change the parameter to the video file path if needed

    while True:
        # Read frame from video stream
        ret, frame = cap.read()

        if not ret:
            break

        # Detect Aruco markers
        corners, ids, rejected = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=aruco_params)

        if ids is not None:
            # Define the plane defined by all the markers
            # The origin is the first marker
            # The x-axis is the first to second marker vector
            # The y-axis is the first to third marker vector
            # The z-axis is the cross product between the x-axis and y-axis
            origin = corners[0][0][0]
            x_axis = corners[0][0][1] - corners[0][0][0]
            y_axis = corners[0][0][2] - corners[0][0][0]
            z_axis = np.cross(x_axis, y_axis)

            # Estimate camera pose
            rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(corners, marker_length, camera_matrix, dist_coeffs)

            # Print the position and orientation of the camera in the system defined by the x,y and z axes
            print('Position: ', tvecs[0][0])
            print('Orientation: ', rvecs[0][0])

            # Draw axis for each marker
            for i in range(len(ids)):
                cv2.aruco.drawAxis(frame, camera_matrix, dist_coeffs, rvecs[i], tvecs[i], marker_length)

        # Display frame
        cv2.imshow('Frame', frame)

        # Exit loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release video capture object and close windows
    cap.release()
    cv2.destroyAllWindows()
