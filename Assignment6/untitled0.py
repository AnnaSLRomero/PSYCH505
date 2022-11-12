#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 09:32:58 2022

@author: annaromero
"""

from psychopy import gui
from datetime import datetime
import os
from psychopy import visual, monitors, event
import numpy as np

#########Q1###########
#dictionary for dialog box gui
exp_info = {'subject_nr':0, 'age':0, 'handedness':('right','left','ambi'), 
            'gender':('male', 'female', 'other', 'prefer not to say'), 'session': 1}

print(exp_info)

my_dlg = gui.DlgFromDict(dictionary=exp_info, fixed = ['session'])

#########Q2###########
exp_info = {'subject_nr':0, 'age':0, 'handedness':('right','left','ambi'), 
            'gender':(), 'session': 1}

#########Q1 and Q2###########
my_dlg = gui.DlgFromDict(dictionary=exp_info, title = "subject info", fixed = ['session'])

###########Q3########
my_dlg = gui.DlgFromDict(dictionary=exp_info, title = "subject info", fixed = ['session'],
                         show = False)

print("All variables have been created! Now ready to show the dialog box!")

my_dlg = gui.DlgFromDict(dictionary=exp_info, title = "subject info", fixed = ['session'])

####Q4####
#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, handedness
exp_info = {'subject_nr':(), 'age':(), 'handedness':('right','left','ambi'), 
            'gender':(), 'session': 1}

my_dlg = gui.DlgFromDict(dictionary=exp_info, title = "subject info", fixed = ['session'])

#get date and time
date = datetime.now()
exp_info['date'] = str(date.day) + "-" + str(date.month) + "-" + str(date.year)
print(exp_info['date'])

#-create a unique filename for the data
filename = str(exp_info['subject_nr']) + '_' + exp_info['date'] + '.csv'
print(filename)
main_dir = os.getcwd()
sub_dir = os.path.join(main_dir,'sub_info',filename)

####### MONITOR AND WINDOW EXERCISES ######
mon = monitors.Monitor('myMonitor', width = 30.41, distance = 60)
mon.setSizePix([2500, 1600])
mon.save()

win = visual.Window(monitor=mon, 
                    color = ["burlywood"],
                    fullscr = True)

##########STIMULUS EXERCISES######

main_dir = os.getcwd()
print(main_dir)
image_dir = os.path.join(main_dir, 'images')

stims = ['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg', 'face05.jpg',
         'face06.jpg', 'face07.jpg', 'face08.jpg', 'face09.jpg', 'face10.jpg']


nTrials = 10
my_image = visual.ImageStim(win)

np.random.shuffle(stims)

for trial in range(nTrials):
    my_image.image = 0s.path.join(image_dir, stims[trial])
    my_image.pos = 
    my_image.draw()
    win.flip()
    event.waitKeys()
win.close()


pic_loc = os.path.join(image_dir, 'face02.jpg')
print(image_dir)



my_image = visual.ImageStim(win, image = pic_loc)

my_image.draw()
win.flip()
event.waitKeys()
win.close()

fix_text = visual.TextSim(win, text = "+")

##############################COMPLETE#########################
mon = monitors.Monitor('myMonitor', width = 30.41, distance = 60)
mon.setSizePix([2500, 1600])
mon.save()
thisSize = mon.getSizePic()
thisWidth = thisSize[0]
thisHeight = thisSize[1]

win = visual.Window(monitor=mon, 
                    color = ["burlywood"],
                    fullscr = True)
                    

main_dir = os.getcwd()
print(main_dir)
image_dir = os.path.join(main_dir, 'images')

stims = ['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg', 'face05.jpg',
         'face06.jpg', 'face07.jpg', 'face08.jpg', 'face09.jpg', 'face10.jpg']

horizMult = [1, -1, 1, -1]
vertMult = [1, 1, -1, -1]


nTrials = 10
fix_text = visual.TextStim(win, text = "+")
my_image = visual.ImageStim(win, units = "pix", size = (400,400),
                            interpolate = True)

np.random.shuffle(stims)

for trial in range(nTrials):
    my_image.image = os.path.join(image_dir, stims[trial])
    my_image.pos = (horizMult[trial] * thisWidth/4, vertMult[trial] * thisHeigh/4)
    my_image.draw()
    fix_text.draw()
    win.flip()
    event.waitKeys()
win.close()


x_axis = [-360, -360, 360, 360, -360, -360, 360, 360, -360, -360]
y_axis = [-225, 225, 225, -225, -225, 225, 225, -225, -225, 225,]
coords = list(zip(x_axis, y_axis))


