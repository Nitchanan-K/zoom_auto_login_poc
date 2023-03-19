

# import function check for audio location
from functions import check_audio_location

def check_if_in_meeting():
    # looking for audio location
    # to confrim that we in zoom meeting if not than run process again by if else condition
    is_audio_location = check_audio_location.check_location()
    
    if is_audio_location is not None:
        return is_audio_location
    
    else:
        return None