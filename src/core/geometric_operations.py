"""
Operações geométricas
Módulo contendo funções para cálculos de retas, planos e geometria analítica
"""

import numpy as np

def equacao_parametrica_reta(ponto, vetor_direcao):
    """
    Retorna a equação paramétrica da reta definida por um ponto e um vetor direção.
    
    Args:
        ponto: Ponto da reta (numpy array)
        vetor_direcao: Vetor direção da reta (numpy array)
        
    Returns:
        String com a equação paramétrica
    """
    try:
        return f"r(t) = {ponto} + t * {vetor_direcao}"
    except Exception as e:
        return f"Erro ao calcular a reta: {str(e)}"

def equacao_simetrica_reta(ponto, vetor_direcao):
    """
    Retorna a equação simétrica da reta.
    
    Args:
        ponto: Ponto da reta (numpy array)
        vetor_direcao: Vetor direção da reta (numpy array)
        
    Returns:
        String com a equação simétrica
    """
    try:
        x0, y0, z0 = ponto
        a, b, c = vetor_direcao
        
        if a != 0 and b != 0 and c != 0:
            return f"(x - {x0})/{a} = (y - {y0})/{b} = (z - {z0})/{c}"
        else:
            return "Equação simétrica não definida (algum componente do vetor é zero)"
    except Exception as e:
        return f"Erro ao calcular equação simétrica: {str(e)}"

def angulo_entre_retas(vetor_direcao1, vetor_direcao2):
    """
    Calcula o ângulo entre duas retas usando seus vetores direção.
    
    Args:
        vetor_direcao1: Vetor direção da primeira reta (numpy array)
        vetor_direcao2: Vetor direção da segunda reta (numpy array)
        
    Returns:
        Ângulo em graus entre as retas
    """
    try:
        # Normalizar os vetores
        v1_norm = vetor_direcao1 / np.linalg.norm(vetor_direcao1)
        v2_norm = vetor_direcao2 / np.linalg.norm(vetor_direcao2)
        
        # Calcular o produto escalar
        produto_escalar = np.dot(v1_norm, v2_norm)
        
        # Garantir que o valor esteja no intervalo válido
        produto_escalar = np.clip(produto_escalar, -1.0, 1.0)
        
        # Calcular o ângulo
        angulo = np.degrees(np.arccos(abs(produto_escalar)))
        
        return angulo
    except Exception as e:
        return f"Erro ao calcular ângulo entre retas: {str(e)}"

def distancia_entre_duas_retas(ponto1, vetor_direcao1, ponto2, vetor_direcao2):
    """
    Calcula a distância entre duas retas no espaço.
    
    Args:
        ponto1: Ponto da primeira reta (numpy array)
        vetor_direcao1: Vetor direção da primeira reta (numpy array)
        ponto2: Ponto da segunda reta (numpy array)
        vetor_direcao2: Vetor direção da segunda reta (numpy array)
        
    Returns:
        Distância entre as retas
    """
    try:
        # Vetor entre os pontos
        vetor_pontos = ponto2 - ponto1
        
        # Produto vetorial dos vetores direção
        produto_vetorial = np.cross(vetor_direcao1, vetor_direcao2)
        
        # Norma do produto vetorial
        norma_produto_vetorial = np.linalg.norm(produto_vetorial)
        
        if norma_produto_vetorial == 0:
            return "As retas são paralelas ou coincidentes"
        
        # Distância
        distancia = abs(np.dot(vetor_pontos, produto_vetorial)) / norma_produto_vetorial
        
        return distancia
    except Exception as e:
        return f"Erro ao calcular distância entre retas: {str(e)}"

def equacao_parametrica_plano(ponto, vetor1, vetor2):
    """
    Retorna a equação paramétrica do plano definido por um ponto e dois vetores.
    
    Args:
        ponto: Ponto do plano (numpy array)
        vetor1: Primeiro vetor direção (numpy array)
        vetor2: Segundo vetor direção (numpy array)
        
    Returns:
        String com a equação paramétrica
    """
    try:
        return f"π(s,t) = {ponto} + s * {vetor1} + t * {vetor2}"
    except Exception as e:
        return f"Erro ao calcular equação paramétrica do plano: {str(e)}"

def equacao_cartesiana_plano(ponto, vetor_normal):
    """
    Retorna a equação cartesiana do plano definido por um ponto e um vetor normal.
    
    Args:
        ponto: Ponto do plano (numpy array)
        vetor_normal: Vetor normal ao plano (numpy array)
        
    Returns:
        String com a equação cartesiana
    """
    try:
        x0, y0, z0 = ponto
        a, b, c = vetor_normal
        
        # Calcular d
        d = -(a * x0 + b * y0 + c * z0)
        
        return f"{a}x + {b}y + {c}z + {d} = 0"
    except Exception as e:
        return f"Erro ao calcular equação cartesiana do plano: {str(e)}"

