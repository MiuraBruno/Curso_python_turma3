def tri_eq(c,n):
    space = ' '* (n-1)
    dig = 1
    for i in range(n):
        print(space + '*' * dig )
        space = space[:-1]
        dig = dig + 2
        
        
        
from time import sleep
for i in range(1,10):    
    tri_eq('*', i)
    sleep(1)
