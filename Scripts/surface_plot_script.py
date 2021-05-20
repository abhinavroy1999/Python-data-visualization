'''
Script info: Script to produce surface plot using mplot3d tool of PyPlot module
Date: 06/05/21

Copyright (C) 2021  Abhinav Roy

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
# Import NumPy, mpl_toolkits and PyPlot
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

# Define a meshgrid for X and Y axis
x, y = np.mgrid[-5:5:20j, -5:5:20j]

# Value of the function
z = np.sqrt(x*x + y*y + x*y)

# Setting size of the figure window
dim = 512
size = 4*dim, 3*dim
dpi = 300.0
figsize = size[0] / float(dpi), size[1] / float(dpi)
fig = plt.figure(figsize=figsize, dpi=dpi)

# Passing the axis line object handle
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none', cstride=1, rstride=1, antialiased=True)
ax.view_init(35.264, 45)

# Save the figure and display it using a suitable backend
plt.savefig('../Figures/surf_plot.png')
plt.show()
