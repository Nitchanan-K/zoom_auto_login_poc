import pyautogui


def find_location_on_screen(template,location_name):
    
    if template is not None:
    
        # template is the picture for function to find location
        # base on that specific image
        
        location = pyautogui.locateCenterOnScreen(template)
        
        # move to location found
        pyautogui.moveTo(location)
        print(f"Move to {location_name} location successfully")
        
        return location
    else:
        print("Template not found please try correct path to file")
    