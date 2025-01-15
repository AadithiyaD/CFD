import numpy as np
from matplotlib import pyplot as plt

def linearconv(nx):
    dx = 2/ (nx - 1)
    nt = 20 # No. of timesteps
    dt = 0.025 # Delta t
    c = 1

    u = np.ones(nx)
    u[int(0.5/dx) : int (1 / dx+1)] = 2

    un = np.ones(nx)

    for n in range(nt):
        un = u.copy()
        for i in range(1,nx):
            u[i] = un[i] - c * dt/dx *(un[i] - un[i-1])
    
    plt.plot(np.linspace(0, 2, nx), u)
    plt.show()

linearconv(41)