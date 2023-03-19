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

def check_location():
    
    # find join audio button
    audio_location = pyautogui.locateCenterOnScreen("assets\images\join_audio.png") 
    return audio_location
    