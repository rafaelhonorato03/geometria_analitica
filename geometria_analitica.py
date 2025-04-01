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


# Definição das matrizes
A = np.array([[2, 1],
              [1, 3],
              [0, 1]])

B = np.array([[0, 3, 0],
              [4, 1, 1]])

# Multiplicação de matrizes
AB = np.dot(A, B)

print(AB)

# Verificando o tipo de matriz
def matriz_quadrada(matriz):
    return matriz.shape[0] == matriz.shape[1]

def matriz_nula(matriz):
    return np.all(matriz == 0)

def matriz_identidade(matriz):
    return matriz_quadrada(matriz) and np.all(matriz == np.eye(matriz.shape[0]))

def matriz_simetrica(matriz):
    return matriz_quadrada(matriz) and np.all(matriz == matriz.T)

# Exemplo de matrizes
a = np.array([[1, 2, 3], [2, 4, 5], [3, 5, 6]])  # Simétrica
b = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])  # Identidade
c = np.zeros((3, 3))  # Nula
d = np.array([[1, 2], [3, 4]])  # Quadrada, mas não simétrica nem identidade

# Testando as funções
print("A é quadrada?", matriz_quadrada(a))
print("B é identidade?", matriz_identidade(b))
print("C é nula?", matriz_nula(c))
print("A é simétrica?", matriz_simetrica(a))

# Transposição de matrizes
A = np.array([[2, 3, 5],
              [3, 1, -1],
              [0, 0, 3]])

B = np.array([[0, 2, 2],
              [1, -1, 5],
              [5, -1, 0]])

### Exemplo:
transposta = A.T
print("Transposta de A:\n", transposta)

A = np.array([[1,0],
             [1,3]])

B = np.array([[1,0,2],
             [1,3,0]])

print(np.dot(A,B))