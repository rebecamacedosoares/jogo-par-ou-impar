from tkinter import *
from constantes import *
from calculoParImpar import *
import random

import sys
import os
import tkinter.messagebox as mbox


def restartProgram():
    python = sys.executable
    os.execl(python, python, *sys.argv)


raiz = Tk()


class Janela:
    '''Classe do jogo'''
    def __init__(self, raiz):
        self.fr1 = Frame(raiz, background=fundo)
        self.fr1.pack()

        self.fr_result = Frame(raiz, background=fundo)
        self.fr_result.pack()

        self.fr2 = Frame(raiz, background=fundo)
        self.fr2.pack()

        self.fr3 = Frame(raiz, background=fundo)
        self.fr3.pack()

        self.fr4 = Frame(raiz, background=fundo)
        self.fr4.pack()

        self.fr5 = Frame(raiz, background=fundo)
        self.fr5.pack()

        self.fr6 = Frame(raiz, background=fundo)
        self.fr6.pack()

        self.img_player = PhotoImage(file='imagens/ninja.png')
        self.img_pc = PhotoImage(file='imagens/robot.png')
        self.img0 = PhotoImage(file='imagens/numero_0.png')
        self.img1 = PhotoImage(file='imagens/numero_1.png')
        self.img2 = PhotoImage(file='imagens/numero_2.png')
        self.img3 = PhotoImage(file='imagens/numero_3.png')
        self.img4 = PhotoImage(file='imagens/numero_4.png')
        self.img5 = PhotoImage(file='imagens/numero_5.png')
        self.img6 = PhotoImage(file='imagens/numero_6.png')
        self.img7 = PhotoImage(file='imagens/numero_7.png')
        self.img8 = PhotoImage(file='imagens/numero_8.png')
        self.img9 = PhotoImage(file='imagens/numero_9.png')
        self.img10 = PhotoImage(file='imagens/numero_10.png')

        self.lb1 = Label(self.fr1, text='JOGO DE PAR OU ÍMPAR', background=fundo, font=fonte1, fg=cor1, pady=15, padx=35)
        self.lb1.pack(side=LEFT)

        self.btr = Button(self.fr1, text='Restart', font=fonte4, relief=RAISED, command=self.resetar1)
        self.btr.bind('<Return>', self.resetar2)
        self.btr.pack(side=LEFT)

        self.lb_result = Label(self.fr_result, text='', font=fonte1, fg=cor2, bg=fundo)
        self.lb_result.pack()

        self.placar1 = 0
        self.placar2 = 0

        self.lb2 = Label(self.fr2, text='       Jogador  ' + str(self.placar1) + '  X  ' +
                         str(self.placar2) + '  Computador', bg=fundo, font=fonte2, fg=cor1, pady=10)
        self.lb2.pack()

        self.lb_img1 = Label(self.fr3, image=self.img_player, bg=fundo)
        self.lb_img1.pack(side=LEFT)

        self.lb_separador = Label(self.fr3, text='         ', bg=fundo)
        self.lb_separador.pack(side=LEFT)

        self.lb_img2 = Label(self.fr3, image=self.img_pc, bg=fundo)
        self.lb_img2.pack(side=LEFT)

        self.escolha = StringVar()

        self.rb_par = Radiobutton(self.fr4, text='Par', value='par', variable=self.escolha, bg=fundo, fg=cor1, font=fonte2, pady=20)
        self.rb_par.pack(side=LEFT)

        self.rb_impar = Radiobutton(self.fr4, text='Ímpar', value='impar', variable=self.escolha, bg=fundo, fg=cor1, font=fonte2, pady=20)
        self.rb_impar.pack(side=LEFT)

        self.lb3 = Label(self.fr5, text='Número de 0 a 10: ', bg=fundo, fg=cor1, font=fonte3, width=15, pady=20)
        self.lb3.pack(side=LEFT)

        self.num = Entry(self.fr5, width=2, font=fonte3)
        self.num.pack(side=LEFT)

        self.bt1 = Button(self.fr6, bg=cor3, text='JOGAR', font=fonte1, relief=RAISED, border=8, command=self.jogar)
        self.bt1.bind("<Return>", self.jogar)
        self.bt1.focus_force()
        self.bt1.pack()
    
        self.lb_erro = Label(self.fr6, text='', font=fonte4, bg=fundo, fg=red)
        self.lb_erro.pack()


    def jogar(self, event=''):
        try:
            num = int(self.num.get())
            escolha = self.escolha.get()
            numRobo = random.randrange(0,11)

            if escolha == 'par' or escolha == 'impar':   
                if num >= 0 and num <= 10:
                    parImpar = calcularParImpar(num, numRobo)

                    if parImpar == 'par':
                        self.lb_result['text'] = 'DEU PAR'
                    elif parImpar == 'impar':
                        self.lb_result['text'] = 'DEU ÍMPAR'


                    if num == 0:
                        self.lb_img1['image'] = self.img0
                        self.lb_erro['text'] = ''
                    elif num == 1:
                        self.lb_img1['image'] = self.img1
                        self.lb_erro['text'] = ''
                    elif num == 2:
                        self.lb_img1['image'] = self.img2
                        self.lb_erro['text'] = ''
                    elif num == 3:
                        self.lb_img1['image'] = self.img3
                        self.lb_erro['text'] = ''
                    elif num == 4:
                        self.lb_img1['image'] = self.img4
                        self.lb_erro['text'] = ''
                    elif num == 5:
                        self.lb_img1['image'] = self.img5
                        self.lb_erro['text'] = ''
                    elif num == 6:
                        self.lb_img1['image'] = self.img6
                        self.lb_erro['text'] = ''
                    elif num == 7:
                        self.lb_img1['image'] = self.img7
                        self.lb_erro['text'] = ''
                    elif num == 8:
                        self.lb_img1['image'] = self.img8
                        self.lb_erro['text'] = ''
                    elif num == 9:
                        self.lb_img1['image'] = self.img9
                        self.lb_erro['text'] = ''
                    elif num == 10:
                        self.lb_img1['image'] = self.img10
                        self.lb_erro['text'] = ''
                    

                    if numRobo == 0:
                        self.lb_img2['image'] = self.img0
                        self.lb_erro['text'] = ''
                    elif numRobo == 1:
                        self.lb_img2['image'] = self.img1
                        self.lb_erro['text'] = ''
                    elif numRobo == 2:
                        self.lb_img2['image'] = self.img2
                        self.lb_erro['text'] = ''
                    elif numRobo == 3:
                        self.lb_img2['image'] = self.img3
                        self.lb_erro['text'] = ''
                    elif numRobo == 4:
                        self.lb_img2['image'] = self.img4
                        self.lb_erro['text'] = ''
                    elif numRobo == 5:
                        self.lb_img2['image'] = self.img5
                        self.lb_erro['text'] = ''
                    elif numRobo == 6:
                        self.lb_img2['image'] = self.img6
                        self.lb_erro['text'] = ''
                    elif numRobo == 7:
                        self.lb_img2['image'] = self.img7
                        self.lb_erro['text'] = ''
                    elif numRobo == 8:
                        self.lb_img2['image'] = self.img8
                        self.lb_erro['text'] = ''
                    elif numRobo == 9:
                        self.lb_img2['image'] = self.img9
                        self.lb_erro['text'] = ''
                    elif numRobo == 10:
                        self.lb_img2['image'] = self.img10
                        self.lb_erro['text'] = ''

                    if parImpar == 'par' and escolha == 'par':
                        self.placar1 += 1
                        self.lb2['text'] = '       Jogador  ' + str(self.placar1) + '  X  ' + str(self.placar2) + '  Computador'
                    elif parImpar == 'par' and escolha == 'impar':
                        self.placar2 += 1
                        self.lb2['text'] = '       Jogador  ' + str(self.placar1) + '  X  ' + str(self.placar2) + '  Computador'
                    elif parImpar == 'impar' and escolha == 'impar':
                        self.placar1 += 1
                        self.lb2['text'] = '       Jogador  ' + str(self.placar1) + '  X  ' + str(self.placar2) + '  Computador'
                    else:
                        self.placar2 += 1
                        self.lb2['text'] = '       Jogador  ' + str(self.placar1) + '  X  ' + str(self.placar2) + '  Computador'

                else:
                    self.lb_erro['text'] = 'ERRO. ESCOLHA PAR OU ÍMPAR E DIGITE DE 0 A 10.'
            else:
                    self.lb_erro['text'] = 'ERRO. ESCOLHA PAR OU ÍMPAR E DIGITE DE 0 A 10.'

    

        except:
            self.lb_erro['text'] = 'ERRO. ESCOLHA PAR OU ÍMPAR E DIGITE DE 0 A 10.'

    def resetar1(self):
        resposta = mbox.askquestion('Restart','Deseja reiniciar o jogo?')
        if resposta == 'yes':
            self.lb_result['text'] = ''
            self.lb_img1['image'] = self.img_player
            self.lb_img2['image'] = self.img_pc
            self.placar1 = 0
            self.placar2 = 0
            self.lb2['text'] = '       Jogador  ' + str(self.placar1) + '  X  ' + str(self.placar2) + '  Computador'
            self.lb_erro['text'] = ''

    def resetar2(self, event):
        resposta = mbox.askquestion('Restart','Deseja reiniciar o jogo?')
        if resposta == 'yes':
            self.lb_result['text'] = ''
            self.lb_img1['image'] = self.img_player
            self.lb_img2['image'] = self.img_pc
            self.placar1 = 0
            self.placar2 = 0
            self.lb2['text'] = '       Jogador  ' + str(self.placar1) + '  X  ' + str(self.placar2) + '  Computador'
            self.lb_erro['text'] = ''

'''    def jogar2(self, event):
        pass'''


raiz.geometry("840x650+300+30")
raiz.iconbitmap('imagens/ninjaa.ico')
raiz.title('Par ou Ímpar')
raiz['background'] = fundo

janela = Janela(raiz)

raiz.mainloop()