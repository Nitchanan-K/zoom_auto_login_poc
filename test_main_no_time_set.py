import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime

# import main process
from main_process import run_process
# import function check for audio location
from functions import check_audio_location
from functions import click_location
from functions import connect_to_computer_audio
from functions import move_to_location
# import function check if in zoom meeting
from functions import is_in_meeting
# import function leave zoom meeting
from functions import leave_zoom


print("Running")

while True:
    df = pd.read_csv("data/info_2.csv")
    
    # set data if time in csv == current time 
    # than read data in csv file 
    # row = df.loc[df['timings'] == now]
    meeting_id = str(df.iloc[0,1])
    meeting_pw = str(df.iloc[0,2])
    print("Read data successfully")
        
    # Start process 
    run_process()

    # check if in zoom meeting by looking for connect audio button
    # if not than run process 
    # currently_in_meeting return positions x y of audio button 
    currently_in_meeting = is_in_meeting.check_if_in_meeting()
    
    if  currently_in_meeting is not None:
        
        print(f"Conect to Zoom Meeting successfully (Found Audio location) at {currently_in_meeting}")
        
        # move to audio location
        move_to_location.move(currently_in_meeting)
        time.sleep(2)
        # click connect to audio 
        click_location.click("Connect Audio button successfully")
        time.sleep(2)
        
        # find button to conect computer audio location
        # and click on connect to computer audio location
        connect_to_computer_audio.connect_audio()
        print("End process of connecting to Zoom Meeting")
        
        time.sleep(5)
        break
    else:
        print("Faild To Conect Zoom Meeting (No Audio location found)")
        # run process again in while loop
        continue
    
# if out of while loop start new while loop 
# cheking for time to
# read df file
df = pd.read_csv("data/info_2.csv") 
# import check time to leave zoom meeting
from check_time_to_leave import check_time
check_time(df)

    
        
        
       
   