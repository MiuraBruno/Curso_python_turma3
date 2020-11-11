#como executar esse script
#py C:\Users\Bruno.Miura\Desktop\CURSO\3_turma\Curso_python_turma3\aula_6\lendo_arquivos.py < C:\Users\Bruno.Miura\Desktop\CURSO\3_turma\Curso_python_turma3\aula_6\dados.txt

def sorteia():
'''
    By Carlão
'''
    from random import shuffle
    prob = list(range(1,61))
    shuffle(prob)
    jogo = prob[:6]
    resp = "-".join(map(lambda x: str(x), sorted(jogo)))
    return resp
    

while True:
    try:
        #código principal
        linha = input()
        mensagem = linha + ' tente a sorte e jogue os números: ' + sorteia() + ' em sua proxima tentativa :D'
        print(mensagem)
    except EOFError:
        #pos leitura
        print('Fim de todos os testes!')
        print('Boa sorte')
        break