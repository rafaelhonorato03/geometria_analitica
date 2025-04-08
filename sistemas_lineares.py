# Resolutor de Matrizes e Sistemas Lineares
# Requer: numpy, sympy, streamlit (ou tkinter, opcional)

import numpy as np
import sympy as sp

# Funções principais

def forma_escada(A):
    return sp.Matrix(A).rref()

def inversa_matriz(A):
    try:
        return sp.Matrix(A).inv()
    except:
        return "Matriz não é invertível."

def eh_invertivel(A):
    return sp.Matrix(A).det() != 0

def produto_matrizes(A, B):
    try:
        return np.dot(A, B)
    except:
        return "Produto não definido para essas dimensões."

def resolver_sistema(A, b):
    A = sp.Matrix(A)
    b = sp.Matrix(b)
    try:
        sol = A.gauss_jordan_solve(b)
        return sol
    except:
        return "Sistema sem solução ou infinitas soluções."

def obter_posto(A):
    return sp.Matrix(A).rank()

# Exemplo de uso no terminal
if __name__ == '__main__':
    print("Bem-vindo ao Resolutor de Matrizes!")
    A = [[1, 2, 3], [2, 3, 5], [3, 4, 2]]
    b = [[1], [2], [3]]

    print("Matriz A:")
    print(sp.Matrix(A))

    print("Forma escada:")
    print(forma_escada(A))

    print("Inversa:")
    print(inversa_matriz(A))

    print("Posto da matriz A:")
    print(obter_posto(A))

    print("Sistema Ax = b:")
    print(resolver_sistema(A, b))
