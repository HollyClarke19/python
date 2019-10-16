# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 09:37:03 2019

@author: medhcl
"""
import random 

#make a y variable between 0 and 99
y0 = random.randrange(100)
#Make an x variable between 0 and 99
x0 = random.randrange(100)

#print variables 
print(y0)
print(x0)

#code to alter y randomly

if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1
    
print(y0, x0)

#alters both y and x randomly 
if random.random() < 0.5:
    y0 += 1
    x0 += 1
else:
    y0 -= 1
    x0 -= 1
    
print(y0, x0)


#make a y variable 
y1 = random.randrange(100)
#Make an x variable 
x1 = random.randrange(100)

#print variables 
print(y1)
print(x1)

#code to alter y randomly

if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1
    
print(y0, x0)

#alters both y and x randomly 
if random.random() < 0.5:
    y1 += 1
    x1 += 1
else:
    y1 -= 1
    x1 -= 1
    
print(y1, x1)

# find pythagoran distance 
distance = ((y1 - y0) ** 2) + ((x1-x0) ** 2) ** 0.5
print(distance)
    