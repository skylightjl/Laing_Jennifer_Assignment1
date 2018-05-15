#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 23:01:15 2018

@author: jenniferlaing


CTA200H 2018
Problem Set #1

Question #5
Analytical vs numerical computation of the derivative

"""

import numpy as np
import matplotlib.pyplot as plt

#------------------------------------Analytical solution
#Calculated by hand
#f(x) = x(x-1)
#f'(x) = 2x-1


#------------------------------------Numerical solution

delta = np.linspace(1e-4, 1e-14, 50)
deltalog = np.logspace(1e-4, 1e-14, 50)

def f(x):
    return x * (x-1)

def derivative(x):
    return (f(x+delta) - f(x))/delta

#test the function
drv = derivative(1)

#plot the results
plt.plot(delta,drv)
plt.xlabel('delta')
plt.ylabel('derivative')
plt.title('Numerical solution to derivative')
plt.savefig("Output_images/derivative.png",dpi=300) #----------------***image
plt.show()

plt.semilogx(delta,drv)
plt.xlabel('delta [log]')
plt.ylabel('derivative')
plt.title('Numberical solution to derivative')
plt.savefig("Output_images/derivative_log.png",dpi=300) #----------------***image
plt.show()


