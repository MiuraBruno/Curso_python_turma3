import os
from time import sleep
def board(m):
    for i in range(3):
        if i != 0:
            print('-'*13)
        print('  '+ ' | '.join(m[i]))
        

def jogada(m,n,jogador):
    if n > 9 or n < 1:
        print('Jogada incorreta tente de novo')
        return 1
    if n > 6:
        if m[0][n%7].isdigit() == True:
            m[0][n%7] = jogador
            return 0
        else:
            print('Jogada incorreta tente de novo')
            return 1
    elif n > 3:
        if m[1][n%4].isdigit() == True:
            m[1][n%4] = jogador
            return 0
        else:
            print('Jogada incorreta tente de novo')
            return 1
    else:
        if m[2][(n%4)-1].isdigit() == True:
            m[2][(n%4)-1] = jogador
            return 0
        else:
            print('Jogada incorreta tente de novo')
            return 1
        
def check_resultado(m):
    from re import findall
    if  m[0][0]+ m[0][1] + m[0][2] == 'XXX' or m[0][0]+ m[0][1] + m[0][2] == 'OOO':
        return 0
    elif  m[1][0]+ m[1][1] + m[1][2] == 'XXX' or m[1][0]+ m[1][1] + m[1][2] == 'OOO':
        return 0
    elif   m[2][0]+ m[2][1] + m[2][2] == 'XXX' or m[2][0]+ m[2][1] + m[2][2] == 'OOO':
        return 0
    elif m[0][0] + m[1][0] + m[2][0] == 'XXX' or m[0][0] + m[1][0] + m[2][0] == 'OOO' :
        return 0
    elif m[0][1] + m[1][1] + m[2][1] == 'XXX' or m[0][1] + m[1][1] + m[2][1] == 'OOO' :
        return 0
    elif m[0][2] + m[1][2] + m[2][2] == 'XXX' or m[0][2] + m[1][2] + m[2][2] == 'OOO' :
        return 0
    elif m[0][0] + m[1][1] + m[2][2] == 'XXX' or m[0][0] + m[1][1] + m[2][2] == 'OOO':
        return 0
    elif m[0][2] + m[1][1] + m[2][0] == 'XXX' or m[0][2] + m[1][1] + m[2][0] == 'OOO':
        return 0
    else:
        n = "".join(m[0])+ "".join(m[1])+ "".join(m[2])
        if findall(r'\d+',n) == []:
            return 1
    return 2
    
def vencer_perder(m,jogador):
    jogada = 0
    possiveis_jogadores = ['X','O']
    linhas = ["".join(m[0]),"".join(m[1]),"".join(m[2])]
    colunas = [m[0][0] + m[1][0] + m[2][0],m[0][1] + m[1][1] + m[2][1],m[0][2] + m[1][2] + m[2][2]]
    diagonal = [m[0][0] + m[1][1] + m[2][2], m[2][0] + m[1][1] + m[0][2]]
    
    #posso ganhar na linha?
    for i in linhas:
        if i.count(jogador) == 2 and i.replace(jogador,'').isdigit():
            jogada = i.replace(jogador,'')
            break
    
    
    #posso ganhar na colunas?
    for i in colunas:
        if i.count(jogador) == 2 and i.replace(jogador,'').isdigit():
            jogada = i.replace(jogador,'')
            break
    
        
    #posso ganhar na diagonal?
    for i in diagonal:
        if i.count(jogador) == 2 and i.replace(jogador,'').isdigit():
            jogada = i.replace(jogador,'')
            break

            
    return int(jogada)
        
    
def ia(jogadas_disponiveis):
    from random import randint
    return jogadas_disponiveis[randint(0,len(jogadas_disponiveis)-1)]
    
    
    
def cal_rodada(m):
    jogadas = []
    for celula in m:
        if celula != ['X'] and celula != ['O']:
            jogadas.append(m.index(celula))
    return jogadas
            
    
    


        
def main(comp,humano,aux):
    if aux%2 == 0:
        cpu = 'X'
    else:
        cpu = 'O'
    print("comecem os jogos!\n\n")
    board(m)
    i = 0
    while check_resultado(m) == 2:
        print('\n\n escolha um numero para a jogadas')
        if i%2 == 0:
            jogador = 'X'
            print('Vez do "X"')
        else:
            jogador = 'O'
            print('Vez do "O"')
        flag = 1
        
        while flag == 1:
            if jogador == 'X':
                if cpu == 'X':
                    posicao = vencer_perder(m,jogador)
                    if posicao != 0:
                        flag = jogada(m,posicao,jogador)
                    else:
                        posicao = vencer_perder(m,'O')
                        if posicao != 0:
                            flag = jogada(m,posicao,jogador)
                        else:
                            posicao = ia(jogadas_disponiveis)
                            flag = jogada(m,posicao,jogador)
                else:
                    posicao = input()
                    flag = jogada(m,posicao,jogador)
            else:
                if cpu == 'O':
                    posicao = vencer_perder(m,jogador)
                    if posicao != 0:
                        flag = jogada(m,posicao,jogador)
                    else:
                        posicao = vencer_perder(m,'X')
                        if posicao != 0:
                            flag = jogada(m,posicao,jogador)
                        else:
                            posicao = ia(jogadas_disponiveis)
                            flag = jogada(m,posicao,jogador)
                else:
                    posicao = input()
                    flag = jogada(m,posicao,jogador)
        os.system('cls')
        board(m)
        sleep(1)
        del jogadas_disponiveis[jogadas_disponiveis.index(posicao)]
        i = i + 1
    if check_resultado(m) == 1:
        print('Empate')
    else:
        if jogador != cpu:
            print('Voce venceu!')
            humano = humano + 1
        else:
            print('Voce perdeu!')
            comp = comp + 1
    return comp,humano

        

comp = 0
humano = 0
aux = 0
while True:
    m = [['7','8','9'],
     ['4','5','6'],
     ['1','2','3']
    ]
    jogadas_disponiveis = range(10)[1:]
    x = raw_input('Deseja jogar?(y/n)\n')
    if __name__ == '__main__' and x == 'y':
        comp,humano = main(comp,humano,aux)
        sleep(1)
        os.system('cls')
        aux = aux + 1
        print('\n')
        print('PLACAR')
        print('comp %d vs Humano %d' %(comp,humano))
        
        print('\n\n\n')
    else:
        break