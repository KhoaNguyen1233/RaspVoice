from ctypes import sizeof
from email.mime import audio
from audiofile.core.info import sampling_rate
from python_speech_features import mfcc, logfbank
import numpy as np
import audiofile
from matplotlib import pyplot as plt

class SpeechObject():
    def __init__(self) -> None:
        self.audio_data = None
        self.extracted_samples = ''
        self.sampling_rate = 16000
        self.cmd = ''
        self.value = ''
        
    def get_voice_data(self, audio_data):
        signal, sampling_rate = audiofile.read(audio_data)
        self.audio_data = signal
        self.sampling_rate = sampling_rate
        pass
    
    def detect_speech(self):
        lenOfWindow = 0.025
        nSamplePerWindow = round(self.sampling_rate * lenOfWindow)
        nSampleBlock = round(len(self.audio_data)/nSamplePerWindow)
        meanBlockValue = []
        output = []
        for block in range(nSampleBlock):
            start = block * nSamplePerWindow
            end = (block + 1)* nSamplePerWindow
            meanBlockValue.append(np.mean(abs(self.audio_data[start:end])))
            # print("Start vs End : {} vs {}".format(start,end))
        
        print(meanBlockValue)
        differentiate = round((np.max(meanBlockValue) + np.min(meanBlockValue))/2,2)    
        print(differentiate)
        desired_output = [data for data in range(len(meanBlockValue)) if meanBlockValue[data] >= (differentiate*0.7)]
        desired_output = range(np.min(desired_output), np.max(desired_output))
        print(desired_output)
        filter = np.divmod(np.arange(len(self.audio_data)),nSamplePerWindow)[0]
        for dataIdx in range(len(self.audio_data)):
            if filter[dataIdx] in desired_output:
                output.append(self.audio_data[dataIdx])
            else:
                output.append(0)
        # print("Number of samples per windows: ", meanBlockValue)
        # print("Max and Min: {} vs {}".format(np.max(meanBlockValue),np.min(meanBlockValue)))
        plt.subplot(2,1,1)
        plt.plot(output)
        plt.subplot(2,1,2)
        plt.plot(self.audio_data)
        plt.show()
        return output
    
    def extract_features(self):
        # signal – the audio signal from which to compute features. Should be an N*1 array
        # samplerate – the samplerate of the signal we are working with.
        # winlen – the length of the analysis window in seconds. Default is 0.025s (25 milliseconds)
        # winstep – the step between successive windows in seconds. Default is 0.01s (10 milliseconds)
        # numcep – the number of cepstrum to return, default 13
        # nfilt – the number of filters in the filterbank, default 26.
        # nfft – the FFT size. Default is 512.
        # lowfreq – lowest band edge of mel filters. In Hz, default is 0.
        # highfreq – highest band edge of mel filters. In Hz, default is samplerate/2
        # preemph – apply preemphasis filter with preemph as coefficient. 0 is no filter. Default is 0.97.
        # ceplifter – apply a lifter to final cepstral coefficients. 0 is no lifter. Default is 22.
        # appendEnergy – if this is true, the zeroth cepstral coefficient is replaced with the log of the total frame energy.
        # winfunc – the analysis window to apply to each frame. By default no window is applied. You can use numpy window functions here e.g. winfunc=numpy.hamming
        self.extract_features = mfcc(self.audio_data, self.sampling_rate)
        
        pass
    
    def learning_model(self):
        pass
    
    def split_output(self):
        pass

if __name__ == '__main__':
    # signal, sampling_rate = audiofile.read('Sample\Recording_7.wav')
    # mfcc_feat = mfcc(signal, sampling_rate)
    # fbank_feat = logfbank(signal, sampling_rate)
    s = SpeechObject()
    s.get_voice_data('Sample\Recording_6.wav')
    s.detect_speech()
    # print (len(mfcc_feat))
    # print ("MFCC: ", mfcc_feat)
    # print (len(fbank_feat))
    # print ("LOG BANK:", fbank_feat)
    # plt.plot(s.audio_data)
    # plt.show()