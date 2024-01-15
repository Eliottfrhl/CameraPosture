# Description du projet

L'objectif de cette partie du Projet S7 du Pôle Robotique est de connaître la position et l'orientation de la caméra dans un plan sur lequel des ArucoMarkers auront été préalablement placés.

# Utilisation

- Télécharger les dependencies du requirements.txt (avec environnement virtuel ou pas) `pip install -r requirements.txt`
- Créer des dossiers CalibrationPics/Initial et CalibrationPics/Final
- Imprimer des aruco markers, simples, en grid ou autre (GenerateArucoMarkers.py)
- Récupérer les images nécessaires à la calibration (getCalibrationPics.py)
- Réaliser la calibration (Calibrate.py)
- Représenter la posture de la caméra (CameraPosture*.py)

# Problèmes à résoudre

La librairie OpenCV a changé récemment et une partie du code est obsolète, notamment sur les classes de GridBoard, etc.

# Fichiers et rôles
## Calibrate.py

Ce script Python utilise OpenCV pour calibrer une caméra à l'aide d'images d'un échiquier prises avec la même caméra. Le script détecte les coins de l'échiquier, améliore leur précision et effectue la calibration de la caméra, produisant des paramètres essentiels tels que la matrice de la caméra et les coefficients de distorsion. Les résultats de la calibration sont sauvegardés pour une utilisation ultérieure dans des tâches de vision par ordinateur, en faisant un outil concis et efficace pour assurer un traitement d'image précis.

## CameraPostureByGrid.py

Ce script Python, utilisant OpenCV, diffuse une vidéo, détecte les marqueurs Aruco et estime la posture de la caméra par rapport à un plan défini par les marqueurs. La calibration de la caméra est nécessaire. Le script vérifie et charge les données de calibration, puis affiche en temps réel la posture estimée de la caméra basée sur les marqueurs Aruco. Pour arrêter la diffusion vidéo, appuyez sur 'q'.

## CameraPostureByMarker.py

Similaire au précédent mais en utilisant de simples markers à la place de grid.

## getCalibrationPics.py

Ce script Python utilise OpenCV pour capturer une vidéo en temps réel à partir d'une caméra (index 2) et enregistre les images de l'échiquier détecté pour la calibration. Les images initiales sont capturées pendant 20 secondes, avec une extraction des images finales toutes les 50 images, et sont sauvegardées respectivement dans "CalibrationPics/Initial" et "CalibrationPics/Final". Pour arrêter la capture, appuyez sur 'q'.

## GenerateArucoMarkers.py

Génère des aruco markers

## requirements.txt

Contient la liste des dependencies à installer.

## test.py

Fourre-tout de test







