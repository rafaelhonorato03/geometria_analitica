"""
Interface Tkinter para Geometria Analítica
Aplicação desktop para cálculos de matrizes e sistemas lineares
"""

import tkinter as tk
from tkinter import messagebox, simpledialog
import numpy as np
import sys
import os

# Adicionar o diretório src ao path para importar os módulos
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.matriz_operations import *

def parse_matrix(text):
    """
    Converte texto em matriz numpy.
    
    Args:
        text: Texto com a matriz
        
    Returns:
        Matriz numpy ou None se erro
    """
    try:
        matrix = [list(map(float, row.split())) for row in text.strip().split('\n')]
        return np.array(matrix)
    except:
        messagebox.showerror("Erro", "Formato inválido! Use espaço entre números e ENTER para nova linha.")
        return None

def executar_operacao():
    """
    Executa a operação selecionada na interface.
    """
    matriz_texto = entrada_matriz.get("1.0", tk.END)
    matriz = parse_matrix(matriz_texto)
    if matriz is None:
        return

    operacao = opcoes.get()
    resultado = ""

    if operacao == "Forma Escada (Gauss-Jordan)":
        resultado = forma_escada(matriz)
    elif operacao == "Inversa da Matriz":
        resultado = inversa_matriz(matriz)
    elif operacao == "Verificar se é Invertível":
        resultado = eh_invertivel(matriz)
        if resultado:
            resultado = "Sim. A matriz é invertível."
        else:
            resultado = "Não. A matriz NÃO é invertível."
    elif operacao == "Posto da Matriz":
        resultado = calcular_posto(matriz)
        resultado = f"O posto da matriz é {resultado}"
    elif operacao == "Resolver Sistema Linear":
        resultado = resolver_sistema(matriz)
    elif operacao == "Determinante da Matriz":
        resultado = determinante(matriz)
    elif operacao == "Transposta da Matriz":
        resultado = transposta(matriz)
    elif operacao == "Regra de Sarrus":
        resultado = regra_de_sarrus(matriz)

    if isinstance(resultado, np.ndarray):
        resultado = np.round(resultado, 2)
        resultado = "\n".join([" ".join(map(str, row)) for row in resultado])
    
    resultado_texto.delete("1.0", tk.END)
    resultado_texto.insert(tk.END, resultado)

def limpar_campos():
    """
    Limpa os campos de entrada e resultado.
    """
    entrada_matriz.delete("1.0", tk.END)
    resultado_texto.delete("1.0", tk.END)

def inserir_exemplo():
    """
    Insere um exemplo de matriz.
    """
    exemplo = "1 2 3\n0 1 4\n5 6 0"
    entrada_matriz.delete("1.0", tk.END)
    entrada_matriz.insert(tk.END, exemplo)

# Interface Tkinter
def criar_interface():
    """
    Cria a interface gráfica principal.
    """
    root = tk.Tk()
    root.title("Calculadora de Geometria Analítica")
    root.geometry("700x600")
    root.configure(bg="#f0f0f0")
    
    # Título
    titulo = tk.Label(root, text="🧮 Calculadora de Geometria Analítica", 
                     font=("Arial", 16, "bold"), bg="#f0f0f0")
    titulo.pack(pady=10)
    
    # Frame principal
    main_frame = tk.Frame(root, bg="#f0f0f0")
    main_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
    
    # Instruções
    instrucoes = tk.Label(main_frame, 
                         text="Digite a matriz (linhas separadas por ENTER, colunas por espaço):",
                         bg="#f0f0f0", font=("Arial", 10))
    instrucoes.pack()
    
    # Campo de entrada da matriz
    entrada_matriz = tk.Text(main_frame, height=8, width=60, font=("Courier", 10))
    entrada_matriz.pack(pady=5)
    
    # Frame para botões de ação
    botoes_frame = tk.Frame(main_frame, bg="#f0f0f0")
    botoes_frame.pack(pady=5)
    
    # Botão para inserir exemplo
    botao_exemplo = tk.Button(botoes_frame, text="Inserir Exemplo", 
                             command=inserir_exemplo, bg="#4CAF50", fg="white",
                             font=("Arial", 9))
    botao_exemplo.pack(side=tk.LEFT, padx=5)
    
    # Botão para limpar
    botao_limpar = tk.Button(botoes_frame, text="Limpar", 
                            command=limpar_campos, bg="#f44336", fg="white",
                            font=("Arial", 9))
    botao_limpar.pack(side=tk.LEFT, padx=5)
    
    # Seleção de operação
    opcoes = tk.StringVar()
    opcoes.set("Forma Escada (Gauss-Jordan)")
    
    operacoes = [
        "Forma Escada (Gauss-Jordan)",
        "Inversa da Matriz",
        "Verificar se é Invertível",
        "Posto da Matriz",
        "Resolver Sistema Linear",
        "Determinante da Matriz",
        "Transposta da Matriz",
        "Regra de Sarrus"
    ]
    
    menu = tk.OptionMenu(main_frame, opcoes, *operacoes)
    menu.config(font=("Arial", 10), bg="#2196F3", fg="white")
    menu.pack(pady=10)
    
    # Botão executar
    botao_executar = tk.Button(main_frame, text="Executar Operação", 
                              command=executar_operacao, bg="#2196F3", fg="white",
                              font=("Arial", 12, "bold"))
    botao_executar.pack(pady=10)
    
    # Label para resultado
    resultado_label = tk.Label(main_frame, text="Resultado:", 
                              bg="#f0f0f0", font=("Arial", 12, "bold"))
    resultado_label.pack()
    
    # Campo de resultado
    resultado_texto = tk.Text(main_frame, height=12, width=60, font=("Courier", 10))
    resultado_texto.pack(pady=5)
    
    # Scrollbar para o resultado
    scrollbar = tk.Scrollbar(main_frame, command=resultado_texto.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    resultado_texto.config(yscrollcommand=scrollbar.set)
    
    # Footer
    footer = tk.Label(root, text="Desenvolvido para o estudo de Geometria Analítica", 
                     bg="#f0f0f0", font=("Arial", 8))
    footer.pack(side=tk.BOTTOM, pady=5)
    
    return root, entrada_matriz, opcoes, resultado_texto

def main():
    """
    Função principal que inicia a aplicação.
    """
    root, entrada_matriz, opcoes, resultado_texto = criar_interface()
    
    # Tornar as variáveis globais para uso nas funções
    global entrada_matriz, opcoes, resultado_texto
    
    # Inserir exemplo inicial
    inserir_exemplo()
    
    # Iniciar o loop da interface
    root.mainloop()

if __name__ == "__main__":
    main() 