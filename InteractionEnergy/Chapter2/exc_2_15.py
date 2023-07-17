import sys

# Accept integer command-line argument n. Write to standard output
# an n-by-n table with an asterisk in row i and column j if either
# i divides j or j divides i.

#n=int(sys.argv[1])

i=1
j=1

while i<=2:
    # Write the ith line.
    
    while j<=2:
       
        if (i%j==0) or (j%i==0):
            print('*')
        else:
            print(' ')
            i +=1
            j +=1
    
    print(i)        
   
