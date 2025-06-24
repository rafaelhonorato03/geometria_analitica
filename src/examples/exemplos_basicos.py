"""
Exemplos básicos de uso
Demonstrações práticas das funcionalidades do sistema
"""

import numpy as np
import sys
import os

# Adicionar o diretório src ao path para importar os módulos
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.matriz_operations import *
from core.vector_operations import *
from core.geometric_operations import *
from visualization.plotting import *

def exemplo_operacoes_matrizes():
    """
    Demonstra operações básicas com matrizes.
    """
    print("=== EXEMPLOS DE OPERAÇÕES COM MATRIZES ===\n")
    
    # Exemplo 1: Matriz 3x3
    A = np.array([[2, -1, 3], [0, 1, 4], [5, 6, 0]])
    print("Matriz A:")
    print(A)
    print()
    
    # Determinante
    det = determinante(A)
    print(f"Determinante de A: {det}")
    
    # Regra de Sarrus
    sarrus = regra_de_sarrus(A)
    print(f"Regra de Sarrus: {sarrus}")
    
    # Transposta
    trans = transposta(A)
    print("Transposta de A:")
    print(trans)
    
    # Forma escada
    escada = forma_escada(A)
    print("Forma escada de A:")
    print(escada)
    
    # Verificar se é invertível
    invertivel = eh_invertivel(A)
    print(f"É invertível: {invertivel}")
    
    if invertivel:
        inv = inversa_matriz(A)
        print("Inversa de A:")
        print(inv)
    
    # Posto
    posto = calcular_posto(A)
    print(f"Posto de A: {posto}")
    
    print("\n" + "="*50 + "\n")

def exemplo_sistema_linear():
    """
    Demonstra resolução de sistema linear.
    """
    print("=== EXEMPLO DE SISTEMA LINEAR ===\n")
    
    # Sistema: 2x - y + 3z = 8
    #          -3x - y + 2z = -11
    #          -2x + y + 2z = -3
    
    matriz_aumentada = np.array([
        [2, -1, 3, 8],
        [-3, -1, 2, -11],
        [-2, 1, 2, -3]
    ])
    
    print("Matriz aumentada do sistema:")
    print(matriz_aumentada)
    print()
    
    solucao = resolver_sistema(matriz_aumentada)
    print(f"Solução do sistema: {solucao}")
    
    print("\n" + "="*50 + "\n")

def exemplo_operacoes_vetores():
    """
    Demonstra operações com vetores.
    """
    print("=== EXEMPLOS DE OPERAÇÕES COM VETORES ===\n")
    
    # Vetores de exemplo
    u = np.array([1, 1, 0])
    v = np.array([-1, 1, 0])
    w = np.array([0, 0, 1])
    
    print(f"Vetor u: {u}")
    print(f"Vetor v: {v}")
    print(f"Vetor w: {w}")
    print()
    
    # Soma de vetores
    soma = soma_vetores(u, v)
    print(f"u + v = {soma}")
    
    # Multiplicação por escalar
    mult = multiplicacao_escalar(u, 3)
    print(f"3 * u = {mult}")
    
    # Produto escalar
    prod_escalar = produto_escalar(u, v)
    print(f"u · v = {prod_escalar}")
    
    # Produto vetorial
    prod_vetorial = produto_vetorial(u, v)
    print(f"u × v = {prod_vetorial}")
    
    # Produto misto
    prod_misto = produto_misto(u, v, w)
    print(f"[u, v, w] = {prod_misto}")
    
    # Ângulo entre vetores
    angulo = angulo_entre_vetores(u, v)
    print(f"Ângulo entre u e v: {angulo:.2f}°")
    
    # Norma dos vetores
    norma_u = norma_vetor(u)
    norma_v = norma_vetor(v)
    print(f"||u|| = {norma_u:.2f}")
    print(f"||v|| = {norma_v:.2f}")
    
    # Vetores unitários
    u_unit = vetor_unitario(u)
    v_unit = vetor_unitario(v)
    print(f"Vetor unitário de u: {u_unit}")
    print(f"Vetor unitário de v: {v_unit}")
    
    # Verificações
    ortogonais = sao_ortogonais(u, v)
    paralelos = sao_paralelos(u, v)
    print(f"u e v são ortogonais: {ortogonais}")
    print(f"u e v são paralelos: {paralelos}")
    
    print("\n" + "="*50 + "\n")

