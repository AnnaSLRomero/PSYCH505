# Assignment 6
```
from psychopy import gui
from datetime import datetime
import os
from psychopy import visual, monitors
```
## Dialog box exercises
1)
```
from psychopy import gui

#dictionary for dialog box gui
exp_info = {'subject_nr':0, 'age':0, 'handedness':('right','left','ambi'), 
            'gender':('male', 'female', 'other', 'prefer not to say'), 'session': 1}
```

2)
```
exp_info = {'subject_nr':0, 'age':0, 'handedness':('right','left','ambi'), 
            'gender':(), 'session': 1}
            
```
## Using DlgFromDict:
1)
```
my_dlg = gui.DlgFromDict(dictionary=exp_info, title = "subject info")
```
2)
```
my_dlg = gui.DlgFromDict(dictionary=exp_info, title = "subject info", fixed = ['session'])
```
Making session fixed, makes it unchangeable by the participant and keeps the session as "1".

3)
```
exp_info = {'subject_nr':0, 'age':0, 'handedness':('right','left','ambi'), 
            'gender':(), 'session': 1}

my_dlg = gui.DlgFromDict(dictionary=exp_info, title = "subject info", fixed = ['session'],
                         show = False)

print("All variables have been created! Now ready to show the dialog box!")

my_dlg = gui.DlgFromDict(dictionary=exp_info, title = "subject info", fixed = ['session'])
#I didn't add show = True, because True is the default
```
4)
```
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

```
## Monitor and Window Exercises
1) For some reason changing units does not affect my window size. I have changed it from "height", "cm", "deg", and "norm", and with the same size (800x800)
and the size of the window is the same.

2) Changing the colour space, changes the way that color is defined. Psychopy had 3 colour spaces: RGB, DKL, and LMS. For RGB and LMS for color[0,0,0] the values
inside can only be between -1 to 1. In DSV the values in color[0,0,0] can range from 0 and higher. This is also because each of the 3 values are defined by specific
aspects of each of the chosen spaces, like RGB, specifies the amount fo red, green, or blue there is to make the chosen color. You can also specify the color you want with hexvalues or names.
Therefore, instead of specifying the color space you just write in: color["#FFFAF0"] or color["burlywood"]. So yes you can define colors by name.

3)
```
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
```

## Stimulus Exercises
1)
```
main_dir = os.getcwd()
print(main_dir)
image_dir = os.path.join(main_dir, 'images')

stims = ['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg', 'face05.jpg',
         'face06.jpg', 'face07.jpg', 'face08.jpg', 'face09.jpg', 'face10.jpg']
nTrials = 10
my_image = visual.ImageStim(win, units = "pix", size = (400, 400))

np.random.shuffle(stims)

for trial in range(nTrials):
    my_image.image = os.path.join(image_dir, stims[trial])
    my_image.draw()
    win.flip()
    event.waitKeys()
win.close()
```
To keep the dimensions and change size, it says the best thing to do is change the dimensions before it is even displayed in psychopy and changed in psychopy.

