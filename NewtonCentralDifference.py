
# NewtonCD.py    Newton Search with central difference

from math import cos

x = 4.;         dx = 3.e-1;        eps = 0.2;                # Parameters
imax = 100;                                        # Max no of iterations

def f(x):                                                     # Function
    return 2*cos(x) - x

for it in range(0, imax + 1):
    F = f(x)
    if ( abs(F) <= eps ):                         # Check for convergence
        print("\n Root found, F =", F, ", tolerance eps = " , eps) 
        break
    print("Iteration # = ", it, " x = ", x, " f(x) = ", F)
    df = ( f(x + dx/2)  -  f(x - dx/2) )/dx               # Central diff
    dx = - F/df 
    x   += dx                                                 # New guess
