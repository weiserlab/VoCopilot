
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

  