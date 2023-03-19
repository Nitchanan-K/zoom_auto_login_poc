import pyautogui
import time

def click(location_name:str):
    # click on location
    pyautogui.click()
    
    print(f"Clicking on {location_name} location successfully")