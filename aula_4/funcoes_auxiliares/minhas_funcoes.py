def tri2(medidas):
    '''Calcular a área do triângulo'''
    return (medidas[0] * medidas[1])/2

def tra2(medidas):
    ''''Calcular a área do trapézio'''
    return ((medidas[0] + medidas[1]) * medidas[2])/2

def cir2(medidas):
    '''Calcular a área do círculo'''
    pi = 3.14159
    return pi * (medidas[0] ** 2)
