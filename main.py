import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime

# import main process 
from main_process import run_process
# import needed function 
from functions import check_audio_location
from functions import click_location
from functions import connect_to_computer_audio
from functions import move_to_location
# import function check if in zoom meeting 
from functions import is_in_meeting


## Before run
# 1. change type language to English
# 2. close program Zoom
# 3. set start time and leave time 
print("Running")

# process flow 
# 1. set up dataframe to read time that we set use in login and logout process
# 2. check current time if equal login time then start the main process 
# 3. main process try to login to zoom meeting
# 4. after main process run code will check if we in zoom meeting or not
# 5. by checking if audio button location is found or not 
# 6. if not found run main process again (try to loging again) if found break out of main while loop
# 7. if in meeting , enter new while loop and code will keep checking time for leaving zoom
# 8. if current time equal leaving time in csv file, code will run leave_zoom.leave function and leave zoom    

while True:
    # set up datafarme
    df = pd.read_csv("data/info_2.csv")
    
    # checking of the current time exists in our csv file 
    now = datetime.now().strftime("%H:%M")
    
    if now in str((df['timings'])):
        print("current time == set time: Run Start!!")
        
        # set data if time in csv == current time 
        # than read data in csv file 
        row = df.loc[df['timings'] == now]
        meeting_id = str(row.iloc[0,1])
        meeting_pw = str(row.iloc[0,2])
        print("Read data successfully")
        
        # Start process 
        run_process()
        
        # check if in zoom meeting by looking for connect audio button
        # if not than run process again 
        # currently_in_meeting return positions x y of audio button 
        currently_in_meeting = is_in_meeting.check_if_in_meeting()
    
        if  currently_in_meeting is not None:
            print(f"Conect to Zoom Meeting successfully (Found Audio location) at {currently_in_meeting}")
        
            # move to audio button location
            move_to_location.move(currently_in_meeting)
            time.sleep(2)
            # click connect to audio button 
            click_location.click("Connect Audio button successfully")
            time.sleep(2)
                
            # find button to conect computer audio location
            # and click on connect to computer audio location
            connect_to_computer_audio.connect_audio()
            print("End process of connecting to Zoom Meeting")
                
            time.sleep(5)
            
            # connect success will break out of while loop
            break
        
        else:
            print("Faild To Conect Zoom Meeting (No Audio location found)")
            
            # run process again in while loop
            continue


# if out of while loop start new while loop with check_time_and_leave function
# cheking for time to logout
# set up data frame
df = pd.read_csv("data/info_2.csv") 

# import check time to leave zoom meeting
from check_time_to_leave import check_time_and_leave
check_time_and_leave(df)
