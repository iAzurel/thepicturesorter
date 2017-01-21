#!/usr/bin/env python

from PIL import Image
import os, os.path
import cv2
import sys

# Detect faces, then returns number of faces.
def detect_face(image_path, face_cascade):


	img = cv2.imread(image_path)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# Change the values based on needs.
	faces = face_cascade.detectMultiScale(
	    gray,
	    scaleFactor=1.1,
	    minNeighbors=7,
	    minSize=(30, 30),
	    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

	return faces

# Moves pictures based on detection of faces.
def imagesChecker():

	imgs_path = '/home/murtaza/Documents/Project/Pictures/'
	nofacesdir = '/home/murtaza/Documents/Project/NoFaces/'
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	imgs = os.listdir(imgs_path)

	for i in range (0, len(imgs)):
		faces = detect_face(imgs_path + '/' + imgs[i], face_cascade)

		if len(faces) == 0:
			os.rename(os.path.abspath(imgs_path + imgs[i]), nofacesdir + imgs[i])

def main():
	imagesChecker()

if __name__ == "__main__":
    main()