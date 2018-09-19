from watchdog.observers import Observer
from watchdog.events import *
import os

import time


class FileEventHandler(RegexMatchingEventHandler):

    def __init__(self):
        RegexMatchingEventHandler.__init__(self, regexes=[r'.*\.ui$'])
        self.last_time = 0

    def on_moved(self, event):
        pass

    def on_created(self, event):
        if event.is_directory is False:
            print("file created:{0}".format(event.src_path))

    def on_deleted(self, event):
        pass

    def on_modified(self, event):
        now_time = time.time() * 1000
        diff = now_time - self.last_time
        if event.is_directory is False and diff > 800:
            self.last_time = now_time
            file_name = os.path.split(event.src_path)[1]
            new_name = os.path.splitext(file_name)[0]
            os.system('python -m PyQt5.uic.pyuic %s -o %s' % (file_name, new_name + '.py'))
            print("file modified:{0}".format(event.src_path))


if __name__ == "__main__":
    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler, os.getcwd(), True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
