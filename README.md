# Description du projet

L'objectif de cette partie du Projet S7 du Pôle Robotique est de connaître la position et l'orientation d'ArUco Markers dans le repère de la caméra.

# Utilisation

- Créer des dossiers CalibrationPics/Initial, CalibrationPics/Final et CalibrationParams
- Récupérer les images nécessaires à la calibration (getCalibrationPics.py)
- Réaliser la calibration (Calibrate.py)
- Retourner la position du tableau dans le repère de la caméra (MarkersPose.py)

# Problèmes à résoudre

La librairie OpenCV a changé récemment et une partie du code est obsolète.

# Fichiers et rôles
## Calibrate.py

Ce script Python utilise OpenCV pour calibrer une caméra à l'aide d'images d'un échiquier prises avec la même caméra. Le script détecte les coins de l'échiquier, améliore leur précision et effectue la calibration de la caméra, produisant des paramètres essentiels tels que la matrice de la caméra et les coefficients de distorsion. Les résultats de la calibration sont sauvegardés pour une utilisation ultérieure dans des tâches de vision par ordinateur, en faisant un outil concis et efficace pour assurer un traitement d'image précis.

## MarkersPose.py

Ce script Python, utilisant OpenCV, diffuse une vidéo, détecte les marqueurs Aruco et estime la position du marqueur ArUco dans le repère de la caméra. La calibration de la caméra est nécessaire. Le script vérifie et charge les données de calibration, puis affiche en temps réel la posture estimée de la caméra basée sur les marqueurs Aruco. Pour arrêter la diffusion vidéo, appuyez sur 'q'.

## getCalibrationPics.py

Ce script Python utilise OpenCV pour capturer une vidéo en temps réel à partir d'une caméra (index 2) et enregistre les images de l'échiquier détecté pour la calibration. Les images initiales sont capturées pendant 20 secondes, avec une extraction des images finales toutes les 50 images, et sont sauvegardées respectivement dans "CalibrationPics/Initial" et "CalibrationPics/Final". Pour arrêter la capture, appuyez sur 'q'.








