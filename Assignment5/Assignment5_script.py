#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 12:24:21 2022

@author: annaromero
"""

#=====================
#IMPORT MODULES
#=====================
#-import numpy and/or numpy functions *
import numpy as np
#-import psychopy functions
from psychopy import core, gui, visual, event
#-import file save functions
import json
#-(import other functions as necessary: os...)
import os

#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
main_dir = os.getcwd()
print(main_dir)
#-define the directory where you will save your data
data_dir = os.path.join(main_dir,'data')
#-if you will be presenting images, define the image directory
image_dir = os.path.join(main_dir,'images')
print(image_dir)
#-check that these directories exist
if not os.path.isdir(image_dir):
    raise Exception("Could not find the path!")

if not os.path.isdir(data_dir):
    raise Exception("Could not find the path!")




#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, handedness
#get date and time
#-create a unique filename for the data

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
#-number of trials and blocks *
nTrials = 10
nBlocks = 2
#-stimulus names (and stimulus extensions, if images) *
cats = ['face']*10
imgs = ['01.jpg', '02.jpg', '03.jpg', '04.jpg', '05.jpg', 
        '06.jpg', '07.jpg', '08.jpg', '09.jpg', '10.jpg']

#-stimulus properties like size, orientation, location, duration *
stimSize = (200, 200)
stimDuration = 1
#-start message text *
startMesage = "Welcome to the experiment, press any key to begin"

#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
for pic in pics:
    if pic == image_dir:
        print("%p was found!" %pic)
    else:
        raise Exception("The image lists do not match up!")


#-create counterbalanced list of all conditions *
faces_stim = list(zip(cats, imgs))
print(faces_stim)


#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
#-create an empty list for correct responses (e.g., "on this trial, a response of X is correct") *
corrResp = []

#-create an empty list for participant responses (e.g., "on this trial, response was a X") *
partResp = []

#-create an empty list for response accuracy collection (e.g., "was participant correct?") *
respAcc = []

#-create an empty list for response time collection *
RT = [];

#-create an empty list for recording the order of stimulus identities *
stimOrder_id = []

#-create an empty list for recording the order of stimulus properties *
stimOrder_prop = []

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
#-define the window (size, color, units, fullscreen mode) using psychopy functions
#-define experiment start text unsing psychopy functions
#-define block (start)/end text using psychopy functions
#-define stimuli using psychopy functions
#-create response time clock
#-make mouse pointer invisible

#=====================
#START EXPERIMENT
#=====================
#-present start message text
#-allow participant to begin experiment with button press

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
for block in range(nBlocks):
    #-present block start message
    #-randomize order of trials here *
    np.random.shuffle(faces_stim)
    #-reset response time clock here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for trial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        #-empty keypresses
        
        #=====================
        #START TRIAL
        #=====================   
        #-draw stimulus
        #-flip window
        #-wait time (stimulus duration)
        #-draw stimulus
        #-...
        
        #-collect subject response for that trial
        #-collect subject response time for that trial
        #-collect accuracy for that trial
        
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
#-quit experiment

##code for assignment
n = 0
pics = []
while n < 10:
    n = n + 1
    pics.append('face' + f'{n:02}' + '.jpg') 
print(pics)


for pic in pics:
    if pic == image_dir:
        print("%p was found!" %pic)
    else:
        raise Exception("The image lists do not match up!")



    

