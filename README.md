## Bot login and logout zoom on time in csv file

## General info

This bot using PyAutoGUi to find position that needed to click and write info that needed
and stored data in csv file and read with pandas dataframe by setting time for login and logout 
we can use while loop to check if current time equal set time than execute the tasks that we set.
### To run this project, install requirement:
* PyAutoGUI => 0.9.53 
* pandas => 1.5.3

## Process Flow 

##### 1. set up dataframe to read time that we set use in login and logout process
##### 2. check current time if equal login time then start the main process 
##### 3. main process try to login to zoom meeting
##### 4. after main process run code will check if we in zoom meeting or not
##### 5. by checking if audio button location is found or not 
##### 6. if not found run main process again (try to loging again) if found break out of main while loop
##### 7. if in meeting , enter new while loop and code will keep checking time for leaving zoom
##### 8. if current time equal leaving time in csv file, code will run leave_zoom.leave function and leave zoom

## Setup
To run this project, install it locally using npm:

```
$ pip install pandas
$ pip install PyAutoGUI
```

## Sources
This bot is inspired by Anish Malla
bot tutorial by [@Anish-Malla](https://github.com/Anish-Malla/Zoom-Automation-Python)

## Important Note 
Result will be vary depend on zoom version user interface please change picture to locate positions accordingly
