def titulo(inf = ['','',''],inf2 = ['dd/mm/yyyy','V 1.0']):
    altura = 8
    largura = 80
    dados =  ["Autor(es): ","Título: ","Descrição: "]
    dados2 = ["Data de criação: ","Versão: "]
    
    for i in range(5):
        if i == 0:
            linha = "╔" + "═"*(largura - 2) + "╗"
        else:
            if i <= len(dados):
                linha = "║" + dados[i-1] + inf[i-1] + " "*(largura - 2 - len(dados[i-1]) - len(inf[i-1])) + "║"
            else:
                linha = "║" + " "*(largura - 2) + "║"
        print(linha)
    for i in range(3):
        if i == 0:
            linha = "╠" +  "═"*(largura - 2) + "╣"
        else:
            if i <= len(dados):
                linha = "║" + dados2[i-1] + inf2[i-1] + " "*(largura - 2 - len(dados2[i-1]) - len(inf2[i-1])) + "║"
        print(linha)
    linha = "╚" + "═"*(largura - 2)+ "╝"
    print(linha)





titulo(['Bruno Miura','teste de cabeçalho só funciona em python 3','Apenas um exemplo de cabeçalho, o código pode ser melhorado'],['10/10/2019','1'])
    
