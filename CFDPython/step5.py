from mpl_toolkits.mplot3d import Axes3D

import numpy as np
from matplotlib import pyplot as plt

# Variables
nx = 81
ny = 81
nt = 100
c = 1
dx = 2 / (nx - 1)
dy = 2 / (ny - 1)
sigma = 0.2
dt = sigma * dx

x = np.linspace(0, 2, nx)
y = np.linspace(0, 2 ,ny)

u = np.ones((ny, nx)) # Creating a 1xn vector of 1's
un = np.ones((ny, nx))

#Initial cdns (conditions)
#Seeting hat function I.C
u[int(0.5 / dy) : int(1 / dy + 1), int(0.5 / dx) : int(1 / dx + 1)] = 2

#Plot Initial Condition
fig = plt.figure(figsize=(11, 7), dpi=100)
ax = fig.add_subplot(projection='3d')       #Use add_subplot instead of gca as in repo                 
X, Y = np.meshgrid(x, y)                            
surf = ax.plot_surface(X, Y, u[:], cmap=plt.cm.viridis) #Do plt.cm instead of cm.viridis as in repo
plt.show()

# #Using nested loops
# u = np.ones((ny, nx))
# u[int(0.5 / dy) : int(1 / dy + 1), int(0.5 / dx) : int(1 / dx + 1)] = 2

# for n in range(nt + 1):
#     un = u.copy()
#     row, col = u.shape
#     for j in range(1, col):
#         for i in range(1, col):
#             u[j, i] = (un[j, i] - (c * dt / dy * (un[j, i] - un[j, i -1])) -
#                                   (c * dt / dy * (un[j, i] - un[j - 1, i])))
            
#             u[0, :] = 1
#             u[-1, :] = 1
#             u[:, 0] = 1
#             u[:, -1] = 1

# fig = plt.figure(figsize=(11, 7), dpi=100)
# ax = fig.add_subplot(projection='3d')       #Use add_subplot instead of gca as in repo                                 
# surf2 = ax.plot_surface(X, Y, u[:], cmap=plt.cm.viridis) #Do plt.cm instead of cm.viridis as in repo
# plt.show()

# Using numpy arrays
u = np.ones((ny, nx))
u[int(0.5 / dy) : int(1 / dy + 1), int(0.5 / dx) : int(1 / dx + 1)] = 2

for n in range(nt + 1):
    un = u.copy()
    u[1:, 1:] = (un[1:, 1:] - (c * dt / dx * (un[1:, 1:] - un[1:, :-1])) -
                              (c* dt / dy * (un[1:, 1:] - un[:-1, 1:])))
    
    u[0, :] = 1
    u[-1, :] = 1
    u[:, 0] = 1
    u[:, -1] = 1

fig = plt.figure(figsize=(11, 7), dpi=100)
ax = fig.add_subplot(projection='3d')       #Use add_subplot instead of gca as in repo                                 
surf3 = ax.plot_surface(X, Y, u[:], cmap=plt.cm.viridis) #Do plt.cm instead of cm.viridis as in repo
plt.show()

# * The use with numpy arrays is MUCH more faster than using nested for loops