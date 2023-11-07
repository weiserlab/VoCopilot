#include "Arduino.h"
#include "NDP.h"

#include "AudioTools.h"
#include "AudioCodecs/CodecG722.h"
#include <Nicla_System.h>

#include <SPI.h>
#include <SD.h>
G722Encoder encoder;
const bool lowestPower = false;

// Recording Related
uint8_t data[32768];
String command;
bool is_recording = false;

// File Related
File myFile;
String FILE_PATH = "DATA/FILE0.TXT";
int fileNumber = 0;
const int chipSelect = 6;

class CustomPrint : public Print {
public:
  size_t write(uint8_t d) override {
    if (!is_recording) return 0;
    return myFile.write(d);
  }
};

CustomPrint intermediaryPrint; // Create an instance of the custom print class

void ledBlueOn(char* label) {
  nicla::leds.begin();
  nicla::leds.setColor(blue);
  delay(200);
  nicla::leds.setColor(off);
  if (!lowestPower) {
    Serial.println(label);
  }
  nicla::leds.end();
}

void ledGreenOn() {
  nicla::leds.begin();
  nicla::leds.setColor(green);
  delay(200);
  nicla::leds.setColor(off);
  nicla::leds.end();
}

void ledRedBlink() {
  while (1) {
    nicla::leds.begin();
    nicla::leds.setColor(red);
    delay(200);
    nicla::leds.setColor(off);
    delay(200);
    nicla::leds.end();
  }
}

void eventTriggered(char* label) {
  String w(label);

  Serial.println("\n\nword detected: " + w);

  if (strstr(label,"yes") != NULL && !is_recording) {
    Serial.println("\nrecording started...");
    startRecording();
  } else if (strstr(label,"stop") != NULL && is_recording) {
    Serial.println("\nrecording stopped...");
    stopRecording();
  }

}

File openFile() {
  myFile = SD.open(FILE_PATH, FILE_WRITE);
  return myFile;
}

void closeFile() {
  myFile.close();
}

void setup() {

  Serial.begin(115200);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  nicla::begin();
  nicla::leds.begin();

  // SD Card Initialization
  Serial.print("Initializing SD card...");

  if (!SD.begin(chipSelect)) {
    Serial.println("initialization failed!");
    while (1);
  }
  Serial.println("initialization done.");

  NDP.onError(ledRedBlink);
  NDP.onMatch(ledBlueOn);
  NDP.onEvent(ledGreenOn);
  NDP.onMatch(eventTriggered);

  AudioBaseInfo bi;
  bi.channels = 1;
  bi.sample_rate = 16000;

  encoder.setOptions(0);
  encoder.begin(bi);
  encoder.setOutputStream(intermediaryPrint);

  Serial.println("Loading synpackages");
  NDP.begin("mcu_fw_120_v91.synpkg");
  NDP.load("dsp_firmware_v91.synpkg");
  NDP.load("ei_model.synpkg");
  Serial.println("packages loaded");
  NDP.getInfo();

  Serial.println("Configure mic");
  NDP.turnOnMicrophone();
  int chunk_size = NDP.getAudioChunkSize();
  if (chunk_size >= sizeof(data)) {
    for(;;);
  }
  NDP.interrupts();
}

void updateFilePath(){
  fileNumber++;
  FILE_PATH = "DATA/FILE" + String(fileNumber) + ".TXT";
}

void startRecording() {
  if (!myFile) myFile = SD.open(FILE_PATH, FILE_WRITE);
  is_recording = true;
}

void stopRecording() {
  myFile.flush(); 
  is_recording = false;
  if (myFile) myFile.close();
  updateFilePath();
}

void loop() {
    NDP.noInterrupts();
    if (is_recording) {
      unsigned int len = 0;
      // myFile.flush();
      NDP.extractData(data, &len);
      encoder.write(data, len);
    } 
    NDP.interrupts();
}