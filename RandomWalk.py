# Walk.py  Random walk with graph
from visual import * 
from visual.graph import *
import random

random.seed(None)                  # Seed generator, None => system clock
jmax = 20
x    = 0.;          y = 0.                              # Start at origin

graph1 = gdisplay(width=500, height=500, title='Random Walk', xtitle='x',
                  ytitle='y')
pts = gcurve(color = color.yellow)  

for i in range(0, jmax + 1):
    pts.plot(pos = (x, y) )                                 # Plot points
    x += (random.random() - 0.5)*2.                        # -1 =< x =< 1
    y += (random.random() - 0.5)*2.                        # -1 =< y =< 1
    pts.plot(pos = (x, y))
    rate(100)
