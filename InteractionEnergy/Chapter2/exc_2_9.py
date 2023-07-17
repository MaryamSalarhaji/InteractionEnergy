import math
power=0
for i in range(1,8):
    power += 1
    n=2**power
    print(str(math.log(n, 10))+ '\t'+ str(n)+ '\t'+ str(n*math.log(n, 10))+'\t'+ str(math.pow(n, 2))+'\t'+ str(math.pow(n, 3)))
    
