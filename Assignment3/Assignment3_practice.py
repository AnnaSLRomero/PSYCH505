#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 17:21:23 2022

@author: annaromero
"""
import numpy as np

##variable ops
sub_code = "sub"
subnr_int = 2
subnr_str = "2"

print(sub_code + subnr_str)
print(sub_code + subnr_int)

print(sub_code + " " + subnr_str)

print(sub_code + " " + subnr_str*3)

print((sub_code + subnr_str)*3)

print((sub_code*3)+(subnr_str*3))

#list ops
numlist = [1,2,3]
numlist * 2

numarr = np.array([1,2,3])
numarr*2

#list multiplies the 1,2,3 twice therefore doubling the length, 
#while in an array the values multiplied by 2, so same length, but the values have changed to 2,4,6.

strlist = ['do', 're', 'mi', 'fa']

