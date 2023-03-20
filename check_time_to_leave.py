import pyautogui
import pandas as pd
from datetime import datetime

# import function leave zoom meeting
from functions import leave_zoom

# function work flow
# 1. get current time
# 2. check if curent time is equal to time that we set in csv file to logout
# 3. check if , if condition is true leave zoom meeting with leave_zoom.leave function 
# 4. break out of loop 
# 5. else continue the while loop and keep checking for time to leave zoom 

def check_time_and_leave(df):
    
    # checking of the current time exists in our csv file 
    while True:
        # get current time
        now = datetime.now().strftime("%H:%M")
        
        if now == str(df.iloc[1,0]):
            print(f"time to leave Zoom meeting: {str(df.iloc[1,0])}")
            
            # leave zoom meeting
            leave_zoom.leave("assets\images\leave_button.png",
                            "assets\images\leave_meeting_button.png",
                            "Leave Button",
                            "Leave Meeting Button")
            
            # break out of while loop
            break
            
        else:
            # continue to check the current time to leave zoom
            continue
        
        