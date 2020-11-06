import pandas as pd
import random
from time import sleep

def escolhe_quantidade():
    quantidade_itens = [1] * 40 + [2] * 30 + [3] * 20 + [4] * 10
    random.shuffle(quantidade_itens)
    return quantidade_itens[random.randint(0,len(quantidade_itens) - 1)]

#escolhe um elemento aleatório de um dataframe
def escolhe_opcao(df):
    maximo = len(df) - 1
    valor = random.randint(0,maximo)
    return df.iloc[valor]
    
#gera um pedido aleatório
def gera_pedido(df):
    pedido = {}
    quantidade = escolhe_quantidade()
    pedido['quantidade'] =  quantidade
    produto = int(escolhe_opcao(df))
    pedido['produto'] = produto
    return pedido