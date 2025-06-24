"""
Pacote de Geometria Analítica
Sistema completo para cálculos de geometria analítica e álgebra linear
"""

__version__ = "1.0.0"
__author__ = "Rafael Honorato"
__description__ = "Sistema de Geometria Analítica com Python"

# Importações principais para facilitar o uso
from .core.matriz_operations import *
from .core.vector_operations import *
from .core.geometric_operations import *
from .visualization.plotting import *

__all__ = [
    # Matriz operations
    'forma_escada', 'inversa_matriz', 'eh_invertivel', 'calcular_posto',
    'resolver_sistema', 'regra_de_sarrus', 'determinante', 'transposta',
    'produto_matrizes', 'verificar_tipo_matriz',
    
    # Vector operations
    'soma_vetores', 'multiplicacao_escalar', 'produto_escalar', 'produto_vetorial',
    'produto_misto', 'angulo_entre_vetores', 'norma_vetor', 'vetor_unitario',
    'distancia_entre_pontos', 'projecao_vetorial', 'sao_ortogonais', 'sao_paralelos',
    
    # Geometric operations
    'equacao_parametrica_reta', 'equacao_simetrica_reta', 'angulo_entre_retas',
    'distancia_entre_duas_retas', 'equacao_parametrica_plano', 'equacao_cartesiana_plano',
    'angulo_entre_planos', 'intersecao_tres_planos', 'distancia_ponto_reta',
    'distancia_ponto_plano', 'sao_paralelas_retas', 'sao_perpendiculares_retas',
    
    # Visualization
    'plotar_elipse', 'plotar_parabola', 'plotar_curva_polar', 'plotar_hiperbole',
    'plotar_circulo', 'plotar_reta', 'plotar_vetores', 'plotar_multiplas_curvas',
    'configurar_grafico'
] 