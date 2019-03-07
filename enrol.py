# voice.py

# speechrecognition, pyaudio, brew install portaudio
import sys
sys.path.append("./")

import pyaudio
import wave
import pyrebase

config = {
  "apiKey": "",
  "authDomain": "",
  "databaseURL": "",
  "storageBucket": ""
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

def uniqid():
    from time import time
    return hex(int(time()*10000000))[2:]

thisIsUserId = uniqid()
# name = raw_input("What is your name? ")
# type(name)
data = {"name": "name this"}
db.child("users").child(thisIsUserId).set(data)

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "audioRefrence/"+thisIsUserId+".wav"

audio = pyaudio.PyAudio()


# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
print "recording..."
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print "finished recording"


# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

