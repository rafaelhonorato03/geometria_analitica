import numpy as np
import matplotlib.pyplot as plt

def eliminacao_gauss(A, B):
    """
    Resolve um sistema linear Ax = B usando o método de eliminação de Gauss.
    
    :para A: Matriz dos coeficientes (numpy array).
    :para B: Vetor dos termos independentes (numpy array).
    :return: Solução do sistema (numpy array).
    """
    # Combinar A e B em uma matriz aumentada
    n = len(B)
    matriz_aumentada = np.hstack((A, B.reshape(-1, 1)))

    # Escalonamento
    for i in range(n):
        # Pivoteamento: garantir que o elemento da diagonal não seja zero
        if matriz_aumentada[i, i] == 0:
            for j in range(i + 1, n):
                if matriz_aumentada[j, i] != 0:
                    matriz_aumentada[[i, j]] = matriz_aumentada[[j, i]]
                    break
            else:
                raise ValueError("O sistema não possui solução única.")

        # Normalizar a linha atual
        matriz_aumentada[i] = matriz_aumentada[i] / matriz_aumentada[i, i]

        # Eliminar os elementos abaixo da diagonal
        for j in range(i + 1, n):
            matriz_aumentada[j] = matriz_aumentada[j] - matriz_aumentada[j, i] * matriz_aumentada[i]

    # Substituição regressiva
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = matriz_aumentada[i, -1] - np.sum(matriz_aumentada[i, i + 1:n] * x[i + 1:n])

    return x
    
# Definição das matrizes
A = np.array([[1, -1, 1, 2],
              [2, -3, 0, 1],
              [4,  7, -1, 2],
              [3,  1, 4, 7]])
B = np.array([-1, 3, 1, 4])

# Resolver o sistema pelo método de Gauss
solucao = eliminacao_gauss(A, B)

# Exibir a solução
print("Solução pelo método de Gauss:", solucao)