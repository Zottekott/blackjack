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
    
    random.randomint(