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

print("Running")
# set up data to write and read by pyautogui

#row = df.loc[df['timings']]


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

    # looking for audio location
    # to confrim that we in zoom meeting if not than run process again by if else condition
    is_audio_location = check_audio_location.check_location()
    
    if is_audio_location is not None:
        print(f"Conect to Zoom Meeting successfully (Found Audio location) at {is_audio_location}")
        
        # move to audio location
        move_to_location.move(is_audio_location)
        time.sleep(2)
        # click connect to audio 
        click_location.click("Connect Audio button successfully")
        time.sleep(2)
        
        # find conect to computer audio location
        # and click on connect to computer audio location
        connect_to_computer_audio.connect_audio()
        print("End process of connecting to Zoom Meeting")
        break
    
    else:
        print("Faild To Conect Zoom Meeting (No Audio location found)")
        # run process again in while loop
        continue