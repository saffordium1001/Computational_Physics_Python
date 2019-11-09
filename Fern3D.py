# Fern in 3D, see Barnsley, "Fractals Everywhere"
 
from visual import *
from visual.graph import *
import random
imax = 20000                                             # points to draw
x = 0.5                                                 # initial x coord
y = 0.0                                                 # initial y coord
z = -0.2
xn = 0.0
yn = 0.0
graph1 = display(width=500, height=500, forward=(-3,0,-1),\
       title='3D Fractal Fern (rotate via right mouse button)', range=10)
graph1.show_rendertime = True
# Using points: cycle=27 ms, render=6 ms
# Using spheres: cycle=750 ms, render=30 ms
pts = points(color=color.green, size=0.01)
for i in range(1,imax):
    r = random.random();                                  # random number
    if ( r <= 0.1):                                     # 10% probability
        xn = 0.0
        yn = 0.18*y
        zn = 0.0
    elif ( r > 0.1 and r <= 0.7):                       # 60% probability
        xn =  0.85 * x
        yn =  0.85 * y + 0.1 * z + 1.6
        zn = -0.1  * y + 0.85 * z
            # print xn,yn,zn
    elif ( r > 0.7 and r <= 0.85):                     # 15 % probability
        xn =  0.2 * x - 0.2 * y 
        yn =  0.2 * x + 0.2 * y + 0.8
        zn=   0.3 * z
    else:
         xn = -0.2 * x +0.2 * y                         # 15% probability
         yn =  0.2 * x +0.2 * y + 0.8
         zn =  0.3 * z
    x = xn
    y = yn
    z = zn
    xc = 4.0*x                                       # linear TF for plot
    yc = 2.0*y-7  
    zc = z
    pts.append(pos=(xc,yc,zc))
