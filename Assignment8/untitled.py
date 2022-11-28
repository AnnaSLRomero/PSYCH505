from psychopy import core, event, visual, monitors
import numpy as np
import csv
import os
import json as json
import pandas as pd

filename = 'participantData_Nov28.csv'
main_dir = os.getcwd()
data_dir = os.path.join(main_dir,'exp','data',filename)

#monitor specs
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

#blocks, trials, stims, and clocks
nBlocks=2
nTrials=4
my_text=visual.TextStim(win)
rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

#prefill dictionary for responses
sub_resp = dict()
sub_acc = dict()
prob = dict()
corr_resp = dict()
resp_time = dict()


#create problems and solutions to show
math_problems = ['1+3=','1+1=','3-2=','4-1='] #write a list of simple arithmetic
solutions = [4,2,1,3] #write solutions
prob_sol = list(zip(math_problems,solutions))


#sub_resp = [[0]*nTrials]*nBlocks
#sub_acc = [[0]*nTrials]*nBlocks
#prob = [[0]*nTrials]*nBlocks
#corr_resp = [[0]*nTrials]*nBlocks
#resp_time = [[0]*nTrials]*nBlocks



for block in range(nBlocks):
    sub_resp[block] = [0]*nTrials
    sub_acc[block] = [0]*nTrials
    prob[block] = [0]*nTrials
    corr_resp[block] = [0]*nTrials
    resp_time[block] = [0]*nTrials
    for trial in range(nTrials):
        #what problem will be shown and what is the correct response?
        prob[block][trial] = prob_sol[np.random.choice(4)]
        corr_resp[block][trial] = prob[block][trial][1]
        
        rt_clock.reset()  # reset timing for every trial
        cd_timer.add(3) #add 3 seconds

        event.clearEvents(eventType='keyboard')  # reset keys for every trial
        
        count=-1 #for counting keys
        while cd_timer.getTime() > 0: #for 3 seconds

            my_text.text = prob[block][trial][0] #present the problem for that trial
            my_text.draw()
            win.flip()

            #collect keypresses after first flip
            keys = event.getKeys(keyList=['1','2','3','4','escape'])

            if keys:
                count=count+1 #count up the number of times a key is pressed

                if count == 0: #if this is the first time a key is pressed
                    #get RT for first response in that loop
                    resp_time[block][trial] = rt_clock.getTime()
                    #get key for only the first response in that loop
                    sub_resp[block][trial] = keys[0] #remove from list

        #record subject accuracy
        #correct- remembers keys are saved as strings
        if sub_resp[block][trial] == str(corr_resp[block][trial]):
            sub_acc[block][trial] = 1 #arbitrary number for accurate response
        #incorrect- remember keys are saved as strings              
        elif sub_resp[block][trial] != str(corr_resp[block][trial]):
            sub_acc[block][trial] = 2 #arbitrary number for inaccurate response 
                                    #(should be something other than 0 to distinguish 
                                    #from non-responses)
                    
        #print results
        print('problem=', prob[block][trial], 'correct response=', 
              corr_resp[block][trial], 'subject response=',sub_resp[block][trial], 
              'subject accuracy=',sub_acc[block][trial], 'response time=', resp_time[block][trial])

for block in range(nBlocks):
    data_as_dict = []
    for a,b,c,d,e in zip(prob[block], corr_resp[block], sub_resp[block], sub_acc[block], resp_time[block]):
        #the names listed here do not need to be the same as the variable names
        data_as_dict.append({'problem':a,'corr_resp':b,'sub_resp':c,'sub_acc':d, 'resp_time':e})
    print(data_as_dict)     
    
    with open(filename + '_block%i.txt'%block, 'w') as outfile:
        json.dump(data_as_dict, outfile)

win.close()


