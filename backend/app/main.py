from server.ScanFolder import ScanFolder
from os import environ as env
from dotenv import load_dotenv
from utils.transcriber import transcribe
from utils.summarizer import summarize
import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger("main")
load_dotenv()

logger.info("Raw File Path:" + env["WATCH_FILES_PATH"])


def compose2(f, g):
    return lambda x: f(g(x))


raw_file_server = ScanFolder(
    env["WATCH_FILES_PATH"], compose2(summarize, transcribe), ["*.g722"])
raw_file_server.start()
