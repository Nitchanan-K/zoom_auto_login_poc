# import function check for audio location
from functions import check_audio_location

def check_if_in_meeting():
    # looking for audio location to confrim that we in zoom meeting 
    # if not Ture run main process again by if else condition
    # check_if_in_meeting return None in case audio location is not found 
    # None will be checked in main while loop to make sure we are not in zoommeeting 
    # and run main process that try to login again
    
    is_audio_location = check_audio_location.check_location()
    
    if is_audio_location is not None:
        return is_audio_location
    
    else:
        return None