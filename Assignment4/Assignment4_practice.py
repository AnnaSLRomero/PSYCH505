#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 10:42:48 2022

@author: annaromero
"""
import random


###########Conditional Exercises#####################
######################################################
#####################################################
response = "NaN"


if response == "1" or response == "2":
    print("OK")
    if response == "1":
        print("Correct!")
    if response == "2":
        print("Incorrect!")
    
elif response == "NaN":
    print("Subject did not respond")
    
else: print("Subject pressed the wrong key")   


#############Loop Exercises####################
###################################################################
#################################################################

letters = ["A", "N", "N", "A"]
count = -1

for i in letters:
    print(i)
    count = count + 1
    print("This letter has a count of %i" %count)        

    
   # name = i
    #print(letters)
        #doing this prints out the list like 4 times
    #print(name)
        #this prints out each letter once through


names = ("Amy", "Rory", "River")
count = -1
l = -1

for i in names:
    l = l + 1
    print(names[count][l])
    print("This letter has a count of %i" %l)
    count = count + 1
    if count == 1:
        l = l + 1
        print(names[count][l])
        print("This letter has a count of %i" %l)
        count = count + 1





for i in names[count]:
    if count == 0:
        l0 = l + 1
        print(names[count][l0])
        print("This letter has a count of %i" %l0)
    if count == 1:
        l1 = l + 1
        print(names[count][l1])
        print("This letter has a count of %i" %l1)
    if count == 1:
        l2 = l + 1
        print(names[count][l2])
        print("This letter has a count of %i" %l2)
    
names = ("Amy", "Rory", "River")
count = -1
l = -1

for i in names:
    if i == names[0]:
        print(names[])


for i in names:
     if names == names[0]:
         l = l + 1
         print(names[count][l])
         print("This letter has a count of %i" %l)  


    if i == names[0]:
        print(names[0][l+1])
    for x in names[0]:
        if x == names[0][0]:
            count = count + 1
            print("This letter has a count of %i" %count)




for i in names:
    if i == names[0]:
        print(names[0][0],
              names[0][1],
              names[0][2])
    for x in names[0]:
        if x == names[0][0]:
            count = count + 1
            print("This letter has a count of %i" %count)
    
    elif i == names[1]:
        print(names[1][0],
              names[1][1],
              names[1][2],
              names[1][3])
        count = count + 1
        print("This letter has a count of %i" %count)
    
    elif i == names[2]:
        print(names[2][0],
              names[2][1],
              names[2][2],
              names[2][3],
              names[2][4])
        count = count + 1
        print("This letter has a count of %i" %count)
        
        
count = -1
l = -1

while count < 2 and l < 4:
    print(names[count][l])
    print("This letter has a count of %i" %l)
    count = count + 1
    l = l + 1
    


################################While loop exercises ######################
##########################################################################
##########################################################################

counter = 1
while counter <= 10:
    print("image1.png")
    print(counter)
    counter = counter + 1
while counter <= 20:
    print("image2.png")
    print(counter)
    counter = counter + 1
    


response = False
failsafe = -1

while not response:
    failsafe = failsafe + 1
    if failsafe == 5:
        break
    print("image.png")
    if random.randint(0,3) == 1 or 2:
        response == True
        
response = False
while not response:
    print("image.png")
    if random.randint(0,3) == 1 or 2:
        response == True


    

    