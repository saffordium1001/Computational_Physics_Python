# determines approximate machine precision

N = 10
eps = 1.0

for i in range(N):
    eps = eps/2
    one_Plus_eps = 1.0  +  eps
    print('eps = ', eps, ', one  +  eps = ', one_Plus_eps)
