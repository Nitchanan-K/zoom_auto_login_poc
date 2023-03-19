import subprocess
import pyautogui
import time
from datetime import datetime

# import functions 
from functions import open_zoom
from functions import find_location
from functions import click_location
from functions import type_on_location
from functions import find_multiple_locations

def connect_audio():
    
    # find join computer audio button
    find_location.find_location_on_screen("assets\images\join_with_computer_audio.png","Join Computer Audio Button")
    # click on join computer audio button
    click_location.click("Join Computer Audio Button")
    time.sleep(2)