
# DecaySound.py spontaneous decay simulation

from visual import *	 
from visual.graph import *
import random
	 
import winsound
lambda1 = 0.001                                                       # Decay constant
max = 300.;  time_max = 500;   seed = 68111                                   # Params
number = nloop = max                                                  # Initial value
# random.seed(seed)                                           # Seed number generator

graph1 = gdisplay(width=1000, height=1000, title ='Spontaneous Decay',xtitle='Time',
                  ytitle = 'Number left',xmax=500,xmin=0,ymax=300,ymin=0)
decayfunc = gcurve(color = color.green)

for time in arange(0, time_max + 1):
    
    # Time loop
    for atom in arange(1, number + 1 ):
        
        # Decay loop
        decay = random.random()   
        if (decay  <  lambda1):
            nloop = nloop  -  1    # A decay
            winsound.Beep(600, 100)
    number = nloop
    decayfunc.plot( pos = (time, number) )
    rate(30)
