#you need to take numbers
import sys
#head or tail so need random library
import random
stake=int(sys.argv[1])
goals=int(sys.argv[2])
trials=int(sys.argv[3])
#calculate wins and bets so start from zero 
wins=0
bets=0
for t in range(trials):
    cash=stake
    while 0<cash<goals:
        bets +=1
        if random.randrange(0,2)==0:
            cash +=1
        else:
            cash -=1
    if cash== goals:
        wins +=1

print("win is:", str(100*wins//trials))
print("avg bets is:", str(bets//trials))
        
              
                

