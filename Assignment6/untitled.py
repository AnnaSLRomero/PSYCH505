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

