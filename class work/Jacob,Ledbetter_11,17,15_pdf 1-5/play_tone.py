#Generating sounds in Pygame using numpy
#Gavriel Feuer
#8/25/13
#--------------------------------------------------
##-Before Running this program make sure numpy is installed
#(https://pypi.python.org/pypi/numpy)
##-additional information on generating sounds is available here
#(http://web.media.mit.edu/~nvawter/otherProduct/keyboard5.py)
#--------------------------------------------------
import numpy
import pygame
Fs=44100
pygame.mixer.init(Fs,-16,1)
pygame.init()
pygame.display.set_mode((800,600))
time=5
length=Fs*time
##freq=600.0
#freq1=800.0
##freq2=600.0
#freq3=460.0
freq1=220.0*(4.0/3.0)
#freq2=17.5
amplitude=500.0
tmp=[]
for t in range(int(length)):
    v1=amplitude*numpy.sin(t*freq1/Fs*2*numpy.pi)
## v2=amplitude*numpy.sin(t*freq2/Fs*2*numpy.pi)
## v2=amp*numpy.sin(t*freq3/Fs*2*numpy.pi)
# v1=1+0.2*numpy.sin(t*freq1/Fs*2*numpy.pi)
# v2=amplitude*numpy.sin(t*freq2/Fs*2*numpy.pi*v1)
# v=v1*v2
    v=v1
    tmp.append(v1)
    sound=pygame.sndarray.make_sound(numpy.array(tmp,numpy.int16))
rungame=True
while rungame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rungame=False
    sound.play()
pygame.quit()
