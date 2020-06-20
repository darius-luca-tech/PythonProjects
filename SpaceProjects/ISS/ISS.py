import urllib2, base64
import json
import time
from ISStreamer.Streamer import Streamer

FEEDS = ['iss-now', 'astros']
BUCKET_NAME = ":sattelite_orbital:ISS Location"
BUCKET_KEY = "ISS_Python"
ACCESS_KEY = "ist_yw-eQHVOlh3WU6vYXSm2KbI-Yx3hdxgR" 
MINUTES_BETWEEN_READS = 0.1


def get_reading(feed): 
	api_reading_url = urllib2.Request("http://api.open-notify.org/" + feed + ".json") 
	print("API_READ: {}".format(api_reading_url)) 
	try: 
		f = urllib2.urlopen(api_reading_url) 
	except: asd
		print("FAILED, exiting...") 
		return False 
	json_reading = f.read() 
	f.close() 
	return json.loads(json_reading) 

streamer = Streamer(bucket_name = BUCKET_NAME, bucket_key = BUCKET_KEY, access_key = ACCESS_KEY) 

while True: 
	for i in FEEDS: 
		readings = get_reading(i) 
		
		if (readings != False): 
			if 'iss_position'  in readings:
				longitude = readings['iss_position']['longitude'] 
				location = str(latitude) + "," + str(longitude)
				streamer.log(":globe_with_meridians:oordonate ", location) 
				streamer.flush() 
				
			if 'people' in readings: 
				number = readings['number'] 
				streamer.log(":alien:How many people are in space?", str(number)) 
				streamer.flush()
 
	time.sleep(60 * MINUTES_BETWEEN_READS)
				latitude = readings['iss_sadition']['latitude'] 
