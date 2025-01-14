import numpy as np
from matplotlib import pyplot as plt
import time,sys


nx = 41 #no. of grid points
dx = 2 / (nx-1) #Distance n/w adjacent grid points
nt = 25 #No. of time steps
dt = 0.025 #Amt. of t ime each timestep covers
c = 1 #Assuming wavespeed c = 1

#Setting up initial conditions i.e Initializing
u = np.ones(nx)
u[int(0.5 / dx):int(1 / dx + 1)] = 2  # u = 2 b/w 0.5 and 1

# Plotting the initial velocity
plt.plot(np.linspace(0, 2, nx), u)
plt.show()
# * The hat graph isn't perfectly vertical because the transition from 1 => 2 is from element i => i + 1.
# * A perfectly vertical line would imply u is 1 and 2 at grid point i 
# * Can be made more vertical by reducing the spacing b/w the transition points i , i + 1

# Implementing discretization for time and space
un = np.ones(nx) # Tem array

for n in range(nt): # Runs nt times
    un = u.copy() # Copy current values of u to un
    for i in range(1, nx):
        u[i] = un[i] - c * dt/ dx * (un[i] - un[i-1])

# Plotting u after advancing in time
plt.plot(np.linspace(0, 2, nx), u)
plt.show()

# * The hat function we initialized is no longer vertical - why?
# * Our discretization scheme is only an approximation for the true convective motion
# * To get better results, we would either have to use a higher order scheme, or use more grid points with smaller spacing
# * This must be done with respect to the CFL stability criterion, otherwise our solution may diverge or have inaccuracies
# * Doubling nx to 82, with nt = 0.025 results in an oscillation at the start and end of the convected wave - a case of numerical dispersion
# * Also, a sharp function like the hat function lends itself to being "smeared". A smooth initialization of velocity is more likely to have its shape preserved

