import numpy as np
import matplotlib.pyplot as plt

# Declarando vetor u
vetor_u = np.array([1, -2, 0])

# Declarando vetor v
vetor_v = np.array([0, 2, 2])

# Declarando o vetor w
vetor_w = np.array([1, 2, -1])

# Soma de vetores
soma_vetores = vetor_u + vetor_v
print("Soma dos vetores u e v: ", soma_vetores)

# Multiplicaçao de vetor com escalar
multiplicacao_escalar = 7 * vetor_u
print("Multiplicação do vetor u por 7: ", multiplicacao_escalar)

# Produto escalar de u com v
produto_escalar = np.dot(vetor_u, vetor_v)
print("Produto escalar de u e v: ", produto_escalar)

# Produto vetorial de u com v
produto_vetorial = np.cross(vetor_u, vetor_v)
print("Produto vetorial de u e v: ", produto_vetorial)

# Produto misto de u, v e w
produto_misto = np.linalg.det([
    vetor_u, vetor_v, vetor_w])
print("Produto misto de u, v e w: ", produto_misto)

# Fazendo gráficos de vetores em python, grafico 1
a, b, x0, y0 = 3, 2, -2, 1

#Variações do parâmetro t
t = np.linspace(-1, 2 * np.pi, 100)

# Equações paramétricas
x = a * np.cos(t) + x0
y = b * np.sin(t) + y0

# Fazendo o gráfico
plt.plot(x, y, label='Elipse')
plt.title('Gráfico da elipse')

# Adicionar legenda
plt.legend()

# Variação dos eixos
plt.axis([-6, 2, -2, 5])

# Mostrar o gráfico
plt.show()

# Fazendo gráficos de vetores em python, grafico 2
a, b, x0, y0 = 3, 2, -2, 1

#Variações do parâmetro t
t = np.linspace(-1, 1, 100)

# Equações paramétricas
x = a * np.cos(t) + x0
y = b * np.sin(t) + y0

# Fazendo o gráfico
plt.plot(x, y, color = 'red')
plt.plot(-x, y, color = 'red')
plt.title('Gráfico da elipse')

# Adicionar legenda
plt.legend()

# Variação dos eixos
plt.axis([-5, 5, -2, 4])

# Mostrar o gráfico
plt.show()

# Fazendo gráficos de vetores em python, grafico de uma parabola
p, x0, y0 = 2, -2, 1

#Variações do parâmetro t
t = np.linspace(-4, 4, 100)

# Equações paramétricas
x = t + x0
y = ( 1 / (4 * p) ) *t ** 2

# Fazendo o gráfico
plt.plot(x, y)

# Variação dos eixos
plt.axis([-7, 3, -1, 3])

# Mostrar o gráfico
plt.show()


# Construindo gráficos polares

# Constante
n = 20

# Variação do paramettro t
t = np.linspace(0, 2 * np.pi, 500)

# Paramétricas em coordenadas polares
theta = t
r = np.cos(n * t)

# Paramétricas em coordenadas cartesianas
x = r * np.cos(theta)
y = r * np.sin(theta)

# Fazendo o gráfico
plt.plot(x, y)
plt.show()

# Resolvendo sistemas de equações lineares
A = np.array([[2, -1], [-1, 2]])
B = np.array([3, 0])

# Resolver o sistema
solucao = np.linalg.solve(A, B)

# Exibir a solução
print(f"Solução: x = {solucao[0]}, y = {solucao[1]}")

# Plotar a solução no gráfico
plt.scatter(solucao[0], solucao[1], color='red', label='Solução (x, y)')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Linha horizontal (eixo x)
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # Linha vertical (eixo y)
plt.title('Solução do Sistema de Equações Lineares')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()