def angulo_entre_planos(vetor_normal1, vetor_normal2):
    """
    Calcula o ângulo entre dois planos usando seus vetores normais.
    
    Args:
        vetor_normal1: Vetor normal do primeiro plano (numpy array)
        vetor_normal2: Vetor normal do segundo plano (numpy array)
        
    Returns:
        Ângulo em graus entre os planos
    """
    try:
        # Normalizar os vetores
        n1_norm = vetor_normal1 / np.linalg.norm(vetor_normal1)
        n2_norm = vetor_normal2 / np.linalg.norm(vetor_normal2)
        
        # Calcular o produto escalar
        produto_escalar = np.dot(n1_norm, n2_norm)
        
        # Garantir que o valor esteja no intervalo válido
        produto_escalar = np.clip(produto_escalar, -1.0, 1.0)
        
        # Calcular o ângulo
        angulo = np.degrees(np.arccos(abs(produto_escalar)))
        
        return angulo
    except Exception as e:
        return f"Erro ao calcular ângulo entre planos: {str(e)}"

def intersecao_tres_planos(coef1, coef2, coef3, termos_independentes):
    """
    Calcula a interseção entre três planos.
    
    Args:
        coef1: Coeficientes do primeiro plano [a1, b1, c1]
        coef2: Coeficientes do segundo plano [a2, b2, c2]
        coef3: Coeficientes do terceiro plano [a3, b3, c3]
        termos_independentes: Termos independentes [d1, d2, d3]
        
    Returns:
        Ponto de interseção ou mensagem de erro
    """
    try:
        # Matriz dos coeficientes
        A = np.array([coef1, coef2, coef3])
        
        # Vetor dos termos independentes
        b = np.array(termos_independentes)
        
        # Resolver o sistema
        solucao = np.linalg.solve(A, b)
        
        return np.round(solucao, 2)
    except np.linalg.LinAlgError:
        return "Os planos não se intersectam em um único ponto"
    except Exception as e:
        return f"Erro ao calcular interseção: {str(e)}"

def distancia_ponto_reta(ponto, ponto_reta, vetor_direcao):
    """
    Calcula a distância de um ponto a uma reta.
    
    Args:
        ponto: Ponto (numpy array)
        ponto_reta: Ponto da reta (numpy array)
        vetor_direcao: Vetor direção da reta (numpy array)
        
    Returns:
        Distância do ponto à reta
    """
    try:
        # Vetor do ponto da reta ao ponto
        vetor_ponto = ponto - ponto_reta
        
        # Produto vetorial
        produto_vetorial = np.cross(vetor_ponto, vetor_direcao)
        
        # Distância
        distancia = np.linalg.norm(produto_vetorial) / np.linalg.norm(vetor_direcao)
        
        return distancia
    except Exception as e:
        return f"Erro ao calcular distância ponto-reta: {str(e)}"

def distancia_ponto_plano(ponto, ponto_plano, vetor_normal):
    """
    Calcula a distância de um ponto a um plano.
    
    Args:
        ponto: Ponto (numpy array)
        ponto_plano: Ponto do plano (numpy array)
        vetor_normal: Vetor normal ao plano (numpy array)
        
    Returns:
        Distância do ponto ao plano
    """
    try:
        # Vetor do ponto do plano ao ponto
        vetor_ponto = ponto - ponto_plano
        
        # Distância
        distancia = abs(np.dot(vetor_ponto, vetor_normal)) / np.linalg.norm(vetor_normal)
        
        return distancia
    except Exception as e:
        return f"Erro ao calcular distância ponto-plano: {str(e)}"

def sao_paralelas_retas(vetor_direcao1, vetor_direcao2):
    """
    Verifica se duas retas são paralelas.
    
    Args:
        vetor_direcao1: Vetor direção da primeira reta (numpy array)
        vetor_direcao2: Vetor direção da segunda reta (numpy array)
        
    Returns:
        True se paralelas, False caso contrário
    """
    produto_vetorial = np.cross(vetor_direcao1, vetor_direcao2)
    return np.allclose(produto_vetorial, 0)

def sao_perpendiculares_retas(vetor_direcao1, vetor_direcao2):
    """
    Verifica se duas retas são perpendiculares.
    
    Args:
        vetor_direcao1: Vetor direção da primeira reta (numpy array)
        vetor_direcao2: Vetor direção da segunda reta (numpy array)
        
    Returns:
        True se perpendiculares, False caso contrário
    """
    return np.isclose(np.dot(vetor_direcao1, vetor_direcao2), 0) 