'''
Script info: Script to produce a plot using PyPlot module of Matplotlib package
Date: 02/05/21

Copyright (C) 2020  Abhinav Roy

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

# Importing the modules into the workspace
import numpy as np
import matplotlib.pyplot as plt

# Importing the data file to be plotted
data_set = np.loadtxt('../Processed_data/viral_load_data.txt')
x_dat = data_set[:,0]
y_dat = data_set[:,1]

# Setting size of the figure window
dim = 720
size = 4*dim, 3*dim
dpi = 300.0
figsize = size[0] / float(dpi), size[1] / float(dpi)
fig, ax = plt.subplots(figsize=figsize, dpi=dpi)

# Plotting the x & y data
plt.plot(x_dat,y_dat)
plt.grid()
plt.axis('tight')

# Passing the handle of line object to a variable
ax = plt.gca()
ax.set_title('HIV Virus data', family='Arial', size=18, weight='bold')
ax.set_xlabel("Time since treatement", family='Arial', size=16, labelpad=12)
ax.set_ylabel("Viral load", family='Arial', size=16, labelpad=14)

# Defining the axis line widths
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(2.5)

# Setting the line attributes
lines = ax.get_lines()
plt.setp(lines[0], linestyle='-', linewidth=3, color='b')

# Set the legends
lines[0].set_label("viral load data")
ax.legend()

# Print the plot
plt.savefig("../Figures/viral_load_plot")

# Display the plot
plt.show()
