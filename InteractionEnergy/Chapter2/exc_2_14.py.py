import sys
n=int(sys.argv[1])

power=1

if n>0:
    while power <=n:
        power *=2

        print(str(power))
