import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime

# improt main process
from main_process import run_process

print("Running")
# set up data to write and read by pyautogui

#row = df.loc[df['timings']]


while True:
    df = pd.read_csv("data/info_2.csv")
    # checking of the current time exists in our csv file 
    now = datetime.now().strftime("%H:%M")
    #print(f"Current time:{now}")
    
    if now in str(df['timings']):
        print("current time == set time: Run Start!!")
        
        # set data if time in csv == current time 
        # than read data in csv file 
        row = df.loc[df['timings'] == now]
        meeting_id = str(row.iloc[0,1])
        meeting_pw = str(row.iloc[0,2])
        print("Read data successfully")
        
        # Start process 
        run_process()
