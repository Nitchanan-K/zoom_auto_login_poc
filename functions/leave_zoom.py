import pyautogui
import time

# import needed function 
from functions import click_location
from functions import move_to_location
from functions import find_location


def leave(leave_button,leave_meeting_button,location_name_1,location_name_2):
    
    # find the location of leave button
    leave_button_location = find_location.find_location_on_screen(leave_button,location_name_1)
    # move to the location
    move_to_location.move(leave_button_location)
    #click the location 
    click_location.click("Leave Button")
    time.sleep(2)
    
    # find the location of leave meeting button
    leave_meting_button_location = find_location.find_location_on_screen(leave_meeting_button,location_name_2)
    # move to the location
    move_to_location.move(leave_meting_button_location)
     #click the location 
    click_location.click("Leave Meeting Button")
    time.sleep(2)
    