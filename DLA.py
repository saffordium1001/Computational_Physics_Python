# Diffusion Limited aggregation
from visual import * 
from visual.graph import *
import random
Maxx = 500                                                 # canvas width
Maxy = 500                                                   # and height

graph1 = display(width=Maxx, height=Maxy, title='Diffusion Ltd Aggregation')
def gauss_ran():                 # Method generates 2 random numbers with
    old = 0                                       # gaussian distribution
    r1=0                                     # just to satisfy next while
    rr=0                               # first call uses gives one number
    if ( old == 0 ):                         # next call gives the second
        while ( rr>=1 or rr==0 ):                 # see Survey Comp. Phys
            r1 = 2. * random.random() - 1.
            r2 = 2. * random.random() - 1.
            rr = r1 * r1 + r2 * r2
        fac = sqrt(-2. * log(rr)/rr)
        mem = int(15000. * r1 * fac)
        old = 1
        return( int(15000. * r2 * fac) )
    else:
        old = 0
        return mem
    
rad = 45.0                                     # radius of yellow circle
step = 0
trav = 0                                   # to check if random walk ends
size = 80                                             # array size x size
max = 500                                # max number of ball generations
grid = zeros((size,size))                  # array for particle positions
                                            # grid=1 if position occupied
ring(pos=(0,0,0), axis=(0,0,1), radius=rad, thickness=0.8, color=color.yellow)
grid[40,40] = 1                                      # particle in center
sphere(pos=(0,0),radius=1.6,color=color.green)            # central point
ball = sphere(radius=1.6)                                   # moving ball

while True:           # generates new ball and its motion,"infinite loop"
    hit = 0                                # ball doesn't hit a fixed one
    angle = 2. *pi * random.random()                   # -2pi <angle <2pi
    x = 40+int(rad * cos(angle))           # start x position of new ball
    y = 40+ int(rad * sin(angle))                   # same for y position
    dist = gauss_ran()                # length of random walk is straight
    trav = 0
                                        # new ball has a new random color
    ballcolor=(random.random(),random.random(),random.random())
               # next:while inside yellow circle random walk not finished
                       # explores if walk, if neighbor is occupied or not
    while( hit==0 and x<79 and x>1 and y<79 and y>1 and trav < abs(dist)):
        if(random.random() <0.5):
            step = 1              # 1/2 probability to advance or retreat
        else:
             step = -1;
        if ((grid[x+1,y] +grid[x-1,y] + grid[x,y+1] + grid[x,y-1]) >= 1):
          hit = 1                         # moving ball hits a fixed ball
          grid[x,y] = 1                   # this position is occupied now
          xc = x-40                     # transform   0<x<80 -> -40<xc<40
          yc = -y +40                   #             0<y<80 -> -40<yc<0
          sphere(pos=(xc,yc), radius=01.6, color=ballcolor)
        else:
            if ( random.random() < 0.5 ):        # prob 1/2 to move right
                x += step
            else:
                y += step                           # prob 1/2 to move up
            xp = x-40                             # linear transformation
            yp = -y+40                                     # to plot ball
            ball.color = ballcolor                 # ball in random color
            ball.pos = (xp,yp,0)               # continuous ball position
            rate(1500)                             # to change ball speed
        trav = trav+1    # increments distance, must be smaller than dist
