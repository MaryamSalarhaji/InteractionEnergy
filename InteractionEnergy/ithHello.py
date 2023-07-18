#print ith hello according to the reminder

for i in range(1, 1000):
    if i%10==1 or i%100==1:
        print(str(i)+'st Hello')
    elif i%10==2 or i%100==2:
        print(str(i)+'nd Hello')
    elif i%10==3 or i%100==3:
        print(str(i)+'rd Hello')
    else:
        print(str(i)+'th Hello')
    
    

          

