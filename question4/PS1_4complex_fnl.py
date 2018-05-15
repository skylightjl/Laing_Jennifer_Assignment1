#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 23:01:15 2018

@author: jenniferlaing


CTA200H 2018
Problem Set #1

Question #4
Complex Plane

"""
import numpy as np
import matplotlib.pyplot as plt


#Set up a meshgrid
#Use equation for each point in the complex plane: c = x + 1j*y
x = np.arange(-2, 2, 0.1)
y = np.arange(-2, 2, 0.1)
xx, yy = np.meshgrid(x,y)
c = xx + 1j*yy
print("c",c)
plt.plot(xx,yy,marker='.')
plt.xlabel('x range')
plt.ylabel('y range')
plt.title('Meshgrid')
plt.show()

#Calculate z
iterations=180
z_array = np.zeros((iterations,len(x),len(y)),dtype='complex')
for i in np.arange(iterations):
    if i == 0:
        z = 0
    else:
        z = z**2 + c  #I get a runtime warning saying there is \
#    \an invalid value in the square. I wonder if this relates \
#    \to why the image produced is pixelated.
    z_array[i,:,:]=z    
print(np.shape(z_array))

#set nans to 0 and else to 1 to plot
zfinal = z_array[-1,:,:]

#zz = abs(zfinal**2)
#RealImag = np.real(zfinal)**2 + np.imag(zfinal)**2
#print("zz",zz)
#print("ls",RealImag)

#zplot = zfinal*1.
#zplot[zplot != np.nan] = 1.
#zplot[zplot == np.nan] = 0.

#plot image of the real values
#the image is pixelated
plt.imshow(np.real(zfinal))
plt.xlim(0,30)
plt.ylim(5,30)
plt.xlabel('x grid')
plt.ylabel('y grid')
plt.title('Real values and the point at which they diverge')
plt.savefig("Output_images/RealValues_plot.png",dpi=300) #----------------***image
plt.show()

print(zfinal)



