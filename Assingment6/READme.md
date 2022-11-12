# Assignment 6
```
from psychopy import gui
from datetime import datetime
import os
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
