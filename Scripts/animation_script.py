'''
Script info: Script to produce sin wave animation Mayavi and MoviePy
Date: 03/05/21

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
# Import Mayavi, NumPy, MoviePy modules
import numpy as np
from mayavi import mlab
import moviepy.editor as mpy

# Set the duration of the GIF animations
duration = 2

# Pass the handle of the figure object to the variable
fig = mlab.figure(size = (512,512), bgcolor=(0,0,0))

# Defining a mesh grid for the X and Y axis
x, y = np.mgrid[-3:3:100j, -3:3:100j]

# Defining the variable sin function in 3D space
z = lambda d: np.sin(x*x + y*y + d)

# Define the function for building frames of the animation
def make_frame(t):
    mlab.clf()
    a = mlab.surf(x, y, z(2*np.pi*t/duration), figure=fig, colormap='cool')
    return mlab.screenshot(antialiased=True)

# Making the animation object
animation = mpy.VideoClip(make_frame, duration=duration)

#Writing the generated GIF animation to a file
animation.write_gif("../Animations/waves.gif", fps=20)
