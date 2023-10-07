import time

def countdown(number):
    x = number
    while x > 0:
        print (f'{x} SECOND(S)!')
        x -= 1
    if x == 0:
        print("HAPPY NEW YEAR!" )

    

countdown(10)

def countdown_with_sleep(number):
    x = number
    while x > 0:
        print (f'{x} SECOND(S)!')
        time.sleep(1)
        x -= 1
    if x == 0:
        print("HAPPY NEW YEAR!" )
    
