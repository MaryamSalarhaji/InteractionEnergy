import sys
import math
#inser coefficient of a, c, and c
a=float(sys.argv[1])
b=float(sys.argv[2])
c=float(sys.argv[3])

#calculate delta
discriminate=b**2-4*a*c

#check division by zero and not negative delta
if discriminate<0:
    print('Negative discriminate')
elif a==0:
    print('No division by zero')
else:
    d=math.sqrt(discriminate)
    print('root one is:',(-b+d)/(2*a))
    print('root two is:', (-b-d)/(2*a))

