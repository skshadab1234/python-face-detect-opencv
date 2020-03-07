import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
# face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
while(True):
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
	for (x,y,w,h) in faces:
		print(x,y,w,h)
		color =  (20, 148, 20)
		stroke =2
		width = x+w
		height = y+h
		cv2.rectangle(frame, (x,y),(width,height), color, stroke)
	cv2.imshow('Shadab Face Detecing',frame)
	if cv2.waitKey(20) & 0xFF == ord('s'):
		break

cap.release()
cv2.destroyAllWindows()
