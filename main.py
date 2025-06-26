import tkinter as tk

# Função para adicionar números e operadores na tela
def adicionar(valor):
    entrada.insert(tk.END, valor)

# Função para limpar a tela
def limpar():
    entrada.delete(0, tk.END)

# Função para calcular o resultado da expressão na tela
def calcular():
    expressao = entrada.get()
    try:
        resultado = eval(expressao)  # Avalia a expressão matemática
        limpar()
        entrada.insert(0, str(resultado))
    except:
        limpar()
        entrada.insert(0, "Erro")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")
janela.resizable(False, False)

# Entrada onde aparece a expressão e o resultado
entrada = tk.Entry(janela, font=("Arial", 24), borderwidth=2, relief="ridge", justify="right")
entrada.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

# Lista dos botões com seus textos e posições na grade (row, column)
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
]

# Criar e posicionar os botões
for (texto, linha, coluna) in botoes:
    if texto == 'C':
        botao = tk.Button(janela, text=texto, font=("Arial", 20), command=limpar)
    else:
        botao = tk.Button(janela, text=texto, font=("Arial", 20), command=lambda t=texto: adicionar(t))
    botao.grid(row=linha, column=coluna, sticky="nsew", padx=5, pady=5)

# Botão igual com destaque
botao_igual = tk.Button(janela, text='=', font=("Arial", 20), bg="#4CAF50", fg="white", command=calcular)
botao_igual.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# Configurar pesos para que os botões expandam proporcionalmente
for i in range(6):  # 0 a 5 linhas
    janela.grid_rowconfigure(i, weight=1)
for j in range(4):  # 0 a 3 colunas
    janela.grid_columnconfigure(j, weight=1)

# Executar o loop principal da interface
janela.mainloop()