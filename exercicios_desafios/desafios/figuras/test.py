def tri_eq(c,linha):
    metade = (linha // 2)
    padrao = (' ' * metade) + c
    for i in range(linha):
        print((' ' * metade) + padrao)
        metade = metade - 1
        padrao = padrao + ' ' + c + ' ' + c
        
        
        
from time import sleep
for i in range(1,10):    
    tri_eq('*', i)
    sleep(1)