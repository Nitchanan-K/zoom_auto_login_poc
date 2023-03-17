import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime


def sign_in():
    # Open up zoom app
    # on Windows use below code for opening zoom 
    # find youe zoom app launcher and copy path use / / / / as path space
    subprocess.call("C:/Program Files/Zoom/bin/Zoom.exe")
    
    # If on mac / Linux use below line for opening zoom 
    # subprocess.call(["/usr/bin/open", "/Applications/zoom.us.app"])

    # sleep for 5 seconds
    time.sleep(5)

def join_meeting(meeting_id,pswd):
    
    # clicks the join meeting button
    join_meeting_button = pyautogui.locateCenterOnScreen("join_button.png")
    pyautogui.moveTo(join_meeting_button)
    pyautogui.click()
    time.sleep(5)
    
    # Type the Meeting ID
    meeting_id_input = pyautogui.locateCenterOnScreen("meeting_id_input.png")
    pyautogui.moveTo(meeting_id_input)
    pyautogui.click()
    pyautogui.write(meeting_id)
    print("typed meeting id")
    time.sleep(5)
    
    # Disables both the camera and th mic 
    media_check_box = pyautogui.locateAllOnScreen("media_check_box.png")
    for checkbox in media_check_box:
        pyautogui.moveTo(checkbox)
        pyautogui.click()
        time.sleep(5)
  
    # Hits the join button
    join_button = pyautogui.locateCenterOnScreen("join_button2.png")
    pyautogui.moveTo(join_button)
    pyautogui.click()
    print("hits the join button")
    
    time.sleep(5)
    # Types the password and hits enter 
    meeting_pswd_input = pyautogui.locateCenterOnScreen("meeting_pswd.png")
    pyautogui.moveTo(meeting_pswd_input)
    # pyautogui.click()
    # time.sleep(2)
    # pyautogui.click()
    pyautogui.write(pswd)
    print("typed password")
    pyautogui.press('enter')          
   

    
# reading the csv file (date time and id password for meeting)

df = pd.read_csv('info_2.csv')

print(df)

# run 
while True:

    # checking of the current time exists in our csv file 
    now = datetime.now().strftime("%H:%M")
    
    if now in str(df['timings']):
        print("test")
        
        row = df.loc[df['timings'] == now]
        m_id = str(row.iloc[0,1])
        m_pswd = str(row.iloc[0,2])
       
        sign_in()
        join_meeting(meeting_id = m_id, 
                     pswd = m_pswd)
        time.sleep(2)
        print("signed in")
        
# write function to check if sometings show then break from loops
# write function to check if break room trhen join