def exemplo_geometria_analitica():
    """
    Demonstra operações de geometria analítica.
    """
    print("=== EXEMPLOS DE GEOMETRIA ANALÍTICA ===\n")
    
    # Pontos e vetores para retas
    ponto1 = np.array([0, 0, 0])
    vetor1 = np.array([1, 0, 0])
    ponto2 = np.array([0, 0, 0])
    vetor2 = np.array([0, 1, 0])
    
    print("Reta 1: ponto (0,0,0), vetor (1,0,0)")
    print("Reta 2: ponto (0,0,0), vetor (0,1,0)")
    print()
    
    # Equação paramétrica
    eq_param = equacao_parametrica_reta(ponto1, vetor1)
    print(f"Equação paramétrica da reta 1: {eq_param}")
    
    # Equação simétrica
    eq_sim = equacao_simetrica_reta(ponto1, vetor1)
    print(f"Equação simétrica da reta 1: {eq_sim}")
    
    # Ângulo entre retas
    angulo_retas = angulo_entre_retas(vetor1, vetor2)
    print(f"Ângulo entre as retas: {angulo_retas:.2f}°")
    
    # Distância entre retas
    dist_retas = distancia_entre_duas_retas(ponto1, vetor1, ponto2, vetor2)
    print(f"Distância entre as retas: {dist_retas}")
    
    # Verificações
    paralelas = sao_paralelas_retas(vetor1, vetor2)
    perpendiculares = sao_perpendiculares_retas(vetor1, vetor2)
    print(f"As retas são paralelas: {paralelas}")
    print(f"As retas são perpendiculares: {perpendiculares}")
    
    print("\n--- PLANOS ---\n")
    
    # Plano
    ponto_plano = np.array([0, 0, 0])
    vetor_normal = np.array([1, 1, 1])
    
    # Equação paramétrica do plano
    eq_param_plano = equacao_parametrica_plano(ponto_plano, np.array([1, 0, 0]), np.array([0, 1, 0]))
    print(f"Equação paramétrica do plano: {eq_param_plano}")
    
    # Equação cartesiana do plano
    eq_cart_plano = equacao_cartesiana_plano(ponto_plano, vetor_normal)
    print(f"Equação cartesiana do plano: {eq_cart_plano}")
    
    print("\n" + "="*50 + "\n")

def exemplo_visualizacao():
    """
    Demonstra as funções de visualização.
    """
    print("=== EXEMPLOS DE VISUALIZAÇÃO ===\n")
    
    print("Gerando gráficos...")
    
    # Elipse
    plotar_elipse(3, 2, -2, 1, title="Exemplo de Elipse", show=False)
    
    # Parábola
    plotar_parabola(2, -2, 1, title="Exemplo de Parábola", show=False)
    
    # Curva polar
    def r_func(theta):
        return np.cos(5 * theta)
    
    plotar_curva_polar(r_func, title="Exemplo de Curva Polar", show=False)
    
    # Círculo
    plotar_circulo(2, 0, 0, title="Exemplo de Círculo", show=False)
    
    # Vetores
    vetores = [np.array([1, 1]), np.array([-1, 1]), np.array([0, 2])]
    plotar_vetores(vetores, title="Exemplo de Vetores", show=False)
    
    print("Gráficos gerados com sucesso!")
    print("Use as funções de plotagem para visualizar as curvas.")
    
    print("\n" + "="*50 + "\n")

def main():
    """
    Função principal que executa todos os exemplos.
    """
    print("🧮 EXEMPLOS DE GEOMETRIA ANALÍTICA COM PYTHON\n")
    print("Este script demonstra as principais funcionalidades do sistema.\n")
    
    try:
        exemplo_operacoes_matrizes()
        exemplo_sistema_linear()
        exemplo_operacoes_vetores()
        exemplo_geometria_analitica()
        exemplo_visualizacao()
        
        print("✅ Todos os exemplos foram executados com sucesso!")
        print("\nPara usar as interfaces gráficas:")
        print("- Interface web: streamlit run src/interfaces/streamlit_app.py")
        print("- Interface desktop: python src/interfaces/tkinter_app.py")
        
    except Exception as e:
        print(f"❌ Erro ao executar exemplos: {str(e)}")

if __name__ == "__main__":
    main() 