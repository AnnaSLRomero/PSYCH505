#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 17:21:23 2022

@author: annaromero
"""
import numpy as np

##variable operation exercises
sub_code = "sub"
subnr_int = 2
subnr_str = "2"

print(sub_code + subnr_str)
print(sub_code + subnr_int)

print(sub_code + " " + subnr_str)

print(sub_code + " " + subnr_str*3)

print((sub_code + subnr_str)*3)

print((sub_code*3)+(subnr_str*3))

#list operation exercises
numlist = [1,2,3]
numlist * 2

numarr = np.array([1,2,3])
numarr*2

#list multiplies the 1,2,3 twice therefore doubling the length, 
#while in an array the values multiplied by 2, so same length, but the values have changed to 2,4,6.

#### STRUGGLING WITH THIS ONE!!
strlist = ['do', 're', 'mi', 'fa']

print(strlist[0]*2, strlist[1]*2, strlist[2]*2, strlist[3]*2)
print(strlist * 2)
print(strlist[0], strlist[0], 
      strlist[1], strlist[1],
      strlist[2],strlist[2],
      strlist[3], strlist[3])

print([strlist[0], strlist[0]], 
      [strlist[1], strlist[1]],
      [strlist[2],strlist[2]],
      [strlist[3], strlist[3]])





#zipping - check if this is correct
faces = ['face1.png', 'face2.png', 'face3.png', 'face4.png', 'face5.png'] * 2
houses = ['house1.png', 'house2.png', 'house3.png', 'house4.png', 'house5.png'] * 2
postCue = ['cue1'] * 5 + ['cue2'] * 5

completeOrder = list(zip(faces, houses, postCue))
print(completeOrder)

np.random.shuffle(completeOrder)
print(completeOrder)

#Indexing
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

print(colors[-2])
print(colors[-2][-2] + " " + colors[-2][-1])

colors.remove(colors[-1])
colors.extend(["indigo", "violet"])
print(colors)

#slicing
list100 = list(range(0, 101))
print(list100)
print(list100[:10])
print(list100[99::-2])
print(list100[:-5:-1])
print(list100[39:43] == 39, 40, 41, 42)



print(list100[43] == 43)
