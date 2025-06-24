"""
Operações básicas com matrizes
Módulo contendo funções para manipulação e cálculo de matrizes
"""

import numpy as np
import sympy as sp

def forma_escada(matriz):
    """
    Converte uma matriz para sua forma escada (Gauss-Jordan).
    
    Args:
        matriz: Matriz numpy array
        
    Returns:
        Matriz na forma escada
    """
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
        return np.round(m, 2)
    except Exception as e:
        return f"Erro: {str(e)}"

def inversa_matriz(matriz):
    """
    Calcula a inversa de uma matriz.
    
    Args:
        matriz: Matriz numpy array
        
    Returns:
        Matriz inversa ou mensagem de erro
    """
    try:
        return np.round(np.linalg.inv(matriz), 2)
    except:
        return "Matriz não é invertível."

def eh_invertivel(matriz):
    """
    Verifica se uma matriz é invertível.
    
    Args:
        matriz: Matriz numpy array
        
    Returns:
        True se invertível, False caso contrário
    """
    try:
        np.linalg.inv(matriz)
        return True
    except:
        return False

def calcular_posto(matriz):
    """
    Calcula o posto (rank) de uma matriz.
    
    Args:
        matriz: Matriz numpy array
        
    Returns:
        Posto da matriz
    """
    return np.linalg.matrix_rank(matriz)

def resolver_sistema(matriz_aumentada):
    """
    Resolve um sistema linear usando matriz aumentada.
    
    Args:
        matriz_aumentada: Matriz com termos independentes na última coluna
        
    Returns:
        Solução do sistema ou mensagem de erro
    """
    try:
        linhas, colunas = matriz_aumentada.shape
        if colunas != linhas + 1:
            return "A matriz deve ser aumentada (última coluna = termos independentes)."
        A = matriz_aumentada[:, :-1]
        b = matriz_aumentada[:, -1]
        x = np.linalg.solve(A, b)
        return np.round(x, 2)
    except Exception as e:
        return f"Erro ao resolver sistema: {str(e)}"

def regra_de_sarrus(matriz):
    """
    Calcula o determinante de uma matriz 3x3 usando a Regra de Sarrus.
    
    Args:
        matriz: Matriz 3x3 (numpy array)
        
    Returns:
        Determinante da matriz ou mensagem de erro
    """
    try:
        if matriz.shape != (3, 3):
            return "A Regra de Sarrus só pode ser aplicada a matrizes 3x3."
        
        # Regra de Sarrus
        det = (
            matriz[0, 0] * matriz[1, 1] * matriz[2, 2] +
            matriz[0, 1] * matriz[1, 2] * matriz[2, 0] +
            matriz[0, 2] * matriz[1, 0] * matriz[2, 1] -
            matriz[0, 2] * matriz[1, 1] * matriz[2, 0] -
            matriz[0, 0] * matriz[1, 2] * matriz[2, 1] -
            matriz[0, 1] * matriz[1, 0] * matriz[2, 2]
        )
        return np.round(det, 2)
    except Exception as e:
        return f"Erro ao calcular determinante: {str(e)}"

def determinante(matriz):
    """
    Calcula o determinante de uma matriz.
    
    Args:
        matriz: Matriz quadrada (numpy array)
        
    Returns:
        Determinante da matriz ou mensagem de erro
    """
    try:
        if matriz.shape[0] != matriz.shape[1]:
            return "O determinante só pode ser calculado para matrizes quadradas."
        
        det = np.linalg.det(matriz)
        return np.round(det, 2)
    except Exception as e:
        return f"Erro ao calcular o determinante: {str(e)}"

def transposta(matriz):
    """
    Calcula a matriz transposta.
    
    Args:
        matriz: Matriz (numpy array)
        
    Returns:
        Matriz transposta
    """
    try:
        return matriz.T
    except Exception as e:
        return f"Erro ao calcular a transposta: {str(e)}"

def produto_matrizes(A, B):
    """
    Calcula o produto de duas matrizes.
    
    Args:
        A: Primeira matriz
        B: Segunda matriz
        
    Returns:
        Produto das matrizes ou mensagem de erro
    """
    try:
        return np.dot(A, B)
    except:
        return "Produto não definido para essas dimensões."

def verificar_tipo_matriz(matriz):
    """
    Verifica o tipo de uma matriz.
    
    Args:
        matriz: Matriz numpy array
        
    Returns:
        Dicionário com informações sobre o tipo da matriz
    """
    resultado = {}
    
    # Verificar se é quadrada
    resultado['quadrada'] = matriz.shape[0] == matriz.shape[1]
    
    # Verificar se é nula
    resultado['nula'] = np.all(matriz == 0)
    
    # Verificar se é identidade
    if resultado['quadrada']:
        resultado['identidade'] = np.allclose(matriz, np.eye(matriz.shape[0]))
        resultado['simetrica'] = np.allclose(matriz, matriz.T)
    else:
        resultado['identidade'] = False
        resultado['simetrica'] = False
    
    return resultado 