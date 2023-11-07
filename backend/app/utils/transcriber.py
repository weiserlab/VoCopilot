import whisper
from decorators.timed import timed
import logging
logger = logging.getLogger("transcribe-logger")
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


@timed
def transcribe(file_path: str, model_size: str = "base.en"):
    logger.info("Transcribe started")
    model = whisper.load_model(model_size)

    result = model.transcribe(file_path, fp16=False)
    return result["text"]
