from psychopy import visual, monitors, event, core

#define the monitor parameters
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1600,900])
win = visual.Window(monitor=mon) #define a window

import os
#stuff you only have to define once at the top of your script
main_dir = os.getcwd() 
image_dir = os.path.join(main_dir,'images')

my_image = visual.ImageStim(win)

stims = ['face01.jpg','face02.jpg','face03.jpg'] #create a list if images to show
nTrials=3 #create a number of trials for your images

end_trial_msg = "End of trial"
end_trial_text = visual.TextStim(win, text = end_trial_msg)
fix_text = visual.TextStim(win, text = "+")

wait_timer = core.Clock()
stimTimer = core.Clock()

for trial in range(nTrials): #loop through trials
    
    my_image.image = os.path.join(image_dir,stims[trial])
    
    stimTimer.reset()
    
    while stimTimer.getTime() <= 1:
        fix_text.draw()
        win.flip()
    
    imgStartTime = wait_timer.getTime()
    while 1 < stimTimer.getTime() <=2: 
        my_image.draw() #draw
        win.flip() #show
    imgEndTime = wait_timer.getTime()
    
    fix_text.draw()
    win.flip()
    
    print("Image duration was {} seconds". format(imgEndTime - imgStartTime))
    
    
win.close() #close the window after trials have looped    


