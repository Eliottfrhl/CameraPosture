import cv2
import pickle
import cv2.aruco as aruco


markerLength = 0.05
# Load camera parameters from .pkl file
with open('camera_params.pkl', 'rb') as f:
    camera_params = pickle.load(f)

# Extract camera matrix and distCoeffs
cameraMatrix = camera_params[0]
distCoeffs = camera_params[1]

aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
parameters = aruco.DetectorParameters_create()

cap = cv2.VideoCapture(0)  

while True:
    ret, frame = cap.read()
    if not ret:
        break

    corners, ids, rejected = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)

    if ids is not None:
        aruco.drawDetectedMarkers(frame, corners, ids)

        for i in range(len(ids)):
            rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners[i], markerLength, cameraMatrix, distCoeffs)

            print(f"Marker ID: {ids[i]}")
            print(f"Translation: {tvec}")
            print(f"Rotation: {rvec}")

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
