import cv2 
print(cv2.__version__) 

cascade_src = 'cars.xml' 
video_src = 'video1.mp4' 
cars_counter = 0
cap = cv2.VideoCapture(video_src) 
car_cascade = cv2.CascadeClassifier(cascade_src) 

while True: 
	ret, img = cap.read() 
	if(type(img) == type(None)): 
		break 

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
	cars = car_cascade.detectMultiScale(gray, 1.1) 

	for (x, y, w, h) in cars: 
		cv2.rectangle(img, (x, y), (x+w, y+w), (0, 0, 255), 2) 
		cars_counter = cars_counter + 1 
	cv2.imshow('video', img) 
	print('cars_counter', cars_counter) 

	if cv2.waitKey(33) == 27: 
		break 

cv2.destroyAllWindows()