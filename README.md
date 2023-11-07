
# VoCopilot

Using Large Language Models for the Voice Activated Tracking of Everyday Interactions

## Prior Publication

**Poster:**
*VoCopilot: Enabling Voice-Activated Tracking for Everyday Interactions*

**Authors:**

- Goh Sheen An
- Ambuj Varshney

**Publication Details:**

- **Conference:** MobiSys '23: Proceedings of the 21st Annual International Conference on Mobile Systems, Applications and Services
- **DOI:** [https://doi.org/10.1145/3581791.3597375](https://doi.org/10.1145/3581791.3597375)

## Getting Started

This repository contains the code for both the embedded device, as well as the backend, to run the end to end system for VoCopilot

### Embedded Device

1) To get started with the frontend, train and deploy a TinyML Model for Keyword Spotting (KWS) into the embedded device, using [Edge Impulse](https://edgeimpulse.com/).
   - For an example of an Edge Impulse Project that has been trained, refer to []
   - Remember to run the `.sh` script to deploy the TinyML model into Nicla Voice.

2) Ensure the following pre-requisites are met before running step 3.
   - Follow this [guide to install Arduino Libraries](https://roboticsbackend.com/install-arduino-library-from-github/) to install the following Libraries
     - [arduino-libg722](https://github.com/pschatzmann/arduino-libg722)
     - [arduino-audio-tools](https://github.com/pschatzmann/arduino-audio-tools/)
   - Connect an SD Card Module and SD Card to Nicla Voice, following this [documentation](https://arduinogetstarted.com/reference/library/arduino-sd-card-library).
3) After the firmware and model has been deployed into Nicla Voice, deploy the code in `./embedded_device/nicla_voice/record_to_sd.ino` using `Arduino IDE` into the Nicla Voice.

### Backend

1) `cd` to `backend` folder.
2) Create an `.env` file, with parameters similar to that of `.env.example`.
3) Start the pipenv shell with `pipenv shell` (Make sure you have pipenv installed)
4) Install the dependencies with `pipenv install`.
5) Ensure `ffmpeg` is installed. (e.g. with `brew install ffmpeg` on Mac OS). If there are errors with `whisper` or `ffmpeg`, try to run `brew reinstall tesseract`.
6) Install `llama 2` via [ollama](https://ollama.ai/).
7) Start the application via `python3 app/main.py`.
8) Drop a wav or g722 file into `WATCH_FILES_PATH` and let the server pick up the file, transcrie and summarize it.

### Benchmark

1) To run the benchmark, run the command `python3 app/benchmark.py`.
