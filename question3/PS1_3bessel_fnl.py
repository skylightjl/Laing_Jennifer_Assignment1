#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 23:01:15 2018

@author: jenniferlaing


CTA200H 2018
Problem Set #1

Question #3
Bessel Function and Point Spread Function (PSF)

"""
import numpy as np
import scipy as sc
from scipy.ndimage.filters import convolve
import matplotlib.pyplot as plt
import matplotlib.image as mpim


"""

Part (a)

"""
m = np.linspace(0,5,6)
x = np.linspace(0,10,1000)

#define the function to integrate
def J_function(theta,m,x):
    return np.cos(m * theta - x * np.sin(theta))

integrate = []

for item in m:
    temp = []
    for k in x:
        tempI, tempErr = sc.integrate.quad(J_function, 0, np.pi, args=(item,k))
        temp.append(tempI)
    integrate.append(temp)
bessel = (1/np.pi) * np.array(integrate)

plt.figure()
for i in bessel:
    plt.plot(x,i)
plt.xlabel('x')
plt.ylabel('Bessel function')
plt.title('Results for 6 values of m')
plt.savefig("Output_images/Bessel_all.png",dpi=300) #----------------***image
plt.show()

plt.plot(x,bessel[1,:])
plt.xlabel('x')
plt.ylabel('Bessel function')
plt.title('Result for m=1')
plt.savefig("Output_images/Bessel_m1.png",dpi=300) #----------------***image
plt.show()




"""

Part (b)

"""
#meshgrid
x = np.arange(-5, 5, 0.01)
y = np.arange(-5, 5, 0.01)
xx, yy = np.meshgrid(x, y, sparse=True)
I_0 = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)
#h = plt.contourf(x,y,I_0)
#plt.show()

#Given a chosen set of parametres
a = 0.0089 #radius in metres
#q = np.linspace(0,10,1000) #distance from optical axis
q = np.sqrt(xx**2 + yy**2)
lmda = 1e-6 #wavelength of the light in metres
R = 0.05 #distance from the aperture to the focal plane in metres
x1 = 2 * np.pi * a * q / lmda * R

#Point Spread Function
I_x = I_0 * (2 * bessel[1] / x1)**2

#show a 2D image of the Point Spread Function
h = plt.contourf(x,y,I_x)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('x')
plt.ylabel('y')
plt.title('2-D Point Spread Function')
plt.savefig("Output_images/PSF.png",dpi=300) #----------------***image
plt.show()

#show a 2D image of the Point Spread Function
h = plt.contourf(x,y,I_x)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlim(-0.05,0.05)
plt.ylim(-0.05,0.05)
plt.xlabel('x')
plt.ylabel('y')
plt.title('2-D Point Spread Function - zoomed-in')
plt.savefig("Output_images/PSF-zoom.png",dpi=300) #----------------***image
plt.show()




"""

Part (c)

"""
#import an image

# Read in a TIF image and return an 2D array
def readtif(file):
    img = mpim.imread(file)
    img = 1.0 * img[:,:,0]   # convert to floating point   
    return(img)

im = "getimages/potw1819a_NASA.tif"
nasa_im = readtif(im)
plt.imshow(nasa_im)
plt.xlabel('pixels')
plt.ylabel('pixels')
plt.savefig("Output_images/Astroimage_Nasa.png",dpi=300) #----------------***image
plt.show()

plt.imshow(nasa_im[400:470,400:470])
plt.xlabel('pixels')
plt.ylabel('pixels')
plt.savefig("Output_images/Astroimage_Nasa_portion.png",dpi=300) #----------------***image
plt.show()

#crop the image
nasa_im_sm = nasa_im[400:470,400:470]

#convolve a portion of the image using the PSF
convolve_image = convolve(nasa_im_sm,I_x)

plt.imshow(convolve_image)
plt.savefig("Output_images/Astroimage_Nasa_portion_convolved.png",dpi=300) #----------------***image
plt.show()




