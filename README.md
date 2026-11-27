# Equilíbrio IMC

Aplicativo de desktop com interface gráfica que calcula o Índice de Massa Corporal (IMC) e informa a categoria do resultado. Desenvolvido em Python 3 com Tkinter.

Trabalho da **4ª Avaliação** da disciplina de Lógica, Algoritmos e Programação, do Curso Superior de Tecnologia em Banco de Dados (Piauí Instituto de Tecnologia), com o professor M.Sc. Tiago Martins Ribeiro.

## Integrantes

- Marcus David de Sousa Bastos
- Francisco David de Oliveira Lopes

## O que o app faz

- Recebe o **peso (kg)** e a **altura (m)** digitados pelo usuário.
- Calcula o IMC com a fórmula `peso / altura²` e mostra o resultado com 2 casas decimais.
- Classifica o resultado em uma das categorias abaixo:

| IMC | Categoria |
|---|---|
| menor que 18,5 | Abaixo do peso |
| de 18,5 a 24,9 | Peso normal |
| de 25 a 29,9 | Sobrepeso |
| 30 ou mais | Obesidade |

- Aceita números com vírgula ou ponto (`1,75` ou `1.75`).
- Mostra uma mensagem de erro quando os valores digitados não são numéricos.
- Possui o botão **Limpar**, que apaga os campos e volta a tela ao estado inicial.

## Projeto original e personalizações

Este projeto foi desenvolvido a partir do vídeo da playlist *Python na Prática | Projetos Python*, do canal **Usando Python** no YouTube.

- Vídeo original: https://youtu.be/CrZkNmpPWVo?si=_rstBk1hFil-Bl_y
- Crédito: canal Usando Python.

Personalizações feitas pela dupla em relação ao original:

- **Nome:** o app passou a se chamar "Equilíbrio IMC" (título da janela e interface).
- **Layout:** janela de 590x460, fontes maiores (Verdana), campos e botões reposicionados.
- **Cores:** nova paleta de cores (fundo escuro, textos brancos e detalhes em verde).
- **Funcionalidades extras:** tratamento de erro com `messagebox`, aceitação de vírgula nos números e botão Limpar.

## Como instalar e executar

### Requisitos

- Python 3.8 ou superior
- Tkinter (já vem instalado com o Python no Windows e no macOS)

O projeto não usa bibliotecas externas, então não é necessário um `requirements.txt`.

No Linux, se o Tkinter não estiver instalado:

```bash
sudo apt install python3-tk
```

### Passo a passo

1. Clone o repositório:

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
```

2. Execute o aplicativo:

```bash
python main_1.0.py
```

No Linux e no macOS, use `python3` no lugar de `python`.

## Como usar

1. Digite o peso em quilos (exemplo: `70`).
2. Digite a altura em metros (exemplo: `1,75`).
3. Clique em **Calcular** para ver o IMC e a categoria.
4. Clique em **Limpar** para fazer uma nova consulta.

## Estrutura do código

| Parte | O que faz |
|---|---|
| Janela | Cria a janela principal, define título, tamanho e cor de fundo |
| Frames | Divide a janela em duas áreas: cabeçalho e área de cálculo |
| Componentes | Labels, campos de entrada (`Entry`) e botões |
| `calcular()` | Lê os valores, calcula o IMC, classifica a categoria e trata erros |
| `limpar()` | Apaga os campos e reinicia o resultado |
| `mainloop()` | Mantém a janela aberta esperando as ações do usuário |

## Captura de tela

<img width="735" height="607" alt="Captura de tela 2026-11-27 192506" src="https://github.com/user-attachments/assets/c9a8e98a-e480-4345-b1c2-f9921a27b918" />


## Tecnologias

- Python 3
- Tkinter
