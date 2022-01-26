import wave
from pyaudio import PyAudio,paInt16
import time

framerate=8000
NUM_SAMPLES=2000
channels=1
sampwidth=2
TIME=20
def save_wave_file(filename,data):
    '''save the date to the wavfile'''
    wf=wave.open(filename,'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b"".join(data))
    wf.close()

def my_record(num):
    pa=PyAudio()
    stream=pa.open(format = paInt16,channels=1,
                   rate=framerate,input=True,
                   frames_per_buffer=NUM_SAMPLES)
    my_buf=[]
    count=0
    while count<TIME:#控制录音时间
        string_audio_data = stream.read(NUM_SAMPLES)
        my_buf.append(string_audio_data)
        count+=1
        print('.')
    save_wave_file('C:/Users/ASUS/Desktop/'+num+'.wav',my_buf)
    stream.close()

chunk=2014
def play(num):
    wf=wave.open(r'C:/Users/ASUS/Desktop/'+num+'.wav','rb')
    p=PyAudio()
    stream=p.open(format=p.get_format_from_width(wf.getsampwidth()),channels=
    wf.getnchannels(),rate=wf.getframerate(),output=True)
    while True:
        data=wf.readframes(chunk)
        if data==b'':break
        stream.write(data)
    stream.close()
    p.terminate()
if __name__ == '__main__':
    my_record("2")
    print("2.wav Over")
    time.sleep(5)
    my_record("3")
    print('3.wav Over!') 
    play("2")
    print("2.wav Over")
    play("3")
    print("3.wav Over")