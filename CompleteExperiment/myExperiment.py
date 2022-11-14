#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 08:56:41 2022

@author: annaromero
"""

#=====================
#IMPORT MODULES
#=====================
#-import numpy and/or numpy functions *
import numpy as np
#-import psychopy functions
from psychopy import core, gui, visual, event, monitors
#-import file save functions
import json
#-(import other functions as necessary: os...)
import os
from datetime import datetime

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
exp_info = {'subject_nr':(), 'age':(), 'handedness':('right','left','ambi'), 
            'gender':(), 'session': 1} #dictionary

my_dlg = gui.DlgFromDict(dictionary=exp_info, title = "subject info", fixed = ['session'])

#get date and time
date = datetime.now()
exp_info['date'] = str(date.day) + "-" + str(date.month) + "-" + str(date.year)

#-create a unique filename for the data
filename = str(exp_info['subject_nr']) + '_' + exp_info['date'] + '.csv'
print(filename)
main_dir = os.getcwd()
sub_dir = os.path.join(main_dir,'sub_info',filename)

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
#-number of trials and blocks *
nTrials = 10
nBlocks = 2
#-stimulus names (and stimulus extensions, if images) *
stims = ['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg', 'face05.jpg',
         'face06.jpg', 'face07.jpg', 'face08.jpg', 'face09.jpg', 'face10.jpg']

#-stimulus properties like size, orientation, location, duration *
x_axis = [-360, -360, 360, 360, -360, -360, 360, 360, -360, -360]
y_axis = [-225, 225, 225, -225, -225, 225, 225, -225, -225, 225]
coords = list(zip(x_axis, y_axis)) #coordinates for the stim presentation
stimDuration = 1 #timing for stim


#-start message text *
start_msg = "Welcome to the experiment, press any key to begin"

#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
for pic in stims:
    if pic == image_dir:
        print("%p was found!" %pic)
    else:
        raise Exception("The image lists do not match up!")


#-create counterbalanced list of all conditions *
np.random.shuffle(stims)


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
mon = monitors.Monitor('myMonitor', width = 30.41, distance = 60)
mon.setSizePix([2500, 1600])

#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon, 
                    color = ["burlywood"], 
                    fullscr = True)

#-define experiment start text using psychopy functions
start_text = visual.TextStim(win, text = start_msg)

#-define block (start)/end text using psychopy functions
block_msg = "Press any key to continue to the next block."
end_trial_msg = "End of trial"
block_text = visual.TextStim(win, text = block_msg)

#-define stimuli using psychopy functions
fix_text = visual.TextStim(win, text = "+")

#-create response time clock
#-make mouse pointer invisible

#=====================
#START EXPERIMENT
#=====================
#-present start message text
start_text.draw()
win.flip()
#-allow participant to begin experiment with button press
event.waitKeys()

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
for block in range(nBlocks):
    #-present block start message
    block_text.draw()
    win.flip()

    
    #-reset response time clock here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for trial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        my_image = visual.ImageStim(win, units = "pix", size = (400, 400))
        my_image.image = os.path.join(image_dir, stims[trial])
        my_image.pos = coords[trial]
        #-empty keypresses
        event.waitKeys()
        
        #=====================
        #START TRIAL
        #=====================   
       #-draw fixation
        fix_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(1)
        
        #-draw image
        my_image.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(1)
        
        #-draw end trial text
        end_trial_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(1)
        
        #-collect subject response for that trial
        #-collect subject response time for that trial
        #-collect accuracy for that trial
        
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
win.close()
#-quit experiment








