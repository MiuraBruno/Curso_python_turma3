def tri(x):
    print('Área do triangulo')
    return (x[0] * x[1])/2
    
def tra(x):
    print('Área do trapézio')
    return ((x[0]+x[1])*x[2])/2
    
def c(x):
    print('Área do circulo')
    return 3.14159 * (x[0] ** 2)

def tudo(func,*valores):
    '''integra
    
    esse código serve para integrar outras funções'''
    print(func(valores))