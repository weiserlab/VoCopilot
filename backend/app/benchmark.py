import time
from utils.transcriber import transcribe
from utils.summarizer import summarize
from os import path

ITERATIONS = 3
AUDIO_FILES = [
    # {"name": "first", "file": "./audio_files/english/30secs.wav"},
    # {"name": "2min_eng", "file": "./audio_files/english/2min.wav"},
    # {"name": "3min_eng", "file": "./audio_files/english/3min.wav"},
    # {"name": "22min_eng", "file": "./audio_files/english/22min.wav"},
    # {"name": "24secs_chi", "file": "./audio_files/chinese/24secs.wav"},
    # {"name": "3min_chi", "file": "./audio_files/chinese/3min.mp3"},
    {"name": "22min_chi", "file": "./audio_files/chinese/22min.mp3"}
]

print("Benchmark Test started...")

for test_case in AUDIO_FILES:
    name = test_case["name"]
    file = path.abspath(test_case["file"])
    print("Test Case: " + name)
    start = time.time()
    for _ in range(ITERATIONS):
        transcript = transcribe(file, model_size="base")
        analysis = summarize(transcript)

    stop = time.time()
    duration_per_loop = (stop-start) / ITERATIONS

    print(f"average time taken for {name}: {duration_per_loop:.2f}s")
