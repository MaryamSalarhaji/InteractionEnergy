import sys
n=int(sys.argv[1])
#Reverse using arithmetic
m=0
while n!=0:
    m=(10*m)+(n%10)
    n//=10

print(m)
print(n)
s=' '
while m!=0:
     digit = m%10
     s += str(digit)
     m //=10
print(s)     
