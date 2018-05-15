#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 22:29:52 2018

@author: jenniferlaing


CTA200H 2018
Problem Set #1

Question #2
The binomial Coefficient

"""
import numpy as np
import scipy.special as spc
import random
import matplotlib.pyplot as plt


"""

Part (a)

"""
#define a function to compute the binomial
def binomial(n,k):
    if k==n:
        return 1
    elif k==1:
        return n
    elif k > n:
        return 0
    else:
        return int(spc.factorial(n) / (spc.factorial(k) * spc.factorial(n-k)))
    

#Request inputs to test binomial function
n = int(input("To test binomial coefficient function, please enter a value for n: "))
k = int(input("Please enter a value for k: "))
print(binomial(n,k))
  


"""

Part (b)

"""  
#write out the first 20 lines of Pascal's Triangle
for i in np.linspace(0,19,20):
    print([int(binomial(i,k)) for k in np.arange(i+1)])



"""

Part (c)

"""
#Consider a biased coin. The probability of obtaining heads k times in n flips
#randomly chosen variables to check the function
#k=1
#n=4
#p=.25

#define a function to calculate probability
def P(k,n,p):
    return binomial(n,k) * p**k * (1-p)**(n-k)

print(P(1,4,.25))




"""

Part (d)

"""
#Experiment: flip the coin n times and hope to get k values of heads.
#Randomly choose values for k,n and p
#Run the experiment N times for N in {10, 100, 1000}
#record the results in a plot.

#select a range for each variable from which to randomly choose
range_k = np.arange(1,5)
range_n = np.arange(1,15)
range_p = np.linspace(0,1,25)

#Experiment for N = 10
N_10 = []
for i in np.arange(10):
    prob = P(random.choice(range_k),random.choice(range_n),random.choice(range_p))
    N_10.append(prob)

plt.plot(N_10)
plt.xlabel('Number of trials [N]')
plt.ylabel('Probability [P]')
plt.title('Results for N = 10')
#plt.savefig("Output_images/N_10.png",dpi=300) #----------------***image
plt.show()

#Experiment for N = 100
N_100 = []
for i in np.arange(100):
    prob = P(random.choice(range_k),random.choice(range_n),random.choice(range_p))
    N_100.append(prob)
    
plt.plot(N_100)
plt.xlabel('Number of trials [N]')
plt.ylabel('Probability [P]')
plt.title('Results for N = 100')
#plt.savefig("Output_images/N_100.png",dpi=300) #----------------***image
plt.show()   
 
#Experiment for N = 1000   
N_1000 = []
for i in np.arange(1000):
    prob = P(random.choice(range_k),random.choice(range_n),random.choice(range_p))
    N_1000.append(prob)

plt.plot(N_1000)
plt.xlabel('Number of trials [N]')
plt.ylabel('Probability [P]')
plt.title('Results for N = 1000')
#plt.savefig("Output_images/N_1000.png",dpi=300) #----------------***image
plt.show()








