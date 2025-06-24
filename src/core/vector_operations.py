"""
Operações com vetores
Módulo contendo funções para cálculos vetoriais em geometria analítica
"""

import numpy as np

def soma_vetores(vetor1, vetor2):
    """
    Calcula a soma de dois vetores.
    
    Args:
        vetor1: Primeiro vetor (numpy array)
        vetor2: Segundo vetor (numpy array)
        
    Returns:
        Soma dos vetores
    """
    return vetor1 + vetor2

def multiplicacao_escalar(vetor, escalar):
    """
    Multiplica um vetor por um escalar.
    
    Args:
        vetor: Vetor (numpy array)
        escalar: Número escalar
        
    Returns:
        Vetor multiplicado pelo escalar
    """
    return escalar * vetor

def produto_escalar(vetor1, vetor2):
    """
    Calcula o produto escalar entre dois vetores.
    
    Args:
        vetor1: Primeiro vetor (numpy array)
        vetor2: Segundo vetor (numpy array)
        
    Returns:
        Produto escalar (escalar)
    """
    return np.dot(vetor1, vetor2)

def produto_vetorial(vetor1, vetor2):
    """
    Calcula o produto vetorial entre dois vetores.
    
    Args:
        vetor1: Primeiro vetor (numpy array)
        vetor2: Segundo vetor (numpy array)
        
    Returns:
        Produto vetorial (vetor)
    """
    return np.cross(vetor1, vetor2)

def produto_misto(vetor1, vetor2, vetor3):
    """
    Calcula o produto misto de três vetores no espaço 3D.
    
    Args:
        vetor1: Primeiro vetor (numpy array)
        vetor2: Segundo vetor (numpy array)
        vetor3: Terceiro vetor (numpy array)
        
    Returns:
        Produto misto (escalar)
    """
    try:
        matriz = np.array([vetor1, vetor2, vetor3])
        return np.linalg.det(matriz)
    except Exception as e:
        return f"Erro ao calcular produto misto: {str(e)}"

def angulo_entre_vetores(vetor1, vetor2):
    """
    Calcula o ângulo (em graus) entre dois vetores.
    
    Args:
        vetor1: Primeiro vetor (numpy array)
        vetor2: Segundo vetor (numpy array)
        
    Returns:
        Ângulo em graus entre os vetores
    """
    try:
        # Produto escalar
        produto_escalar = np.dot(vetor1, vetor2)
        
        # Normas dos vetores
        norma_vetor1 = np.linalg.norm(vetor1)
        norma_vetor2 = np.linalg.norm(vetor2)
        
        # Cálculo do cosseno do ângulo
        cos_theta = produto_escalar / (norma_vetor1 * norma_vetor2)
        
        # Garantir que o valor esteja no intervalo válido para arccos
        cos_theta = np.clip(cos_theta, -1.0, 1.0)
        
        # Cálculo do ângulo em radianos e conversão para graus
        angulo = np.degrees(np.arccos(cos_theta))
        return angulo
    except Exception as e:
        return f"Erro ao calcular o ângulo: {str(e)}"

def norma_vetor(vetor):
    """
    Calcula a norma (módulo) de um vetor.
    
    Args:
        vetor: Vetor (numpy array)
        
    Returns:
        Norma do vetor
    """
    return np.linalg.norm(vetor)

def vetor_unitario(vetor):
    """
    Calcula o vetor unitário (versor) de um vetor.
    
    Args:
        vetor: Vetor (numpy array)
        
    Returns:
        Vetor unitário
    """
    norma = np.linalg.norm(vetor)
    if norma == 0:
        return vetor
    return vetor / norma

def distancia_entre_pontos(ponto1, ponto2):
    """
    Calcula a distância entre dois pontos no espaço.
    
    Args:
        ponto1: Primeiro ponto (numpy array)
        ponto2: Segundo ponto (numpy array)
        
    Returns:
        Distância entre os pontos
    """
    return np.linalg.norm(ponto2 - ponto1)

def projecao_vetorial(vetor1, vetor2):
    """
    Calcula a projeção vetorial de vetor1 sobre vetor2.
    
    Args:
        vetor1: Vetor a ser projetado (numpy array)
        vetor2: Vetor sobre o qual projetar (numpy array)
        
    Returns:
        Projeção vetorial
    """
    try:
        produto_escalar = np.dot(vetor1, vetor2)
        norma_vetor2_quadrado = np.dot(vetor2, vetor2)
        return (produto_escalar / norma_vetor2_quadrado) * vetor2
    except Exception as e:
        return f"Erro ao calcular projeção: {str(e)}"

def sao_ortogonais(vetor1, vetor2):
    """
    Verifica se dois vetores são ortogonais.
    
    Args:
        vetor1: Primeiro vetor (numpy array)
        vetor2: Segundo vetor (numpy array)
        
    Returns:
        True se ortogonais, False caso contrário
    """
    return np.isclose(np.dot(vetor1, vetor2), 0)

def sao_paralelos(vetor1, vetor2):
    """
    Verifica se dois vetores são paralelos.
    
    Args:
        vetor1: Primeiro vetor (numpy array)
        vetor2: Segundo vetor (numpy array)
        
    Returns:
        True se paralelos, False caso contrário
    """
    produto_vetorial = np.cross(vetor1, vetor2)
    return np.allclose(produto_vetorial, 0) 