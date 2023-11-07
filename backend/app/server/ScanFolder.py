import time
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer
from typing import Callable, List
import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger("scan-folder")


class ScanFolder:
    'Class defining a scan folder'

    def __init__(self, path: str, fn: Callable[[str], str], patterns: List[str] = ["*.wav", "*.g722"]):
        logger.info("Server Started")
        logger.info("Listening for File Events")

        self.fn = fn
        self.path = path
        self.documents = dict()
        self.event_handler = PatternMatchingEventHandler(patterns=patterns,
                                                         ignore_patterns=[],
                                                         ignore_directories=True)
        self.event_handler.on_any_event = self.on_any_event
        self.observer = Observer()

    def start(self):
        self.observer.schedule(self.event_handler, self.path, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        finally:
            self.observer.stop()
            self.observer.join()

    def stop(self):
        self.observer.stop()
        self.observer.join()

    def on_any_event(self, event):
        # logger.info(event.src_path, event.event_type)
        logger.info("Complete ScanFolder() access")
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            # Event is created, you can process it now
            logger.info(f"Watchdog created event - {event.src_path}.")
            self.fn(event.src_path)
        elif event.event_type == 'modified':
            # Event is modified, you can process it now
            logger.info(f"Watchdog modified event - {event.src_path}.")
        elif event.event_type == "deleted":
            # Event is deleted, you can process it now
            logger.info(f"Watchdog deleted event - {event.src_path}.")
