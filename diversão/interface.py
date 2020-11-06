from Tkinter import *
import sys
from PIL import ImageTk, Image
def randcor():
    from random import randint
    v = ['4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd']
    cor = '#'
    for i in range(6):
        cor = cor + v[randint(0,len(v)-1)]
    return cor

numero_jogos = [0]
m = [['7','8','9'],
     ['4','5','6'],
     ['1','2','3']
    ]
v = [-1]
flags_click = [1]*9
score_player_1 = [0]

score_player_2 = [0]
controle_player = [-1]
cor = randcor()

class Janelinha:
    def __init__(self, q,result,jogador):
        self.result = result
        self.jogador = jogador
        vencedor = ''
        if jogador == -1:
            
            if controle_player[-1] % 2 == 0:
                vencedor = "O jogador 1 inicia"
            else:
                vencedor = "O jogador 2 inicia"
            self.msg=Label(q,width=96,height=6,text = vencedor)
        else:
            if (jogador) % 2 == 0:
                vencedor = "O jogador com X venceu!"
            else:
                vencedor = "O jogador com O venceu!"
            if self.result == 0:
                self.msg=Label(q,width=96,height=6,text = vencedor)
            else:
                self.msg=Label(q,width=96,height=6,text = 'Empatou')
        self.msg.focus_force()
        self.msg.pack()

        self.close = Button(q, text='Fechar', command=q.destroy )
        self.close.pack()



