import tkinter as tk
from tkinter import messagebox, simpledialog
import numpy as np

def parse_matrix(text):
    try:
        matrix = [list(map(float, row.split())) for row in text.strip().split('\n')]
        return np.array(matrix)
    except:
        messagebox.showerror("Erro", "Formato inválido! Use espaço entre números e ENTER para nova linha.")
        return None

def forma_escada(matriz):
    try:
        m = matriz.astype(float)
        rows, cols = m.shape
        for i in range(min(rows, cols)):
            if m[i, i] == 0:
                for j in range(i+1, rows):
                    if m[j, i] != 0:
                        m[[i, j]] = m[[j, i]]
                        break
            m[i] = m[i] / m[i, i]
            for j in range(rows):
                if j != i:
                    m[j] = m[j] - m[i]*m[j, i]
        return m
    except Exception as e:
        return f"Erro: {str(e)}"

def inversa(matriz):
    try:
        inv = np.linalg.inv(matriz)
        return inv
    except np.linalg.LinAlgError:
        return "Matriz não é invertível."

def eh_invertivel(matriz):
    try:
        np.linalg.inv(matriz)
        return "Sim. A matriz é invertível."
    except np.linalg.LinAlgError:
        return "Não. A matriz NÃO é invertível."

def calcular_posto(matriz):
    return f"O posto da matriz é {np.linalg.matrix_rank(matriz)}"

def resolver_sistema(matriz):
    try:
        linhas, colunas = matriz.shape
        if colunas != linhas + 1:
            return "A matriz deve ser aumentada (última coluna = termos independentes)."
        A = matriz[:, :-1]
        b = matriz[:, -1]
        x = np.linalg.solve(A, b)
        return f"Solução: {x}"
    except Exception as e:
        return f"Erro ao resolver sistema: {str(e)}"

def executar_operacao():
    matriz_texto = entrada_matriz.get("1.0", tk.END)
    matriz = parse_matrix(matriz_texto)
    if matriz is None:
        return

    operacao = opcoes.get()
    resultado = ""

    if operacao == "Forma Escada (Gauss-Jordan)":
        resultado = forma_escada(matriz)
    elif operacao == "Inversa da Matriz":
        resultado = inversa(matriz)
    elif operacao == "Verificar se é Invertível":
        resultado = eh_invertivel(matriz)
    elif operacao == "Posto da Matriz":
        resultado = calcular_posto(matriz)
    elif operacao == "Resolver Sistema Linear":
        resultado = resolver_sistema(matriz)

    if isinstance(resultado, np.ndarray):
        resultado = np.round(resultado, 2)
        resultado = "\n".join([" ".join(map(str, row)) for row in resultado])
    
    resultado_texto.delete("1.0", tk.END)
    resultado_texto.insert(tk.END, resultado)

# Interface Tkinter
root = tk.Tk()
root.title("Resolutor de Matrizes")
root.geometry("600x500")
root.configure(bg="#f2f2f2")

tk.Label(root, text="Digite a matriz (linhas separadas por ENTER, colunas por espaço):", bg="#f2f2f2").pack()

entrada_matriz = tk.Text(root, height=7, width=60)
entrada_matriz.pack()

opcoes = tk.StringVar()
opcoes.set("Forma Escada (Gauss-Jordan)")
menu = tk.OptionMenu(root, opcoes,
                     "Forma Escada (Gauss-Jordan)",
                     "Inversa da Matriz",
                     "Verificar se é Invertível",
                     "Posto da Matriz",
                     "Resolver Sistema Linear")
menu.pack(pady=10)

botao = tk.Button(root, text="Executar Operação", command=executar_operacao, bg="#4caf50", fg="white")
botao.pack(pady=10)

tk.Label(root, text="Resultado:", bg="#f2f2f2").pack()
resultado_texto = tk.Text(root, height=10, width=60)
resultado_texto.pack()

root.mainloop()