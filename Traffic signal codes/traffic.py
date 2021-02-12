import time
import random
from random import choice
# Green = 2
# Orange = 0
# Red = 1
def traffic_colors():
    color = [1, 2] 
    print('Orange[0]...')
    X = (choice(color))
    print(X)
    if X == 1:
        print("Red!..")
        time.sleep(3.5)
        print("Hey! Hold on")
    elif X == 2:
        print("Green!...Move on")

        
        
traffic_colors()

               # for n in range(n, -1, -1):
                   #  print(n, end= '', flush=True)
                     # print(c, flush=True)
                    # time.sleep(5)
                    # pass 