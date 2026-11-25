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

#----------configurando frame cima----------------

#criando o nome do app
app_nome = Label(frame_cima, text="Equilíbrio IMC", width=30, height=1, padx=0, relief="flat", anchor="center", font=("Ivy 24 bold "), bg=co0, fg=co1)
app_nome.place(x=0, y=10)

#criando uma linha abaixo do nome do app
app_linha = Label(frame_cima, text="", width=800, height=1, padx=0, relief="flat", anchor="center", font=("Ivy 1 "), bg=co1, fg=co1)
app_linha.place(x=0, y=70)



#-----função calcular--------

#função para calcular o IMC
def calcular():

    try:
        #pegando os valores digitados pelo usuário
        peso = float(e_peso.get().replace(",", "."))
        altura = float(e_altura.get().replace(",", "."))

        #calculando o IMC
        imc = peso / altura**2

        #mostrando o resultado do IMC na tela
        resultado = imc
        
        #if para classificar a categoria do resultado do IMC
        if resultado < 18.5:
            l_resultado_texto["text"] = "O seu IMC: Abaixo do peso"
            

        elif resultado >= 18.5 and resultado < 25:
            l_resultado_texto["text"] = "O seu IMC: Peso normal"
            

        elif resultado >= 25 and resultado < 30:
            l_resultado_texto["text"] = "O seu IMC: Sobrepeso"
            

        else:
            l_resultado_texto["text"] = "O seu IMC: Obesidade"
            

        l_resultado["text"] = "{:.{}f}".format(resultado, 2)
    
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos para peso e altura.")

#criando o label para o peso
l_peso = Label(frame_baixo, text="Digite seu peso(kg):", height=1, padx=0, relief="flat", anchor="center", font=("Ivy 16 bold "), bg=co0, fg=co1)
l_peso.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)

#criando o entry para o peso
e_peso = Entry(frame_baixo, width=8, relief="solid", font=("Ivy 16 bold "), justify="center")
e_peso.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)

#criando o label para a altura
l_altura = Label(frame_baixo, text="Digite sua altura(m):", height=1, padx=0, relief="flat", anchor="center", font=("Ivy 16 bold "), bg=co0, fg=co1)
l_altura.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)

#criando o entry para a altura
e_altura = Entry(frame_baixo, width=8, relief="solid", font=("Ivy 16 bold "), justify="center")
e_altura.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)

#criando o label para o resultado
l_resultado = Label(frame_baixo, text="---", width=5, height=1, padx=1, pady=12, relief="flat", anchor="center", font=("Ivy 28 bold "), bg=co2, fg=co1)
l_resultado.place(x=430, y=15)

#criando o label para o resultado do texto
l_resultado_texto = Label(frame_baixo, text="", width=45, height=1, padx=0, pady=12, relief="flat", anchor="center", font=("Ivy 16 bold "), bg=co0, fg=co1)
l_resultado_texto.place(x=0, y=110)

#criando o botão para calcular
b_calcular = Button(frame_baixo, command=calcular, text="Calcular", width=43, height=1, overrelief=SOLID, padx=0, pady=20, relief="raised", anchor="center", font=("Ivy 16 bold "), bg=co2, fg=co0)
b_calcular.grid(row=4, column=0, columnspan=150, sticky=NSEW, pady=90, padx=10)


#loop infinito da janela
janela.mainloop()
