import pyautogui


def write(data):
    
    if data is not None:
        # write on location 
        pyautogui.write(data)
        
        print("write on location successfully")
        
    else:
        print("please check your data type or file path")