#Simple script to capture video using python.

import numpy as np
import cv2

def captureVideo():
	cap = cv2.VideoCapture(0)
	try:
		face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
		eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
	except e:
		print e	



	while(True):
		#Capture frame-by-frame
		ret, frame = cap.read()
		#frame = cv2.imread("../Data/angeline.jpg")
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		#Apply face detection algo here
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		for (x, y, w, h) in faces:
			cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
			roi_gray = gray[y:y+h, x:x+w]
			roi_color = frame[y:y+h, x:x+w]
			eyes = eye_cascade.detectMultiScale(roi_gray)
			for (ex, ey, ew, eh) in eyes:
				cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
		cv2.imshow('frame', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cap.release()
	cv2.destroyAllWindows()