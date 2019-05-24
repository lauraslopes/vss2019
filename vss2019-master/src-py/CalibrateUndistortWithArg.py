'''
 Based on the following tutorial:
   http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_calib3d/py_calibration/py_calibration.html
'''

import numpy as np
import cv2
import glob
import sys

# Aqui eu defino o tamanho do tabuleiro usadopara calibração.
# Determinado pelos pontos onde dois quadrados pretos se tocam
linhas = 19
colunas = 13

# Aqui defino o critério de parada pro algoritmo dos sub-pixels dos cantos.
criterio = (cv2.TERM_CRITERIA_MAX_ITER + cv2.TERM_CRITERIA_EPS, 30, 0.001)

# Aqui preparo os pontos que representarão osn cantos detectados pelo algoritmo de SHI-Tomasi
# e refinados a nível de sub-pixel. Chamados de object points, são coordenadas:
# (0,0,0), (1,0,0), (2,0,0), ..., (18,12,0). Se soubermos o tamanho de cada quadrado
# no mundo real, podemos mudar a unidade desses pontos para a distancia real entre eles.
# Eles são os mesmos pra todas as imagens
objectPoints = np.zeros((linhas * colunas, 3), np.float32)
objectPoints[:, :2] = np.mgrid[0:linhas, 0:colunas].T.reshape(-1, 2)

# Create the arrays to store the object points and the image points
objectPointsArray = []
imgPointsArray = []

images = glob.glob('/home/gabriel/Downloads/VSSS/vss2019-master/checkerboard_pattern/*.jpg')

# Loop over the image files
for path in images:
  print(path)
  # Load the image and convert it to gray scale
  img = cv2.imread(path)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  

  # Aqui chamo a função que encontra os cantos na imagem capturada.
  ret, corners = cv2.findChessboardCorners(gray, (linhas, colunas), None)

  # Make sure the chess board pattern was found in the image
  if ret:
    # Refine the corner position
    corners = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criterio)
      
    # Add the object points and the image points to the arrays
    objectPointsArray.append(objectPoints)
    imgPointsArray.append(corners)
 
    # Draw the corners on the image
    cv2.drawChessboardCorners(img, (linhas, colunas), corners, ret)
  
    # Display the image
    cv2.imshow('Tabuleiro', img)
    cv2.waitKey(500)

# Calibrate the camera and save the results
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objectPointsArray, imgPointsArray, gray.shape[::-1], None, None)
np.savez('../data/calib.npz', mtx=mtx, dist=dist, rvecs=rvecs, tvecs=tvecs)

# Print the camera calibration error
error = 0

for i in range(len(objectPointsArray)):
  imgPoints, _ = cv2.projectPoints(objectPointsArray[i], rvecs[i], tvecs[i], mtx, dist)
  error += cv2.norm(imgPointsArray[i], imgPoints, cv2.NORM_L2) / len(imgPoints)

print("Total error: ", error / len(objectPointsArray))

# Load one of the test images
img = cv2.imread(sys.argv[1])
h, w = img.shape[:2]

# Obtain the new camera matrix and undistort the image
newCameraMtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
undistortedImg = cv2.undistort(img, mtx, dist, None, newCameraMtx)

# Crop the undistorted image
# x, y, w, h = roi
# undistortedImg = undistortedImg[y:y + h, x:x + w]

# Display the final result
cv2.imshow('Tabuleiro', np.hstack((img, undistortedImg)))
cv2.waitKey(0)
cv2.destroyAllWindows()