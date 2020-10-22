from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self,event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "\\" + filename
            new_dest = folder_destination + "\\" + filename
            os.rename(src,new_dest)
folder_to_track = "/Users/manny/Desktop/cm1"
folder_destination = "/Users/manny/Desktop/Blooger_Website"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler,folder_to_track,recursive=True)
observer.start()
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
    
