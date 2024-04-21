import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
from pydub import AudioSegment
import cv

seconds = 2
fs = 44100
recordsMaxLength = 5
concatedRecords = AudioSegment.empty()
audioIndex = 0

records = []
try:
    while 1:
        record = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()
        if len(records) < recordsMaxLength:
            records.append(record)
        else:
            for i in range(0, recordsMaxLength-1):
                records[i] = records[i+1]
            records[recordsMaxLength-1] = record
        if len(records) > 1:
            concatedRecords = np.concatenate(records)
        audioIndex += 1
except KeyboardInterrupt:
    pass
write("records/records.wav", fs, concatedRecords)
