"""
Funções de visualização gráfica
Módulo contendo funções para plotagem de curvas e gráficos em geometria analítica
"""

import numpy as np
import matplotlib.pyplot as plt

def plotar_elipse(a, b, x0=0, y0=0, t_range=None, color='blue', title='Elipse', show=True):
    """
    Plota uma elipse com parâmetros dados.
    
    Args:
        a: Semi-eixo maior
        b: Semi-eixo menor
        x0: Coordenada x do centro
        y0: Coordenada y do centro
        t_range: Range do parâmetro t (padrão: [-2π, 2π])
        color: Cor da curva
        title: Título do gráfico
        show: Se deve mostrar o gráfico
        
    Returns:
        Figura matplotlib
    """
    if t_range is None:
        t_range = [-2*np.pi, 2*np.pi]
    
    t = np.linspace(t_range[0], t_range[1], 100)
    
    # Equações paramétricas
    x = a * np.cos(t) + x0
    y = b * np.sin(t) + y0
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, color=color, label='Elipse')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    
    if show:
        plt.show()
    
    return plt.gcf()

def plotar_parabola(p, x0=0, y0=0, t_range=None, color='red', title='Parábola', show=True):
    """
    Plota uma parábola com parâmetro dado.
    
    Args:
        p: Parâmetro da parábola
        x0: Coordenada x do vértice
        y0: Coordenada y do vértice
        t_range: Range do parâmetro t (padrão: [-4, 4])
        color: Cor da curva
        title: Título do gráfico
        show: Se deve mostrar o gráfico
        
    Returns:
        Figura matplotlib
    """
    if t_range is None:
        t_range = [-4, 4]
    
    t = np.linspace(t_range[0], t_range[1], 100)
    
    # Equações paramétricas
    x = t + x0
    y = (1 / (4 * p)) * t**2 + y0
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, color=color, label='Parábola')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    
    if show:
        plt.show()
    
    return plt.gcf()

def plotar_curva_polar(r_func, theta_range=None, color='green', title='Curva Polar', show=True):
    """
    Plota uma curva polar.
    
    Args:
        r_func: Função r(θ) que define a curva
        theta_range: Range do ângulo θ (padrão: [0, 2π])
        color: Cor da curva
        title: Título do gráfico
        show: Se deve mostrar o gráfico
        
    Returns:
        Figura matplotlib
    """
    if theta_range is None:
        theta_range = [0, 2*np.pi]
    
    theta = np.linspace(theta_range[0], theta_range[1], 500)
    r = r_func(theta)
    
    # Conversão para coordenadas cartesianas
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, color=color, label='Curva Polar')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    
    if show:
        plt.show()
    
    return plt.gcf()

def plotar_hiperbole(a, b, x0=0, y0=0, t_range=None, color='purple', title='Hipérbole', show=True):
    """
    Plota uma hipérbole.
    
    Args:
        a: Semi-eixo real
        b: Semi-eixo imaginário
        x0: Coordenada x do centro
        y0: Coordenada y do centro
        t_range: Range do parâmetro t (padrão: [-2, 2])
        color: Cor da curva
        title: Título do gráfico
        show: Se deve mostrar o gráfico
        
    Returns:
        Figura matplotlib
    """
    if t_range is None:
        t_range = [-2, 2]
    
    t = np.linspace(t_range[0], t_range[1], 100)
    
    # Equações paramétricas
    x = a * np.cosh(t) + x0
    y = b * np.sinh(t) + y0
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, color=color, label='Hipérbole')
    plt.plot(-x, y, color=color)  # Ramo negativo
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    
    if show:
        plt.show()
    
    return plt.gcf()

def plotar_circulo(raio, x0=0, y0=0, color='orange', title='Círculo', show=True):
    """
    Plota um círculo.
    
    Args:
        raio: Raio do círculo
        x0: Coordenada x do centro
        y0: Coordenada y do centro
        color: Cor da curva
        title: Título do gráfico
        show: Se deve mostrar o gráfico
        
    Returns:
        Figura matplotlib
    """
    t = np.linspace(0, 2*np.pi, 100)
    
    # Equações paramétricas
    x = raio * np.cos(t) + x0
    y = raio * np.sin(t) + y0
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, color=color, label='Círculo')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    
    if show:
        plt.show()
    
    return plt.gcf()

def plotar_reta(ponto, vetor_direcao, t_range=None, color='black', title='Reta', show=True):
    """
    Plota uma reta definida por um ponto e um vetor direção.
    
    Args:
        ponto: Ponto da reta [x, y]
        vetor_direcao: Vetor direção [dx, dy]
        t_range: Range do parâmetro t (padrão: [-5, 5])
        color: Cor da reta
        title: Título do gráfico
        show: Se deve mostrar o gráfico
        
    Returns:
        Figura matplotlib
    """
    if t_range is None:
        t_range = [-5, 5]
    
    t = np.linspace(t_range[0], t_range[1], 100)
    
    # Equações paramétricas
    x = ponto[0] + vetor_direcao[0] * t
    y = ponto[1] + vetor_direcao[1] * t
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, color=color, label='Reta')
    plt.plot(ponto[0], ponto[1], 'ro', markersize=8, label='Ponto')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    
    if show:
        plt.show()
    
    return plt.gcf()

def plotar_vetores(vetores, origens=None, colors=None, title='Vetores', show=True):
    """
    Plota vetores no plano.
    
    Args:
        vetores: Lista de vetores [[x1, y1], [x2, y2], ...]
        origens: Lista de pontos de origem (padrão: origem)
        colors: Lista de cores para cada vetor
        title: Título do gráfico
        show: Se deve mostrar o gráfico
        
    Returns:
        Figura matplotlib
    """
    if origens is None:
        origens = [[0, 0]] * len(vetores)
    
    if colors is None:
        colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'pink', 'gray']
    
    plt.figure(figsize=(8, 6))
    
    for i, (vetor, origem) in enumerate(zip(vetores, origens)):
        color = colors[i % len(colors)]
        plt.quiver(origem[0], origem[1], vetor[0], vetor[1], 
                  angles='xy', scale_units='xy', scale=1, color=color,
                  label=f'Vetor {i+1}')
    
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    
    if show:
        plt.show()
    
    return plt.gcf()

def plotar_multiplas_curvas(curvas, title='Múltiplas Curvas', show=True):
    """
    Plota múltiplas curvas no mesmo gráfico.
    
    Args:
        curvas: Lista de dicionários com dados das curvas
               [{'x': x1, 'y': y1, 'label': 'label1', 'color': 'color1'}, ...]
        title: Título do gráfico
        show: Se deve mostrar o gráfico
        
    Returns:
        Figura matplotlib
    """
    plt.figure(figsize=(10, 8))
    
    for curva in curvas:
        plt.plot(curva['x'], curva['y'], 
                color=curva.get('color', 'blue'),
                label=curva.get('label', 'Curva'),
                linewidth=curva.get('linewidth', 2))
    
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    
    if show:
        plt.show()
    
    return plt.gcf()

def configurar_grafico(title='Gráfico', xlabel='x', ylabel='y', grid=True, equal_axis=True):
    """
    Configura um gráfico com parâmetros padrão.
    
    Args:
        title: Título do gráfico
        xlabel: Rótulo do eixo x
        ylabel: Rótulo do eixo y
        grid: Se deve mostrar grade
        equal_axis: Se deve usar eixos iguais
        
    Returns:
        None
    """
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if grid:
        plt.grid(True, alpha=0.3)
    if equal_axis:
        plt.axis('equal')
    plt.legend() 