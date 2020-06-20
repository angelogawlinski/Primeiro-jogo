from tkinter import *
from constantes import *
import random

from retangulo import Retangulo
from bola import Bola

class Jogo(object):
    def __init__(self):

      
        self.root = Tk()
        self.root.geometry('%ix%i' %(LARGURA, ALTURA))
        self.root.resizable(False, False)
        self.root.title('Primeiro Jogo')

      
        self.frame = Frame(bg="blue")
        self.frame.pack()

        self.canvas = Canvas(self.frame, bg="blue", width=CANVAS_L, height=CANVAS_A, cursor = 'target')
        self.canvas.pack()

        
       
        self.comecar = Button(self.root, text='INCIAR', command=self.começa)
        self.comecar.focus_force()
        self.comecar.pack()

        self.comecar.bind('<Return>', self.começa)
        self.novoJogo()
          
        self.root.mainloop()


    def novoJogo(self):
        
        self.player = Retangulo(largura = 100, altura = 20, cor = 'white', pos = (LARGURA//2 + 360, 380), vel = (15, 15), tag = 'player')
        self.player.desenhar(self.canvas)
        self.canvas.bind('<Motion>', self.move_player)
        
        self.bola = Bola(raio = 30, cor = 'red', pos = (100, 200), vel = (3, 3))
        
        
        
        self.r = []
        l, c, e = 5, 8, 2
        b, h, y0 = 48, 20, 50

        for i in range(l):
            cor = random.choice(['black', 'orange', 'white', 'lightgray', 'yellow', 'green', 'purple'])
            for j in range(c):
                r = Retangulo(b, h, cor, (b*j+(j+1)*e, i*h+(i+1)*e + y0), (0, 0), 'rect')
                self.r.append(r)
        self.canvas.create_text(CANVAS_L/2, CANVAS_A/2, text = 'Bem Vindos!!', fill='white', font='Verdana, 12')

        self.jogando = True

    def começa(self):
        self.jogar()

    def jogar(self):
        
        if self.jogando:
            self.update()
            self.desenhar()
            
            if len(self.r) == 0:
                self.jogando = False
                self.msg = "VOCÊ GANHOU!!"
            if self.bola.y > CANVAS_A:
                self.jogando = False
                self.msg = "VOCÊ PERDEU!!"
                
            self.root.after(10, self.jogar)
        else:
            self.acabou(self.msg)


    def move_player(self, event):

        if event.x > 0 and event.x < CANVAS_L - self.player.b:
            self.player.x = event.x

    def update(self):
     
        self.bola.update(self)

        
    def recomeça(self):
        self.novoJogo()
        self.comecar['text'] = 'INICIAR'
        self.jogar()


    def acabou(self, msg):
        self.canvas.delete(ALL)
        self.canvas.create_text(CANVAS_L/2, CANVAS_A/2, text= msg, fill='white')
        self.comecar['text'] = 'Reiniciar'
        self.comecar['command'] = self.recomeça


    def desenhar(self):

        self.canvas.delete(ALL)

        self.player.desenhar(self.canvas)
       
        for r in self.r:
            r.desenhar(self.canvas)
 
        self.bola.desenhar(self.canvas)
         
        

    def verificaColisao(self):
       
        coord = self.canvas.bbox('bola')
     

        colisoes = self.canvas.find_overlapping(*coord)

        if len(colisoes) != 0:
            if colisoes[0] != self.player:
            
                m_p = self.canvas.find_closest(coord[0], coord[1])
            
                for r in self.r:
            
                    if r == m_p[0]:
                        self.r.remove(r)   
                        self.canvas.delete(r)
                        self.b_vy *= -1
                        return

                        

if __name__ == '__main__':
    Jogo()       



        
