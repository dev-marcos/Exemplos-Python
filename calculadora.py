import tkinter as tk

def pressar_botao(valor):
    entrada.insert(tk.END, valor)

def limpar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        limpar()
        entrada.insert(tk.END, str(resultado))
    except Exception as e:
        limpar()
        entrada.insert(tk.END, "Erro")

root = tk.Tk()
root.title("Calculadora")

# Entrada para exibir e inserir números
entrada = tk.Entry(root, width=25, borderwidth=5)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botões da calculadora
botoes = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for (texto, linha, coluna) in botoes:
    if texto != "C" and texto != "=":
        botao = tk.Button(root, text=texto, padx=20, pady=20, command=lambda t=texto: pressar_botao(t))
        botao.grid(row=linha, column=coluna)
    elif texto == "C":
        botao = tk.Button(root, text=texto, padx=20, pady=20, command=limpar)
        botao.grid(row=linha, column=coluna)
    else:
        botao = tk.Button(root, text=texto, padx=20, pady=20, command=calcular)
        botao.grid(row=linha, column=coluna)

root.mainloop()
