from tkinter import *
import pyqrcode

class Qrcode():

    def __init__(self,texto):
        self.texto = texto
    def criarNovo(self):
        qr = pyqrcode.create(self.texto)
        qr.png('Qrcode.png',scale=8)
        print('Gerado com sucesso!')

class Tela():
    def __init__(self,master):
        self.frame = Frame(master)
        self.frame.pack()

        self.label = Label(self.frame,text='teste',background='white',width='35',height='15')
        self.label.pack()

        self.texto = Entry(self.frame)
        self.texto.pack(side=LEFT)

        self.botao = Button(self.frame,text='Gerar',command=self.gerar)
        self.botao.pack()

    def gerar(self):
        self.imagem = Qrcode(self.texto.get())
        self.texto.delete(0,END)
        self.imagem.criarNovo()
        image = PhotoImage(file='./Qrcode.png')
        self.label.config(image=image,width='280',height='260')
        self.label.imagem= image

root = Tk()
root.title('Gerador de QrCode')
root.resizable(0,0)
root.geometry('300x300+700+400')

Tela(root)

root.mainloop()