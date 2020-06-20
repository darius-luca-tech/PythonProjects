from watchdog.observers import Observer 
import time 
from watchdog.events import FileSystemEventHandler 
import os 
import json 
import shutil 
from datetime import datetime 
from time import gmtime, strftime 

class MyHandler(FileSystemEventHandler) : 
	def on_modified (self, event):  
		for filename in os.listdir(folder_to_track): 
			i = 1
			if filename != 'Files': 
				new_name = filename 
				extension = 'noname' 
				try: 
					extension = str(os.path.splitext(folder_to_track + '/' + filename)[1]) 
					path = extensions_folders[extension] 
				except Exception: 
					extension = 'noname' 

				now = datetime.now() 
				year = now.strftime("%Y") 
				month = now.strftime("%m") 

				folder_destination_path = extensions_folders[extension] 

				year_exists = False 
				month_exists = False 

				for folder_name in os.listdir(extensions_folders[extension]): 
					if folder_name == year: 
						folder_destination_path = extensions_folders[extension] + "/" + year 
						year_exists = True 
						for folder_month in os.listdir(folder_destination_path): 
							if month == folder_month: 
								folder_destination_path = extensions_folders[extension] + "/" + year + "/" + 											month 
								month_exists = True 

				if not year_exists: 
					os.mkdir(extensions_folders[extension] + "/" + year) 
					folder_destination_path = extensions_folders[extension] + "/" + year 
				if not month_exists: 
					os.mkdir(folder_destination_path + "/" + month) 
					folder_destination_path = folder_destination_path + "/" + month  

				file_exists = os.path.isfile(folder_destination_path + "/" + new_name) 
				while file_exists: 
					i += 1 
					new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(i) + 							os.path.splitext(folder_to_track + '/' + filename)[1] 
					new_name = new_name.split("/")[4] 
					file_exists = os.path.isfile(folder_destination_path + "/" + new_name) 

				src = folder_to_track + "/" + filename 
				new_name = folder_destination_path + "/" + new_name  
				os.rename(src, new_name)
			#exception Exception: 
			#	print(filename)   
print("1")

extensions_folders = { 
	'noname' : "/home/gal1l30/Desktop/Files/Uncategorized_Files", 

	'.txt' : "/home/gal1l30/Desktop/Files/TextFiles",   

	'.h264': "/home/gal1l30/Desktop/Files/Videos",
	'.m4v': "/home/gal1l30/Desktop/Files/Videos",
	'.mkv': "/home/gal1l30/Desktop/Files/Videos",
	'.mov': "/home/gal1l30/Desktop/Files/Videos",
	'.mp4': "/home/gal1l30/Desktop/Files/Videos",
	'.mpg': "/home/gal1l30/Desktop/Files/Videos",
	'.mpeg': "/home/gal1l30/Desktop/Files/Videos", 

    '.gif' :"/home/gal1l30/Desktop/Files/Images" , 
    '.png' :"/home/gal1l30/Desktop/Files/Images", 
    '.jpeg' :"/home/gal1l30/Desktop/Files/Images",  
    '.jpg' : "/home/gal1l30/Desktop/Files/Images", 

    '.deb' : "/home/gal1l30/Desktop/Files/CompressedFiles", 
    '.rar' : "/home/gal1l30/Desktop/Files/CompressedFiles", 
    'tar.gz' : "/home/gal1l30/Desktop/Files/CompressedFiles", 
    '.zip' : "/home/gal1l30/Desktop/Files/CompressedFiles", 

    '.cpp' : "/home/gal1l30/Desktop/Files/C++Codes", 
    '.py' : "/home/gal1l30/Desktop/Files/PythonCodes", 
    '.sh' : "/home/gal1l30/Desktop/Files/Shell Codes", 

}  
print("2")

folder_to_track = "/home/gal1l30/Desktop"  
folder_destionation = "/home/gal1l30/Desktop/Files"
event_handler = MyHandler() 
observer = Observer() 
observer.schedule(event_handler, folder_to_track, recursive = True)  
print("3")
observer.start() 

try: 
	while True: 
		time.sleep(10) 
except KeyboardInterrupt: 
	observer.stop() 

observer.join() 

