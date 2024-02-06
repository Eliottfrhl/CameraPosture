import cv2
import pickle
import cv2.aruco as aruco
import numpy as np

with open('camera_params.pkl', 'rb') as f:
    camera_params = pickle.load(f)

cameraMatrix = camera_params[0]
distCoeffs = camera_params[1]
markerLength = 0.05

aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
parameters = aruco.DetectorParameters_create()

cap = cv2.VideoCapture(0)  

while True:
    ret, frame = cap.read()
    while(not ret):
        ret,frame=cap.read()

    corners, ids, rejected = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)

    if ids is not None:
        aruco.drawDetectedMarkers(frame, corners, ids)

        for i in range(len(ids)):
            rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners[i], markerLength, cameraMatrix, distCoeffs)

            print(f"Marker ID: {ids[i]}")
            print(f"Translation: {tvec}")
            print(f"Rotation: {rvec}")

            rotation_matrix = cv2.Rodrigues(rvec)[0]

            normal = rotation_matrix[:, 2] 

            a, b, c = normal
            d = -np.dot(normal, tvec)

            print(f"Équation du plan : {a}x + {b}y + {c}z + {d} = 0")

            homogeneous_transform = np.column_stack((rotation_matrix, tvec))
            homogeneous_transform = np.vstack([homogeneous_transform, [0, 0, 0, 1]])

        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
