import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime

# import functions 
from functions import open_zoom
from functions import find_location
from functions import click_location
from functions import type_on_location
from functions import find_multiple_locations


# set up data to write and read by pyautogui
df = pd.read_csv("data/info_2.csv")
#row = df.loc[df['timings']]
meeting_id = str(df.iloc[0,1])
meeting_pw = str(df.iloc[0,2])
print(str(df.iloc[0,1]))
print(str(df.iloc[0,2]))


      
def run_process():
    
    # open zoom
    open_zoom.open()
    
    # move to join zoom meeting button
    find_location.find_location_on_screen("assets/images/join_button.png","Join button")
    time.sleep(2)
    
    # click on join button
    click_location.click("join zoom meeting button")
    time.sleep(2)
    
    # type meeting id 
    type_on_location.write(meeting_id)
    time.sleep(2)
    
    # find all checkboxes locations to turn off camera and mic
    locations = find_multiple_locations.find_all_locations_on_screen("assets\images\media_check_box.png")
    # use for loop to assess each location individually
    for location in locations:
        # move to each location
        pyautogui.moveTo(location) 
        print(f"move to {location} successfully")
        # click on each location
        click_location.click(f"click on {location} successfully")
        time.sleep(2)
    
    # find join zoom room location
    find_location.find_location_on_screen("assets\images\join_button2.png","Join Room Button")
    time.sleep(2)
    # click on join room button location
    click_location.click("Join Room Button")
    time.sleep(3)
    
    # find password input location    
    find_location.find_location_on_screen("assets\images\meeting_pswd.png", "Meeting Password input")
    time.sleep(2)
    
    # type meeting password
    type_on_location.write(meeting_pw)
    time.sleep(2)
    
    # find join meeting button location
    find_location.find_location_on_screen("assets\images\join_meeting_button.png", "Join Meeeting button")
    time.sleep(1) 
    # click on join meeting button
    click_location.click("Join Meeeting Button")
    time.sleep(30) 
    
    
    
    
