import sounddevice
import vosk
import sys
import sounddevice as sd
import queue
import time

model = vosk.Model("model")
sample_rate = 16000
device = 1  # id устройства записи, в этом случае микрофон

q = queue.Queue()


def callback(in_data, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(in_data))


with sd.RawInputStream(samplerate=sample_rate, blocksize=8000, device=device, dtype='int16',
                       channels=1, callback=callback):
    rec = vosk.KaldiRecognizer(model, sample_rate)
    while True:
        data = q.get()

        if rec.AcceptWaveform(data):
            print(rec.Result())

