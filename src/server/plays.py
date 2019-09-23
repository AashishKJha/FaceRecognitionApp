from pygame import mixer # Load the required library
import time

song=['woosh.mp3','sneez.mp3','air.mp3']
delay=['10','5','5']
i=0
while(i<3):
    
    mixer.init()
    mixer.music.load(song[i])
    mixer.music.play()
    time.sleep(float(delay[i]))
    i=i+1
