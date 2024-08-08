from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.geometry('300x200')
root.maxsize(400, 220)
root.minsize(400, 220)
root.title('Sorteio')
root.configure(bg='#C0C0C0')

def senha_aleatoria():
    caracteres_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    caracteres_low = 'abcdefghijklmnopqrstuvwxyz'
    numeros = '1234567890'
    simbolos_especias = '!@#$[]'

    password = caracteres_up + caracteres_low + numeros + simbolos_especias

    senha_gerada = ''
    for i in range(8):
        senha_gerada += random.choice(password)

    messagebox.showinfo('Senha', senha_gerada)
    print(senha_gerada)

botao_senha = Button(root, text='Gerar Senha', bg='#836FFF', fg='white', font='Arial 16 bold', width=15, command=senha_aleatoria)
botao_senha.pack(expand=True)

root.mainloop()