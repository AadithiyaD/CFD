import numpy as np
from matplotlib import pyplot as plt

nx = 41
dx = 2 / (nx - 1)
nt = 20 # no. of timesteps
dt = 0.025 # amt. of time each timestep covers

# Initialize velocity
u = np.ones(nx) 
u[int(0.5 / dx) : int(1 / dx + 1)] = 2

un = np.ones(nx)

for n in range(nt):
    un = u.copy()
    for i in range(1, nx):
        u[i] = un[i] - un[i] * dt / dx * (un[i] - un[i-1]) 

plt.plot(np.linspace(0, 2,nx), u)
plt.show()

# * changing parameters here shows the importance of the CFL Condition more clearly
# * Even under the basic parameters, the covected wave is not smooth
# * Taking characteristic velocity as 1m/s, we have CFL = 0.5. Reducing dt to 0.01 gives a smoother function, but will require more timesteps nt
