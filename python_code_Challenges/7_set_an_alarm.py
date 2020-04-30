import simpleaudio as sa
from time import sleep

def alarm(time,message = 'Alarm!', audio = '7_audio.wav'):
    sleep(int(time))
    obj = sa.WaveObject.from_wave_file(audio)
    play = obj.play()
    print(message)
    input()
    #obj.stop()

print('Enter time to set alarm:')
time = input()
print('Enter path to sound file:')
audio = input()
print('Enter message for alarm:')
message = input()
if audio:
    alarm(time,message,audio)
else:
    alarm(time, message)
