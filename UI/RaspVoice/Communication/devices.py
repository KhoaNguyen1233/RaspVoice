from random import sample
import sounddevice as sd
from scipy.io.wavfile import write, read
from scipy import signal
from matplotlib import pyplot as plt
import numpy as np

fs = 16000  # Sample rate
seconds = 5  # Duration of recording
lo,hi=400,3500

# myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
# sd.wait()  # Wait until recording is finished
# write('output.wav', fs, myrecording)  # Save as WAV file 
# fs, data = read('output.wav')
# plt.plot(data)
# plt.show()

duration = 2  # seconds
output_handler = []


def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata
    output_handler.append(indata)

with sd.Stream(channels=2, callback=callback, samplerate=fs, blocksize=200):
    sd.sleep(int(duration * 1000))

# print(output_handler)
print("Size of output: ", np.shape(output_handler))
plt.plot(output_handler[0])
plt.show()
    