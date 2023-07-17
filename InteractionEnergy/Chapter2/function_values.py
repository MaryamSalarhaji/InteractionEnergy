import sys
import math
n=int(sys.argv[1])

for i in range(1, n+1):
    print(str(i)+ ' '+ str(2*math.pi*i/n))