class Janela:
    def __init__(self,instancia_Tk):
        
        #define os containers para criacao das casa do jogo
        
        #define container para canvas
        self.container1 = Frame(instancia_Tk)
        self.container2 = Frame(instancia_Tk)
        self.container3 = Frame(instancia_Tk)
        
        #define container para botoes
        self.container4 = Frame(instancia_Tk)
        
        #define container para placar
        self.container5 = Frame(instancia_Tk)
        
        #define container para imagem
        self.container6 = Frame(instancia_Tk)

        #cria container para botoes e placar
        self.container4.pack()
        self.container5.pack()
        
        
        
        
        #cria botoes
        #para new game 
        self.new_game = Button(self.container4, text='New Game')
        self.new_game.bind("<Button-1>", self.start_game)
        self.new_game.pack(side = LEFT)

        #para sair do jogo
        self.close = Button(self.container4, text = 'Exit', command = instancia_Tk.destroy)
        self.close.pack(side = RIGHT)
        
        #cria placar
        self.score_board = Label(self.container5,
                        width=48,
                        height=6,
                        text = "PLACAR\n\n\nJOGADOR 1  "\
                        + " Vs.   "\
                        + "JOGADOR 2 \n\n"\
                        + str(score_player_1[-1])\
                        + "\t"\
                        + str(score_player_2[-1]),
                        background = "white",
                        font = "Verdana" )
        self.score_board.pack()
        
        #cria container para canvas
        self.container1.pack()
        self.container2.pack()
        self.container3.pack()
        
        #cria container e coloca a imagem 
        self.container6.pack()
        self.img = ImageTk.PhotoImage(Image.open("keyrus.jpg"))
        self.imglabel = Label(self.container6, image=self.img).grid(row=1, column=1)

        

    def cria_tabuleiro(self):
        cor = randcor()
        controle_player[-1] = controle_player[-1] + 1

        root2 = Tk()
        root2.geometry("200x150+600+300") #tela(comp x larg)+posicaoA+posicaoB
        root2.grab_set() #trava a janela ao ser exibida
        Janelinha(root2,0,-1)
        
        
        self.score_board.destroy()
        
        self.score_board = Label(self.container5,
                        width=48,
                        height=6,
                        text = "PLACAR\n\n\nJOGADOR 1  "\
                        + " Vs.   "\
                        + "JOGADOR 2 \n\n"\
                        + str(score_player_1[-1])\
                        + "\t"\
                        + str(score_player_2[-1]),
                        background = "white",
                        font = "Verdana" )
        self.score_board.pack()
       
        
        self.canvas1 = Canvas(self.container1, width = 150, height = 150, bd = 5,bg = cor)
        self.canvas1.bind("<Button-1>",self.x1)
        self.canvas1['cursor']='X_cursor'
        self.canvas1.pack(side=LEFT)
        

        self.canvas2 = Canvas(self.container1, width = 150, height = 150, bd = 5,bg = cor)
        self.canvas2.bind("<Button-1>",self.x2)
        self.canvas2['cursor']='X_cursor'
        self.canvas2.pack(side=LEFT)


        self.canvas3 = Canvas(self.container1, width = 150, height = 150, bd = 5,bg = cor)
        self.canvas3.bind("<Button-1>",self.x3)
        self.canvas3['cursor']='X_cursor'
        self.canvas3.pack(side=LEFT)

        self.canvas4 = Canvas(self.container2, width = 150, height = 150, bd = 5,bg = cor)
        self.canvas4.bind("<Button-1>",self.x4)
        self.canvas4['cursor']='X_cursor'
        self.canvas4.pack(side=LEFT)

        self.canvas5 = Canvas(self.container2, width = 150, height = 150, bd = 5,bg = cor)
        self.canvas5.bind("<Button-1>",self.x5)
        self.canvas5['cursor']='X_cursor'
        self.canvas5.pack(side=LEFT)


        self.canvas6 = Canvas(self.container2, width = 150, height = 150, bd = 5,bg = cor)
        self.canvas6.bind("<Button-1>",self.x6)
        self.canvas6['cursor']='X_cursor'
        self.canvas6.pack(side=LEFT)

        self.canvas7 = Canvas(self.container3, width = 150, height = 150, bd = 5,bg = cor)
        self.canvas7.bind("<Button-1>",self.x7)
        self.canvas7['cursor']='X_cursor'
        self.canvas7.pack(side=LEFT)

        self.canvas8 = Canvas(self.container3, width = 150, height = 150, bd = 5,bg = cor)
        self.canvas8.bind("<Button-1>",self.x8)
        self.canvas8['cursor']='X_cursor'
        self.canvas8.pack(side=LEFT)

        self.canvas9 = Canvas(self.container3, width = 150, height = 150, bd = 5,bg = cor)
        self.canvas9.bind("<Button-1>",self.x9)
        self.canvas9['cursor']='X_cursor'
        self.canvas9.pack(side=LEFT)


        

    def start_game(self,event):
        m[0] = ['7','8','9']
        m[1] = ['4','5','6']
        m[2] = ['1','2','3']
        if numero_jogos[-1] != 0:
            self.limpa_tela(event)
        for i in range(9):
            flags_click[i] = 0
        self.cria_tabuleiro()
        numero_jogos[-1] = numero_jogos[-1] + 1
        v[-1] = -1
        
    def change_cursor(self,player):
        if player == 'O':
            self.canvas1['cursor']='X_cursor'
            self.canvas1.pack()
            self.canvas2['cursor']='X_cursor'
            self.canvas2.pack()
            self.canvas3['cursor']='X_cursor'
            self.canvas3.pack()
            self.canvas4['cursor']='X_cursor'
            self.canvas4.pack()
            self.canvas5['cursor']='X_cursor'
            self.canvas5.pack()
            self.canvas6['cursor']='X_cursor'
            self.canvas6.pack()
            self.canvas7['cursor']='X_cursor'
            self.canvas7.pack()
            self.canvas8['cursor']='X_cursor'
            self.canvas8.pack()
            self.canvas9['cursor']='X_cursor'
            self.canvas9.pack()
            
        else:
            self.canvas1['cursor']='dot'
            self.canvas1.pack()
            self.canvas2['cursor']='dot'
            self.canvas2.pack()
            self.canvas3['cursor']='dot'
            self.canvas3.pack()
            self.canvas4['cursor']='dot'
            self.canvas4.pack()
            self.canvas5['cursor']='dot'
            self.canvas5.pack()
            self.canvas6['cursor']='dot'
            self.canvas6.pack()
            self.canvas7['cursor']='dot'
            self.canvas7.pack()
            self.canvas8['cursor']='dot'
            self.canvas8.pack()
            self.canvas9['cursor']='dot'
            self.canvas9.pack()
            
    
    
    def limpa_tela(self,event):
        self.canvas1.destroy()
        self.canvas2.destroy()
        self.canvas3.destroy()
        self.canvas4.destroy()
        self.canvas5.destroy()
        self.canvas6.destroy()
        self.canvas7.destroy()
        self.canvas8.destroy()
        self.canvas9.destroy()
        self.score_board.destroy()

        
    def ganhei(self,value,jogador):
        dic_click = {1:self.canvas1,
                 2:self.canvas2,
                 3:self.canvas3,
                 4:self.canvas4,
                 5:self.canvas5,
                 6:self.canvas6,
                 7:self.canvas7,
                 8:self.canvas8,
                 9:self.canvas9
                }
                
        if value < 2:
            number_canvas = who_win(m,v)
        for i in number_canvas:
            dic_click[i]['bg'] = "#" + conjug_color(cor)
            dic_click[i].pack()
        root2 = Tk()
        root2.geometry("200x150+600+300") #tela(comp x larg)+posicaoA+posicaoB
        root2.grab_set() #trava a janela ao ser exibida
        Janelinha(root2,value,jogador)
    

    def x1(self, event):
        muda(v)
        if flags_click[0] == 0:
            if v[-1] % 2 == 0:
                m[0][0] = 'X'
                self.canvas1.create_text(80, 80, text='X',
                                        font=('courier-new','96','bold'),
                                        anchor=CENTER, fill="#ffffff")
                self.change_cursor('X')
            else:
                m[0][0] = 'O'
                self.canvas1.create_text(80, 80, text='O',
                                        font=('courier-new','96','bold'),
                                        anchor=CENTER, fill="#000000")
                self.change_cursor('O')
            flags_click[0] = 1
            result = check_resultado(m)
            if result == 0:
                self.ganhei(result,v[-1])
                block_flags()
                if controle_player[-1] % 2 == 0 and v[-1] % 2 == 0:
                    score_player_1[-1] = score_player_1[-1] + 1
                elif controle_player[-1] % 2 == 0 and v[-1] %2 != 0:
                    score_player_2[-1] = score_player_2[-1] + 1
                elif controle_player[-1] % 2 != 0 and v[-1] %2 == 0:
                    score_player_2[-1] = score_player_2[-1] + 1
                else:
                    score_player_1[-1] = score_player_1[-1] + 1
            elif result == 1:
                self.ganhei(result,v[-1])
        self.score_board.destroy()
        
        self.score_board = Label(self.container5,
                        width=48,
                        height=6,
                        text = "PLACAR\n\n\nJOGADOR 1  "\
                        + " Vs.   "\
                        + "JOGADOR 2 \n\n"\
                        + str(score_player_1[-1])\
                        + "\t"\
                        + str(score_player_2[-1]),
                        background = "white",
                        font = "Verdana" )
        self.score_board.pack()
                
            

    def x2(self, event):
        muda(v)
        if flags_click[1] == 0:
            if v[-1] % 2 == 0:
                m[0][1] = 'X'
                self.canvas2.create_text(80, 80, text='X',
                                    font=('courier-new','96','bold'),
                                    anchor=CENTER, fill="#ffffff")
                self.change_cursor('X')
            else:
                m[0][1] = 'O'
                self.canvas2.create_text(80, 80, text='O',
                                    font=('courier-new','96','bold'),
                                    anchor=CENTER, fill="#000000")
                self.change_cursor('O')
            flags_click[1] = 1
            result = check_resultado(m)
            if result == 0:
                self.ganhei(result,v[-1])
                block_flags()
                if controle_player[-1] % 2 == 0 and v[-1] % 2 == 0:
                    score_player_1[-1] = score_player_1[-1] + 1
                elif controle_player[-1] % 2 == 0 and v[-1] %2 != 0:
                    score_player_2[-1] = score_player_2[-1] + 1
                elif controle_player[-1] % 2 != 0 and v[-1] %2 == 0:
                    score_player_2[-1] = score_player_2[-1] + 1
                else:
                    score_player_1[-1] = score_player_1[-1] + 1
            elif result == 1:
                self.ganhei(result,v[-1])
        self.score_board.destroy()
        
        self.score_board = Label(self.container5,
                        width=48,
                        height=6,
                        text = "PLACAR\n\n\nJOGADOR 1  "\
                        + " Vs.   "\
                        + "JOGADOR 2 \n\n"\
                        + str(score_player_1[-1])\
                        + "\t"\
                        + str(score_player_2[-1]),
                        background = "white",
                        font = "Verdana" )
        self.score_board.pack()

    def x3(self, event):
        muda(v)
        if flags_click[2] == 0:
            if v[-1] % 2 == 0:
                m[0][2] = 'X'
                self.canvas3.create_text(80, 80, text='X',
                                    font=('courier-new','96','bold'),
                                    anchor=CENTER, fill="#ffffff")
                self.change_cursor('X')
            else:
                m[0][2] = 'O'
                self.canvas3.create_text(80, 80, text='O',
                                    font=('courier-new','96','bold'),
                                    anchor=CENTER, fill="#000000")
                self.change_cursor('O')
            flags_click[2] = 1
            result = check_resultado(m)
            if result == 0:
                self.ganhei(result,v[-1])
                block_flags()
                if controle_player[-1] % 2 == 0 and v[-1] % 2 == 0:
                    score_player_1[-1] = score_player_1[-1] + 1
                elif controle_player[-1] % 2 == 0 and v[-1] %2 != 0:
                    score_player_2[-1] = score_player_2[-1] + 1
                elif controle_player[-1] % 2 != 0 and v[-1] %2 == 0:
                    score_player_2[-1] = score_player_2[-1] + 1
                else:
                    score_player_1[-1] = score_player_1[-1] + 1
            elif result == 1:
                self.ganhei(result,v[-1])
        self.score_board.destroy()
        
        self.score_board = Label(self.container5,
                        width=48,
                        height=6,
                        text = "PLACAR\n\n\nJOGADOR 1  "\
                        + " Vs.   "\
                        + "JOGADOR 2 \n\n"\
                        + str(score_player_1[-1])\
                        + "\t"\
                        + str(score_player_2[-1]),
                        background = "white",
                        font = "Verdana" )
        self.score_board.pack()

    def x4(self, event):
        muda(v)
        if flags_click[3] == 0:
            if v[-1] % 2 == 0:
                m[1][0] = 'X'
                self.canvas4.create_text(80, 80, text='X',
                                    font=('courier-new','96','bold'),
                                    anchor=CENTER, fill="#ffffff")
                self.change_cursor('X')
            else:
                m[1][0] = 'O'
                self.canvas4.create_text(80, 80, text='O',
                                    font=('courier-new','96','bold'),
                                    anchor=CENTER, fill="#000000")
                self.change_cursor('O')
            flags_click[3] = 1
            result = check_resultado(m)
            if result == 0:
                self.ganhei(result,v[-1])
                block_flags()
                if controle_player[-1] % 2 == 0 and v[-1] % 2 == 0:
                    score_player_1[-1] = score_player_1[-1] + 1
                elif controle_player[-1] % 2 == 0 and v[-1] %2 != 0:
                    score_player_2[-1] = score_player_2[-1] + 1
                elif controle_player[-1] % 2 != 0 and v[-1] %2 == 0:
                    score_player_2[-1] = score_player_2[-1] + 1
                else:
                    score_player_1[-1] = score_player_1[-1] + 1
            elif result == 1:
                self.ganhei(result,v[-1])
        self.score_board.destroy()
        
        self.score_board = Label(self.container5,
                        width=48,
                        height=6,
                        text = "PLACAR\n\n\nJOGADOR 1  "\
                        + " Vs.   "\
                        + "JOGADOR 2 \n\n"\
                        + str(score_player_1[-1])\
                        + "\t"\
                        + str(score_player_2[-1]),
                        background = "white",
                        font = "Verdana" )
        self.score_board.pack()
                

    def x5(self, event):
        muda(v)
        if flags_click[4] == 0:
            if v[-1] % 2 == 0:
                m[1][1] = 'X'
                self.canvas5.create_text(80, 80, text='X',
                                    font=('courier-new','96','bold'),
                                    anchor=CENTER, fill="#ffffff")
                self.change_cursor('X')
            else:
                m[1][1] = 'O'
                self.canvas5.create_text(80, 80, text='O',
                                    font=('courier-new','96','bold'),
                                    anchor=CENTER, fill="#000000")
                self.change_cursor('O')
            flags_click[4] = 1
            result = check_resultado(m)
            if result == 0:
                self.ganhei(result,v[-1])
                block_flags()
                if controle_player[-1] % 2 == 0 and v[-1] % 2 == 0:
                    score_player_1[-1] = score_player_1[-1] + 1
                elif controle_player[-1] % 2 == 0 and v[-1] %2 != 0:
                    score_player_2[-1] = score_player_2[-1] + 1
                elif controle_player[-1] % 2 != 0 and v[-1] %2 == 0:
                    score_player_2[-1] = score_player_2[-1] + 1
                else:
                    score_player_1[-1] = score_player_1[-1] + 1
            elif result == 1:
                self.ganhei(result,v[-1])
        self.score_board.destroy()
        
        self.score_board = Label(self.container5,
                        width=48,
                        height=6,
                        text = "PLACAR\n\n\nJOGADOR 1  "\
                        + " Vs.   "\
                        + "JOGADOR 2 \n\n"\
                        + str(score_player_1[-1])\
                        + "\t"\
                        + str(score_player_2[-1]),
                        background = "white",
                        font = "Verdana" )
        self.score_board.pack()

    def x6(self, event):
        muda(v)
        if flags_click[5] == 0:
            if v[-1] % 2 == 0:
                m[1][2] = 'X'
                self.canvas6.create_text(80, 80, text='X',
                                    font=('courier-new','96','bold'),
                                    anchor=CENTER, fill="#ffffff")
                self.change_cursor('X')
            else:
                m[1][2] = 'O'
                self.canvas6.create_text(80, 80, text='O',
                                    font=('courier-new','96','bold'),
                                    anchor=CENTER, fill="#000000")
                self.change_cursor('O')
            flags_click[5] = 1
            result = check_resultado(m)
            if result == 0:
                self.ganhei(result,v[-1])
                block_flags()
                if controle_player[-1] % 2 == 0 and v[-1] % 2 == 0:
                    score_player_1[-1] = score_player_1[-1] + 1
                elif controle_player[-1] % 2 == 0 and v[-1] %2 != 0:
                    score_player_2[-1] = score_player_2[-1] + 1
                elif controle_player[-1] % 2 != 0 and v[-1] %2 == 0:
                    score_player_2[-1] = score_player_2[-1] + 1
                else:
                    score_player_1[-1] = score_player_1[-1] + 1
            elif result == 1:
                self.ganhei(result,v[-1])
        self.score_board.destroy()
        
        self.score_board = Label(self.container5,
                        width=48,
                        height=6,
                        text = "PLACAR\n\n\nJOGADOR 1  "\
                        + " Vs.   "\
                        + "JOGADOR 2 \n\n"\
                        + str(score_player_1[-1])\
                        + "\t"\
                        + str(score_player_2[-1]),
                        background = "white",
                        font = "Verdana" )
        self.score_board.pack()        
                
    def x7(self, event):
        muda(v)
        if flags_click[6] == 0:
            if v[-1] % 2 == 0:
                m[2][0] = 'X'
                self.canvas7.create_text(80, 80, text='X',
                                    font=('courier-new','96','bold'),
                                    anchor=CENTER, fill="#ffffff")
                self.change_cursor('X')
            else:
                m[2][0] = 'O'
                self.canvas7.create_text(80, 80, text='O',
                                    font=('courier-new','96','bold'),
                                    anchor=CENTER, fill="#000000")
                self.change_cursor('O')
            flags_click[6] = 1
            result = check_resultado(m)
            if result == 0:
                self.ganhei(result,v[-1])
                block_flags()
                if controle_player[-1] % 2 == 0 and v[-1] % 2 == 0:
                    score_player_1[-1] = score_player_1[-1] + 1
                elif controle_player[-1] % 2 == 0 and v[-1] %2 != 0:
                    score_player_2[-1] = score_player_2[-1] + 1
                elif controle_player[-1] % 2 != 0 and v[-1] %2 == 0:
                    score_player_2[-1] = score_player_2[-1] + 1
                else:
                    score_player_1[-1] = score_player_1[-1] + 1
            elif result == 1:
                self.ganhei(result,v[-1])
        self.score_board.destroy()
        
        self.score_board = Label(self.container5,
                        width=48,
                        height=6,
                        text = "PLACAR\n\n\nJOGADOR 1  "\
                        + " Vs.   "\
                        + "JOGADOR 2 \n\n"\
                        + str(score_player_1[-1])\
                        + "\t"\
                        + str(score_player_2[-1]),
                        background = "white",
                        font = "Verdana" )
        self.score_board.pack()

        
    def x8(self, event):
        muda(v)
        if flags_click[7] == 0:
            if v[-1] % 2 == 0:
                m[2][1] = 'X'
                self.canvas8.create_text(80, 80, text='X',
                                    font=('courier-new','96','bold'),
                                    anchor=CENTER, fill="#ffffff")
                self.change_cursor('X')
            else:
                m[2][1] = 'O'
                self.canvas8.create_text(80, 80, text='O',
                                    font=('courier-new','96','bold'),
                                    anchor=CENTER, fill="#000000")
                self.change_cursor('O')
            flags_click[7] = 1
            result = check_resultado(m)
            if result == 0:
                self.ganhei(result,v[-1])
                block_flags()
                if controle_player[-1] % 2 == 0 and v[-1] % 2 == 0:
                    score_player_1[-1] = score_player_1[-1] + 1
                elif controle_player[-1] % 2 == 0 and v[-1] %2 != 0:
                    score_player_2[-1] = score_player_2[-1] + 1
                elif controle_player[-1] % 2 != 0 and v[-1] %2 == 0:
                    score_player_2[-1] = score_player_2[-1] + 1
                else:
                    score_player_1[-1] = score_player_1[-1] + 1
            elif result == 1:
                self.ganhei(result,v[-1])
        self.score_board.destroy()
        
        self.score_board = Label(self.container5,
                        width=48,
                        height=6,
                        text = "PLACAR\n\n\nJOGADOR 1  "\
                        + " Vs.   "\
                        + "JOGADOR 2 \n\n"\
                        + str(score_player_1[-1])\
                        + "\t"\
                        + str(score_player_2[-1]),
                        background = "white",
                        font = "Verdana" )
        self.score_board.pack()
                
    def x9(self, event):
        muda(v)
        if flags_click[8] == 0:
            if v[-1] % 2 == 0:
                m[2][2] = 'X'
                self.canvas9.create_text(80, 80, text='X',
                                    font=('courier-new','96','bold'),
                                    anchor=CENTER, fill="#ffffff")
                self.change_cursor('X')
            else:
                m[2][2] = 'O'
                self.canvas9.create_text(80, 80, text='O',
                                    font=('courier-new','96','bold'),
                                    anchor=CENTER, fill="#000000")
                self.change_cursor('O')

            flags_click[8] = 1
            result = check_resultado(m)
            if result == 0:
                self.ganhei(result,v[-1])
                block_flags()
                if controle_player[-1] % 2 == 0 and v[-1] % 2 == 0:
                    score_player_1[-1] = score_player_1[-1] + 1
                elif controle_player[-1] % 2 == 0 and v[-1] %2 != 0:
                    score_player_2[-1] = score_player_2[-1] + 1
                elif controle_player[-1] % 2 != 0 and v[-1] %2 == 0:
                    score_player_2[-1] = score_player_2[-1] + 1
                else:
                    score_player_1[-1] = score_player_1[-1] + 1
            elif result == 1:
                self.ganhei(result,v[-1])
        self.score_board.destroy()
        
        self.score_board = Label(self.container5,
                        width=48,
                        height=6,
                        text = "PLACAR\n\n\nJOGADOR 1  "\
                        + " Vs.   "\
                        + "JOGADOR 2 \n\n"\
                        + str(score_player_1[-1])\
                        + "\t"\
                        + str(score_player_2[-1]),
                        background = "white",
                        font = "Verdana" )
        self.score_board.pack()        
                                    
                                   
                                    
    
