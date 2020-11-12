def media_matriz(m):
    divisao = len(m)
    elementos = len(m[0])
    soma = [0]*elementos
    for indice,linha in enumerate(m):
        for indice_2,valor in enumerate(linha):
            soma[indice_2] = soma[indice_2] + valor
    resposta = list(map(lambda x: x/divisao,soma))
    return resposta
def print_name():
    return __name__
    
if __name__ == '__main__':    
    print('Hello World!')