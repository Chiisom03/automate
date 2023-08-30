import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class AutoReloader(FileSystemEventHandler):
    def on_any_event(self, event):
        print("File change detected. Reloading...")
        sys.exit(0)


def main():
    event_handler = AutoReloader()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
            print('im here')
            print("File change detected. Reloading...")
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


if __name__ == "__main__":
    main()
