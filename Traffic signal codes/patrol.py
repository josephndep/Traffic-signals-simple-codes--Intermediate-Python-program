# This code is for automating traffic lights with blue traffic signals added
# I think this is very cool particulary when we have the ordinary Green, orange and red lights
# with blue added can improve traffic signals on the street
import time
from datetime import datetime
from time import sleep


now = datetime.now()
current_time = now.strftime("%H:%M:%S") # Time is of esssence that is why current_time is included
# Define a function convoy
def traffic():
    while True:
        for X in range(10000):
             print("Green....", current_time)  # GREEN Traffic lights with timer below 
             time.sleep(5)                                 #
             
             print("Orange....")                                      # With the orange light
             print("Possible convoy or Ambulance", current_time)      # Decisions of leaving space for convoys
             print('Press tap Ctrl+C for Emergency: ')                 # or Ambulance can be decided
             try:
                  for i in range(0,5):
                     sleep(3)
                     print("No Interruptions...")
             except KeyboardInterrupt:
                 print("OK Blue Traffic lights Activated")           # BLUE Activated
                 print("Blue....")
                 print("Space for Emergency")
                 time.sleep(7)                                        
                 
             print("Red okay stop", current_time)         # Red Traffic lights with Timer below
             time.sleep(5)
            
                                 
traffic()     # recall the function