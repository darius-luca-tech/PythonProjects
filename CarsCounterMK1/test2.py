import numpy as np 
import cv2
import pandas as pd 

cap = cv2.VideoCapture('video3.mp4') 
frames_count, fps, width, height = cap.get(cv2.CAP_PROP_FRAME_COUNT), cap.get(cv2.CAP_PROP_FPS), cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT) 

width = int(width) 
height = int(height) 
print(frames_count, fps, width, height) 

df = pd.DataFrame(index = range(int(frames_count))) 
df.index.name = "Frames" 

framenumber = 0  
carscrossedup = 0 
carscrosseddown = 0 
carids = [] 
caridscrossed = [] 
totalcars = 0 

fgbg = cv2.createBackgroundSubtractorMOG2() 
ret, frame = cap.read() 
ratio = .5 
image = cv2.resize(frame, (0, 0), None, ratio, ratio) 
width2, height2, channels = image.shape 
video = cv2.VideoWriter('traffic3_counter.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, (height2, width2), 1) 

while True:
	ret, frame = cap.read() 

	if ret: 
		image = cv2.resize(frame, (0, 0), None, ratio, ratio) 
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
		fgmask = fgbg.apply(gray) 

		kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)) 
		closing = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel) 
		
		
		opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel) 
		dilation = cv2.dilate(opening, kernel) 
		retvalbin, bins = cv2.threshold(dilation, 220, 255, cv2.THRESH_BINARY) 

		contours, hierarchy = cv2.findContours(bins, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
		hull = [cv2.convexHull(c) for c in contours] 
		cv2.drawContours(image, hull, -1, (0, 255, 0), 3) 

		lineypos = 255 
		cv2.line(image, (0, lineypos), (width, lineypos), (255, 0, 0), 5) 

		lineypos2 = 250 
		cv2.line(image, (0, lineypos2), (width, lineypos2), (0, 255, 0), 5) 

		minarea = 300 
		maxarea = 50000 

		cxx = np.zeros(len(contours)) 
		cyy = np.zeros(len(contours)) 

		for i in range(len(contours)): 
			if hierarchy[0, i, 3] == -1: 
				area = cv2.contourArea(contours[i]) 

				if minarea < area < maxarea: 
					cnt = contours[i] 
					M = cv2.moments(cnt) 
					cx = int(M['m10'] / M['m00']) 
					cy = int(M['m01'] / M['m00']) 

					if cy > lineypos:  
						x, y, w, h = cv2.boundingRect(cnt) 
						cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2) 
						cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10), cv2.FONT_HERSHEY_SIMPLEX, .3, (0, 0, 255), 1) 
						cv2.drawMarker(image, (cx, cy), (0, 0, 255), cv2.MARKER_STAR, markerSize = 5, thickness = 1, line_type = cv2.LINE_AA) 
						cxx[i] = cx 
						cyy[i] = cy 

		cxx = cxx[cxx != 0] 
		cyy = cyy[cyy != 0] 

		minx_index2 = [] 
		miny_index2 = [] 

		maxrad = 25 

		if len(cxx): 
			if not carids: 
				for i in range(len(cxx)): 
					carids.append(i) 
					df[str(carids[i])] = "" 
					df.at[int(framenumber), str(carids[i])] = [cxx[i], cyy[i]] 

					totalcars = carids[i] + 1 

			else: 
				dx = np.zeros((len(cxx), len(carids))) 
				dy = np.zeros((len(cyy), len(carids))) 

				for i in range (len(cxx)): 
					for j in range(len(carids)): 
						oldcxcy = df.iloc[int(framenumber - 1)][str(carids[j])] 
						curcxcy = np.array([cxx[i], cyy[i]]) 

						if not oldcxcy: 
							continue
						else: 
							dx[i, j] = oldcxcy[0] - curcxcy[0] 
							dy[i, j] = oldcxcy[1] - curcxcy[1] 

				for j in range(len(carids)): 
					sumsum = np.abs(dx[:, j]) + np.abs(dy[:, j]) 
					correctindextrue = np.argmin(np.abs(sumsum)) 
					minx_index = correctindextrue 
					miny_index = correctindextrue
 
					mindx = dx[minx_index, j] 
					mindy = dy[miny_index, j] 

					if mindx == 0 and mindy == 0 and np.all(dx[:, j] == 0) and np.all(dy[:, j] == 0):
						continue 
					else: 
						if np.abs(mindx) < maxrad and np.abs(mindy) < maxrad: 
							df.at[int(framenumber), str(carids[j])] = [cxx[minx_index], cyy[miny_index]] 
							minx_index2.append(minx_index) 
							miny_index2.append(miny_index) 

				for i in range(len(cxx)):
					if i not in minx_index2 and miny_index2: 
						df[str(totalcars)] = "" 
						totalcars = totalcars + 1 
						t = totalcars - 1 
						carids.append(t) 
						df.at[int(framenumber), str(t)] = [cxx[i], cyy[i]] 
					elif curcxcy[0] and not oldcxcy and not minx_index2 and not miny_index2: 
						df[str(totalcars)] = ""
						t = totalcars - 1 
						carids.append(t) 
						df.at[int(framenumber), str(t)] = [cxx[i], cyy[i]]			

		currentcars = 0
		currentcarsindex = [] 


		for i in range(len(carids)): 
			if df.at[int(framenumber), str(carids[i])] != '': 
				currentcars = currentcars + 1 
				currentcarsindex.append(i) 

		for i in range(currentcars): 
			curcent = df.iloc[int(framenumber)][str(carids[currentcarsindex[i]])] 
			oldcent = df.iloc[int(framenumber - 1)][str(carids[currentcarsindex[i]])] 

			if curcent: 
				cv2.putText(image, "Centroid" + str(curcent[0]) + "," + str(curcent[1]), 
					(int(curcent[0]), int(curcent[1])), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 255, 255), 2) 
				cv2.putText(image, "ID:" + str(carids[currentcarsindex[i]]), (int(curcent[0]), int(curcent[1] - 15)), 
					cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 255, 255), 2) 
				cv2.drawMarker(image, (int(curcent[0]), int(curcent[1])), (0, 0, 255), cv2.MARKER_STAR, markerSize = 5, 
					thickness = 1, line_type = cv2.LINE_AA) 

				if oldcent: 
					xstart = oldcent[0] - maxrad	 
					ystart = oldcent[1] - maxrad 
					xwidth = oldcent[0] + maxrad 
					yheight = oldcent[1] + maxrad  
					cv2.rectangle(image, (int(xstart), int(ystart)), (int(xwidth), int(yheight)),(0, 125, 0), 1) 

					if oldcent[1] >= lineypos2 and curcent[1] <= lineypos2 and carids[currentcarsindex[i]] not in caridscrossed:

						carscrossedup = carscrossedup + 1 
						cv2.line(image, (0, lineypos2), (width, lineypos2), (0, 0, 255), 5) 
						caridscrossed.append( 
							currentcarsindex[i]) 

					elif oldcent[1] <= lineypos2 and curcent[1] >= lineypos2 and carids[currentcarsindex[i]] not in caridscrossed: 
						carscrosseddown = carscrosseddown + 1 
						cv2.line(image, (0, lineypos2), (width, lineypos2), (0, 0, 125), 5) 
						caridscrossed.append(currentcarsindex[i]) 
 
		cv2.rectangle(image, (0, 0), (250, 100), (255, 0, 0), -1)
 
		cv2.putText(image, "Cars in Area: " + str(currentcars), (0, 15), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 170, 0), 1)
 
		cv2.putText(image, "Cars Crossed Up: " + str(carscrossedup), (0, 30), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 170, 0), 1)
 
		cv2.putText(image, "Cars Crossed Down: " + str(carscrosseddown), (0, 45), cv2.FONT_HERSHEY_SIMPLEX, .5,
                    (0, 170, 0), 1)
 
		cv2.putText(image, "Total Cars Detected: " + str(len(carids)), (0, 60), cv2.FONT_HERSHEY_SIMPLEX, .5,
                    (0, 170, 0), 1)
 
		cv2.putText(image, "Frame: " + str(framenumber) + ' of ' + str(frames_count), (0, 75), cv2.FONT_HERSHEY_SIMPLEX,
                    .5, (0, 170, 0), 1)
 
		cv2.putText(image, 'Time: ' + str(round(framenumber / fps, 2)) + ' sec of ' + str(round(frames_count / fps, 2))
                    + ' sec', (0, 90), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 170, 0), 1)
 
		cv2.imshow("countours", image)
		cv2.moveWindow("countours", 0, 0)
 
		cv2.imshow("fgmask", fgmask)
		cv2.moveWindow("fgmask", int(width * ratio), 0)
 
		cv2.imshow("closing", closing)
		cv2.moveWindow("closing", width, 0)
 
		cv2.imshow("opening", opening)
		cv2.moveWindow("opening", 0, int(height * ratio))
 
		cv2.imshow("dilation", dilation)
		cv2.moveWindow("dilation", int(width * ratio), int(height * ratio))
 
		cv2.imshow("binary", bins)
		cv2.moveWindow("binary", width, int(height * ratio))
 
		video.write(image)
 
		framenumber = framenumber + 1
 
		k = cv2.waitKey(int(1000 / fps)) & 0xff
		if k == 27:
			break
 
	else:
 
		break
 
cap.release()
cv2.destroyAllWindows()
 
df.to_csv('traffic2.csv', sep=',')