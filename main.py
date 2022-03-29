from ast import arg
import threading
from queue import Queue
from sys import platform
import os

# init module

def init_module():
    print ('Init module')
    
    if platform == "linux" or platform == "linux2":
        print("Linux")
    elif platform == "darwin":
        print("Darwin")
    elif platform == "win32":
        print("Window")
    else:
        print("Undefined")
    pass
    
def voice_receving(pattern_q):
    audio = ''
    print('voice_receving')
    return audio

def voice_pattern_extraction(pattern_q):
    pattern = []    
    print('feature_extraction')
    return pattern

def commands_analysis(pattern_q):
    val = ''
    cmd = ''
    print('command analysis')
    return (cmd, val)

def doAction(pattern_q):
    print('do action')
    if ():
        # do sth wtih val 
        pass
      
if __name__ == '__main__':
    init_module()
    q = Queue()
    stage1 = threading.Thread(target = voice_receving, args = (q,))
    stage2 = threading.Thread(target = voice_pattern_extraction, args = (q,))
    stage3 = threading.Thread(target = commands_analysis, args = (q,))
    stage4 = threading.Thread(target = doAction, args = (q,))
    
    stage1.start()
    stage2.start()
    stage3.start()
    stage4.start()
    