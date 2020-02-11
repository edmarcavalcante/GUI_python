import PIL.Image, PIL.ImageTk
from tkinter import *
from tkinter import filedialog
import os

root = Tk() #root é um objeto da classe Tk(). Essa classe pertence á library Tkinter
#root.mainloop()# comando necessário para abrir a janela GUI

#Vamos adicionar o título da janela, definir as dimensões em pixels, # adicionar uma
#um painel de layout e uma imagem para decorar

root.title("GUI experimental") #define o título da janela
root.geometry('550x550') #define o tamanho da janela

#panel_title é uma variável de 'Label' e será responsável por
# definir o título para o painel.
#obs: janela GUI =! painel

panel_title = Label(root, text='GUI experimental version 1.0', font=('heveltica',
                                                                     16), pady=20)
#observa-se que Label também é uma classe da library tkinter. panel_title é um objeto dessa classe
# a classe Label recebe vários parâmetros, ex: root, o título do painel, a fonte e o espaçamento
# vertical no plano carteziano de 20 pixels (pady=20)
panel_title.pack()

img = PIL.ImageTk.PhotoImage(PIL.Image.open('mar_azul.jfif'))
panel = Label(root, image = img)
panel.pack()

root.mainloop()