2)
```
mon = monitors.Monitor('myMonitor', width = 30.41, distance = 60)
mon.setSizePix([2500, 1600])
mon.save()

win = visual.Window(monitor=mon, 
                    color = ["burlywood"],
                    fullscr = True)
                    

main_dir = os.getcwd()
print(main_dir)
image_dir = os.path.join(main_dir, 'images')

stims = ['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg', 'face05.jpg',
         'face06.jpg', 'face07.jpg', 'face08.jpg', 'face09.jpg', 'face10.jpg']

x_axis = [-360, -360, 360, 360, -360, -360, 360, 360, -360, -360]
y_axis = [-225, 225, 225, -225, -225, 225, 225, -225, -225, 225]
#I got these coordinate values from the mon.save(), where it told me that the actual monitor size is [1440, 900], which I split in half 2x to get
#[360, 225], so that each image stimulus will be in the middle of each quadrant.
coords = list(zip(x_axis, y_axis))


nTrials = 10
my_image = visual.ImageStim(win, units = "pix", size = (400, 400))

np.random.shuffle(stims)

for trial in range(nTrials):
    my_image.image = os.path.join(image_dir, stims[trial])
    my_image.pos = coords[trial]
    my_image.draw()
    win.flip()
    event.waitKeys()
win.close()
```
3)
```
main_dir = os.getcwd()
print(main_dir)
image_dir = os.path.join(main_dir, 'images')

stims = ['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg', 'face05.jpg',
         'face06.jpg', 'face07.jpg', 'face08.jpg', 'face09.jpg', 'face10.jpg']

x_axis = [-360, -360, 360, 360, -360, -360, 360, 360, -360, -360]
y_axis = [-225, 225, 225, -225, -225, 225, 225, -225, -225, 225,]
coords = list(zip(x_axis, y_axis))


nTrials = 10
fix_text = visual.TextStim(win, text = "+")
my_image = visual.ImageStim(win, units = "pix", size = (400, 400))

np.random.shuffle(stims)

for trial in range(nTrials):
    my_image.image = os.path.join(image_dir, stims[trial])
    my_image.pos = coords[trial]
    my_image.draw()
    fix_text.draw()
    win.flip()
    event.waitKeys()
win.close()
```
4)
```
from psychopy import gui
from datetime import datetime
import os
from psychopy import visual, monitors, event
import numpy as np

nBlocks = 2
nTrials = 10

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define experiment start text unsing psychopy functions
start_msg = "Welcome to my experiment! Press any key."
start_text = visual.TextStim(win, text = start_msg)
#-define block (start)/end text using psychopy functions
block_msg = "Press any key to continue to the next block."
end_trial_msg = "End of trial"
block_text = visual.TextStim(win, text = block_msg)
end_trial_text = visual.TextStim(win, text = end_trial_msg)
#-define stimuli using psychopy functions (images, fixation cross)
main_dir = os.getcwd()
print(main_dir)
image_dir = os.path.join(main_dir, 'images')

stims = ['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg', 'face05.jpg',
         'face06.jpg', 'face07.jpg', 'face08.jpg', 'face09.jpg', 'face10.jpg']

fix_text = visual.TextStim(win, text = "+")

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
#-for loop for nBlocks
for block in range(nBlocks)
    #-present block start message
    block_text.draw()
    win.flip()
    event.waitKeys()
    #-randomize order of trials here
    np.random.shuffle(stims)
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials
    for trial in range(nTrials)
        #-set stimuli and stimulus properties for the current trial
        my_image = visual.ImageStim(win, units = "pix", size = (400, 400))
        #=====================
        #START TRIAL
        #=====================  
        #-draw fixation
        fix_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        
        #-draw image
        my_image.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        
        #-draw end trial text
        end_trial_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        
#======================
# END OF EXPERIMENT
#======================        
#-close window
win.close()
```
There are some things here we did not learn yet like wait time (stimulus duration). Because of this it is not completely working, I do have a script that
works that I'll put below, but without the start text, end text, and block start text. I think I will complete everything and have it all running together in the order at the end.
```
from psychopy import gui
from datetime import datetime
import os
from psychopy import visual, monitors, event
import numpy as np

#dictionary for dialog box gui
exp_info = {'subject_nr':(), 'age':(), 'handedness':('right','left','ambi'), 
            'gender':(), 'session': 1}

print(exp_info)

my_dlg = gui.DlgFromDict(dictionary=exp_info, title = "subject info", fixed = ['session'],
                         show = False)

print("All variables have been created! Now ready to show the dialog box!")

my_dlg = gui.DlgFromDict(dictionary=exp_info, title = "subject info", fixed = ['session'])

date = datetime.now()
exp_info['date'] = str(date.day) + "-" + str(date.month) + "-" + str(date.year)
print(exp_info['date'])

filename = str(exp_info['subject_nr']) + '_' + exp_info['date'] + '.csv'
print(filename)
main_dir = os.getcwd()
sub_dir = os.path.join(main_dir,'sub_info',filename)

mon = monitors.Monitor('myMonitor', width = 30.41, distance = 60)
mon.setSizePix([2500, 1600])
mon.save()

win = visual.Window(monitor=mon, 
                    color = ["burlywood"],
                    fullscr = True)
                    

main_dir = os.getcwd()
print(main_dir)
image_dir = os.path.join(main_dir, 'images')

stims = ['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg', 'face05.jpg',
         'face06.jpg', 'face07.jpg', 'face08.jpg', 'face09.jpg', 'face10.jpg']

x_axis = [-360, -360, 360, 360, -360, -360, 360, 360, -360, -360]
y_axis = [-225, 225, 225, -225, -225, 225, 225, -225, -225, 225,]
coords = list(zip(x_axis, y_axis))


nTrials = 10
fix_text = visual.TextStim(win, text = "+")
my_image = visual.ImageStim(win, units = "pix", size = (400, 400))

np.random.shuffle(stims)

for trial in range(nTrials):
    my_image.image = os.path.join(image_dir, stims[trial])
    my_image.pos = coords[trial]
    my_image.draw()
    fix_text.draw()
    win.flip()
    event.waitKeys()
win.close()

```
