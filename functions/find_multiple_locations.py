import pyautogui


def find_all_locations_on_screen(template:str):
    
    # check for all possible locations base on template
    locations = pyautogui.locateAllOnScreen(template)
    
    # return objects and can use forloop to assess each x,y location individually
    return locations
    

