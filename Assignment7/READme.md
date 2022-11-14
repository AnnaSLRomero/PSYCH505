# Level 5: Clocks and Timing
## Wait Exercises
1)
```
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

```

## Clock Exercises
1)
```
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

for trial in range(nTrials): #loop through trials
    
    my_image.image = os.path.join(image_dir,stims[trial])
    
    fix_text.draw()
    win.flip()
    core.wait(.5)
    
    my_image.draw() #draw
    win.flip() #show
    imgStartTime = wait_timer.getTime()
    core.wait(1) #wait .5 seconds, then:
    imgEndTime = wait_timer.getTime()
    
    fix_text.draw()
    win.flip()
    core.wait(.5)
    
    print("Image duration was {} seconds". format(imgEndTime - imgStartTime))
    
    
win.close() #close the window after trials have looped  
```
Image duration was 1.001098415999877 seconds....

2)
3)
4)

## Frame-based Timing Exercises
1)
2)
