#
from visual import *
from visual.graph import *
import random
Minx = 0                                               # min value x axis
Maxx = 200                                             # max value x axis
Miny = 0                                                     # for y axis
Maxy = 60
g = gdisplay(width=500, height=500, title="Coastline", xtitle='x',ytitle='coast',xmin=Minx, xmax=Maxx, ymin=Miny, ymax=Maxy)
seacoast = gcurve(color=color.yellow)
coast = zeros((200))                                              # array
for i in range(0, 5000):                          # All particles dropped
    spot = int(200*random.random())              # generate random number
    if (spot == 0):                 # Hitting edge counts as filling hole
        if (coast[spot] < coast[spot + 1]):
            coast[spot] = coast[spot + 1]
        else:
            coast[spot]= coast[spot] + 1
    else:
        if (spot == 199):
            if (coast[spot] < coast[spot - 1]):
                coast[spot] = coast[spot - 1]
            else:
                coast[spot]=coast[spot] + 1
        else:
            if ((coast[spot]<coast[spot - 1])and
                (coast[spot]<coast[spot + 1])):
                if (coast[spot-1] > coast[spot + 1]):
                     coast[spot] = coast[spot - 1]
                else:
                     coast[spot] = coast[spot + 1]
            else:
                coast[spot] = coast[spot] + 1
for i in range(0,200):
   seacoast.plot(pos=(i,coast[i]))                       # plot coastline
