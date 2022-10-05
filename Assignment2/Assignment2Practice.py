#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 08:58:16 2022

@author: annaromero
"""
import numpy as np
import pprint as pp
import math
#Print exercises
print("A")
print("N")
print("N")
print("A")
#remember to save as Anna.py
#no not show up in variable editor

letter1 = "A"
letter2 = "N"
letter3 = "N"
letter4 = "A"
#yes show up in variable editor
#no problem with 2 different variables having the same value
#changing letterX did change the value of that variable

   letter1 = "A"
   letterX = letter3
   letter3 = "N"
   letter4 = "A"

letterX
letter3
   
   letter1 = "A"
   letterX = "N"
   letter3 = "Z"
   letter4 = "A"

#operation exercise
print(5/2)
print(5.0/2.0)
#I got the same answer
print(4%2)
print(10%2)
print(7%3)
print(20%3)
print(-7%4)
#gives me the remainder in diviision

print(5**10)
print(4**2)
#number to the power of the second number

print(4//2)
print(16//4)
print(25//5)
print(25//2)
#how much it goes into one without the remainder

print(7-4*3)
print(5+2+3*3/9)
#yes follows the rules

##boolean exercises
print(1 == 1.0)
print("1" == "1.0")
# float and integer are equivalent, but strings are not equivalent
print(5 == (3+2))
print((1 == 1.0) and not ("1" == "1.0") and (5 == (3+2)))
print((1 == 1.0) and ("1" != "1.0") and not (5 != (3+2)))
print((1 == 1.0) and not ("1" == "1.0") or (5 != (3+2)))
print((1 == 1.0) or ("1" != "1.0") and (5 == (3+2)))
print((1 == 1.0) and ("1" != "1.0") or (5 == (3+2)))

##List exercises
oddlist = [1, 3, 5, 7, 9]
#yes became a variable
print(oddlist)

print(len(oddlist))
#5

print(type(oddlist))
#list

intlist = list(range(1, 100))
print(intlist)

##Dicitionary exercises
about_me = {'name':'Anna', 
            'age':23.0, 
            'studyYear': 17, 
            'faves': ["chocolate almonds", "spaghetti", "coffee"],
            }
pp.pprint(about_me)
print(len(about_me))
#makes length by the type of things that there, so the list is one item
print(type(about_me))
##Array exercises
mixnums = np.array([1, 2, 3, 4.0, 5.0, 6.0])
print(mixnums)
#numbers now have decimals after the whole number, but no zero after.
print(type(mixnums))

mixtypes = np.array([1, 2, 3.0, 4.0, '5', '6'])
print(mixtypes)
#make them all strings

oddarray = np.arange(1, 100, 2)
print(oddarray)

logarray = np.logspace(math.log(1), 5, 16)
print(logarray)
