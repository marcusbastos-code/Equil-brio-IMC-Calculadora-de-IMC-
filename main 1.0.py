#importando os conteudos basicos da biblioteca tkinter
from tkinter import *
#importando um submodulo mais atualizado 
from tkinter import ttk
from tkinter import messagebox

#criação da janela
janela = Tk()
#Titulo da Janela
janela.title("Equilíbrio IMC")
#Dimensões da Janela
janela.geometry("590x460")
#Cor de Fundo da Janela
janela.configure(bg="black")

#cores

co0 = "#121218" #preto
co1 = "#ffffff" #branco  
co2 = "#2E8B57" #verde 

#----------dividindo a janela em 2 partes----------------

#criando um frame para a parte superior da janela
frame_cima = Frame(janela, width=590, height=100, bg=co0, pady=0, padx=0, relief="flat")
#colocando o frame na janela
frame_cima.grid(row=0, column=0, sticky=NSEW)

#criando um frame para a parte inferior da janela
frame_baixo = Frame(janela, width=590, height=360, bg=co0, pady=0, padx=0, relief="flat")
#colocando o frame na janela
frame_baixo.grid(row=1, column=0, sticky=NSEW)
