import os
import time
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from plyer import notification

DOWNLOADS_PATH = os.path.join(os.path.expanduser('~'), 'Downloads')
VIDEO_PATH = os.path.join(DOWNLOADS_PATH, 'videos')
AUDIO_PATH = os.path.join(DOWNLOADS_PATH, 'audios')
EXECUTABLE_PATH = os.path.join(DOWNLOADS_PATH, 'executables')
UNKNOWN_PATH = os.path.join(DOWNLOADS_PATH, 'unknown_downloads')

def move_file(src, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
    shutil.move(src, dest)

def classify_and_move_file(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension in ['.mp4', '.avi', '.mkv']:
        move_file(file_path, VIDEO_PATH)
    elif file_extension in ['.mp3', '.wav', '.flac']:
        move_file(file_path, AUDIO_PATH)
    elif file_extension in ['.exe', '.msi']:
        move_file(file_path, EXECUTABLE_PATH)
    else:
        move_file(file_path, UNKNOWN_PATH)

def show_notification(message):
    notification.notify(
        title='Download Complete',
        message=message,
        timeout=10
    )

class DownloadHandler(FileSystemEventHandler):
    def __init__(self):
        self.pool = ThreadPoolExecutor(max_workers=2)  # Adjust the number of workers as needed

    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            self.pool.submit(classify_and_move_file, file_path)
            show_notification(f'{os.path.basename(file_path)} moved to its respective folder.')

def monitor_downloads_folder():
    event_handler = DownloadHandler()
    observer = Observer()
    observer.schedule(event_handler, path=DOWNLOADS_PATH, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    monitor_downloads_folder()
