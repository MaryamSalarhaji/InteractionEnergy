import random

while True:
    x= -1.0+2* random.random()
    y=-1.0+2* random.random()
    if x*x+y*y<=1.0:
        break

print("hit")
