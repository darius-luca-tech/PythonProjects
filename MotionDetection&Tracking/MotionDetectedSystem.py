import cv2 
from datetime import datetime 
import easygui
import sys

def diffImg(t0, t1, t2): 
	d1 = cv2.absdiff(t2, t1) 
	d2 = cv2.absdiff(t1, t0) 
	return cv2.bitwise_and (d1, d2)

def displayHelloScreen(title): 
	easygui.msgbox("Welcome To\n" + title + "\n\nDeveloped by MEEEEEE ak Luca",title,"Starting Program") 
	d = easygui.diropenbox("Choose directory to save images in",title,"k") 
	if d == None: 
		sys.exit() 
	return d 

TITLE = "Motion Detection System" 
DIR = displayHelloScreen(TITLE) 

threshold = 12000 
cam = cv2.VideoCapture(0) 
winName = TITLE + "Webcam Footage" 
cv2.namedWindow(winName) 

t_minus = cv2.cvtColor(cam.read() [1], cv2.COLOR_RGB2GRAY) 
t = cv2.cvtColor(cam.read() [1], cv2.COLOR_RGB2GRAY) 
t_plus = cv2.cvtColor(cam.read() [1], cv2.COLOR_RGB2GRAY) 

timeCheck = datetime.now().strftime('%Ss') 


while True: 
	cv2.imshow(winName, cam.read() [1]) 
	if cv2.countNonZero(diffImg(t_minus, t, t_plus)) > threshold and timeCheck != datetime.now().strftime('%Ss'):
		dimg = cam.read() [1] 
		cv2.imwrite(datetime.now().strftime(DIR +'\%Y%m%d_%Hh%Mm%Ss%f') + '.jpg', dimg)
	timeCheck = datetime.now().strftime('%Ss') 

	t_minus = t 
	t = t_plus 
	t_plus = cv2.cvtColor(cam.read() [1],cv2.COLOR_RGB2GRAY) 

	key = cv2.waitKey(10) 
	if key == 27: 
		cv2.destroyWindows(winName) 
		if easygui.boolbox("Are u sure that u wanna exit,mtfk?", TITLE): 
			if easygui.passwordBox("Enter password to exit", TITLE) == password:
				break 
			else: 
				continue