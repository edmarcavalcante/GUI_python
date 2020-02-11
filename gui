import PIL.Image, PIL.ImageTk
from tkinter import *
from tkinter import filedialog
import os

root = Tk() #root é um objeto da classe Tk(). Essa classe pertence á library Tkinter
root.mainloop()# comando necessário para abrir a janela GUI

#Vamos adicionar o título da janela, definir as dimensões em pixels, # adicionar uma
#um painel de layout e uma imagem para decorar

root.title("GUI experimental")
root.geometry('550x550')

panel_title = Label(root, text='GUI experimental version 1.0', font=('heveltica',
                                                                     16), pady=20)
panel_title.pack()

img = PIL.ImageTk.PhotoImage(PIL.Image.open('mar_azul.jpg'))
panel = Label(root, image = img)
panel.pack()

root.mainloop()
