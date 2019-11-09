# Trap.py          trapezoid integration of t^2
#                A, B : endpoints,    N: points (not intervals)

from numpy import *

A = 0.0;    B = 3.0;    N = 100
h = (B - A)/(N - 1)
sum = 0.0                                                # initialization

for i in range(1, N + 1):                                     # trap rule
    t = A  +  (i-1)*h
    if ((i == 1) or (i ==  N)):   w = h/2.0             # end with wt=h/2
    else:   w = h
    sum  = sum  +  w * t * t
    
print('sum = ', sum)                                     # print integral
print("Enter and return a character to finish")
s = raw_input()
