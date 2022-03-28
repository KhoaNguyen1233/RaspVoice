import numpy as np
import pyaudio
import wave
import sys
from scipy.io.wavfile import write
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# x = []
# y = []

# figure, ax = plt.subplots(figsize=(4,3))
# line, = ax.plot(x, y)
# plt.axis([0, 4*np.pi, -1, 1])

# def func_animate(i):
#     x = np.linspace(0, 4*np.pi, 1000)
#     y = np.sin(2 * (x - 0.1 * i))
    
#     line.set_data(x, y)
    
#     return line,

# ani = FuncAnimation(figure,
#                     func_animate,
#                     frames=10,
#                     interval=50)

# ani.save(r'animation.gif', fps=10)

# plt.show()

def main():
    RATE    = 16000
    CHUNK   = 256

    p = pyaudio.PyAudio()

    player = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, output=True, frames_per_buffer=CHUNK)
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK)

    print("start recording")
    for i in range(int(2*RATE/CHUNK)): #do this for 10 seconds
        player.write(np.fromstring(stream.read(CHUNK),dtype=np.int16))
        # print(player.read(CHUNK))
        
    stream.stop_stream()
    # write('test.wav',RATE,player)
    stream.close()
    p.terminate()

if __name__ == '__main__':
    main()
