import random
import time
while True:
    try:
        geld=abs(int(input('Wat is uw kapitaal? ')
        break
    except:
        print('U moet een geheel getal ingeven')
        time.sleep(2)
while geld<0:
    while True:
        try:
            inzet=abs(int(input('Hoeveel zet je in? ')
            break
        except:
            print('U moet een geheel getal ingeven')
            time.sleep(2)
    
    if inzet>geld:
        inzet=geld
        print('U gaat all-in met',inzet)
    
    random.randomchoice((2,3,4,5,6,7,8,9,10,J,Q,K,A))