def conjug_color(cor):
    cor = '0x' + cor[1:]
    cor_dec = int(cor,16)
    max_cor = int('0xffffff', 16)
    return hex(max_cor - cor_dec).split('x')[-1]

    
def muda(v):
    v[-1] = v[-1] +1
    
def who_win(m,player):
    if player[-1] % 2 == 0:
        #X
        aux = 0
        possible = [
                    [1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [1,4,7],
                    [2,5,8],
                    [3,6,9],
                    [1,5,9],
                    [3,5,7]
                    ]
        #Para cada linha
        for i in m:
            if "".join(i) == 'XXX':
                return possible[aux]
            else:
                aux = aux + 1
                
        #Para cada coluna
        if str(m[0][0]) + str(m[1][0]) + str(m[2][0]) == 'XXX':
            return possible[aux]
        elif str(m[0][1]) + str(m[1][1]) + str(m[2][1]) == 'XXX':
            return possible[aux + 1]
        elif str(m[0][2]) + str(m[1][2]) + str(m[2][2]) == 'XXX':
            return possible[aux + 2]
        else:
            aux = aux + 3
        
        
        #Para cada diagonal
        if str(m[0][0]) + str(m[1][1]) + str(m[2][2]) == 'XXX':
            return possible[aux]
        elif str(m[2][0]) + str(m[1][1]) + str(m[0][2]) == 'XXX':
            return possible[aux + 1]
        
        else:
            return []
    else:
        #O
        aux = 0
        possible = [
                    [1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [1,4,7],
                    [2,5,8],
                    [3,6,9],
                    [1,5,9],
                    [3,5,7]
                    ]
        #Para cada linha
        for i in m:
            if "".join(i) == 'OOO':
                return possible[aux]
            else:
                aux = aux + 1
                
        #Para cada coluna
        if str(m[0][0]) + str(m[1][0]) + str(m[2][0]) == 'OOO':
            return possible[aux]
        elif str(m[0][1]) + str(m[1][1]) + str(m[2][1]) == 'OOO':
            return possible[aux + 1]
        elif str(m[0][2]) + str(m[1][2]) + str(m[2][2]) == 'OOO':
            return possible[aux + 2]
        else:
            aux = aux + 3
        
        
        #Para cada diagonal
        if str(m[0][0]) + str(m[1][1]) + str(m[2][2]) == 'OOO':
            return possible[aux]
        elif str(m[2][0]) + str(m[1][1]) + str(m[0][2]) == 'OOO':
            return possible[aux + 1]
        
        else:
            return []
    
def block_flags():
    flags_click[0] = 1
    flags_click[1] = 1
    flags_click[2] = 1
    flags_click[3] = 1
    flags_click[4] = 1
    flags_click[5] = 1
    flags_click[6] = 1
    flags_click[7] = 1
    flags_click[8] = 1
        
        
        
def check_resultado(m):
    #0 vitoria
    #1 empate
    #2 nada
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
        
    

def main():    
    #janela principal da tkinter
    raiz=Tk()
    raiz.title('Tic Tac Toe')
    raiz.attributes('-fullscreen', True)
    
    
    
    #chama classe e passa a janela principal como parametro
    Janela(raiz)        

    #deixa a janela rodando em loopin para nao ser perdida a menos que alguma acao seja realizada
    raiz.mainloop()


if __name__ == '__main__':
    main()
