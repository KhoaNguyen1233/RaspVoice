from multiprocessing import context
import sounddevice as sd
from scipy.io.wavfile import write
from scipy import signal
import numpy as np


class RecordingObj():
    def __init__(self) -> None:
        self.sampling_rate = 16000
        self.num_channels = 2
        self.context = []
        self.recording_data = None
        self.recording_files = '_out/recording.wav'
        self.timeout = 5

    def extract_words(self):
        pass

    def visualize_audio(self):
        pass

    def return_context(self):
        return self.context
        
    def recording_audio(self):
        myrecording = sd.rec(int(self.timeout * self.sampling_rate), dtype='float64', samplerate=self.sampling_rate, channels=1)
        sd.wait()  # Wait until recording is finished
        print(np.shape(myrecording))
        data = np.array(myrecording)
        b,a=signal.butter(N=6, Wn=[2*lo/fs, 2*hi/fs], btype='band')
        x = signal.filtfilt(b,a,data.transpose()[0])
        write('output.wav', fs, myrecording)  # Save as WAV file 
