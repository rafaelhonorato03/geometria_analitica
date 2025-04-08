import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("Álgebra Linear e Visualização de Matrizes/Vetores")

st.header("Operações com Vetores")

vetor_u = np.array([1, -2, 0])
vetor_v = np.array([0, 2, 2])
vetor_w = np.array([1, 2, -1])

soma_vetores = vetor_u + vetor_v
multiplicacao_escalar = 7 * vetor_u
produto_escalar = np.dot(vetor_u, vetor_v)
produto_vetorial = np.cross(vetor_u, vetor_v)
produto_misto = np.linalg.det([vetor_u, vetor_v, vetor_w])

st.write("Vetor u:", vetor_u)
st.write("Vetor v:", vetor_v)
st.write("Vetor w:", vetor_w)
st.write("Soma dos vetores u e v:", soma_vetores)
st.write("Multiplicação do vetor u por 7:", multiplicacao_escalar)
st.write("Produto escalar de u e v:", produto_escalar)
st.write("Produto vetorial de u e v:", produto_vetorial)
st.write("Produto misto de u, v e w:", produto_misto)

st.header("Gráficos de Vetores e Cônicas")

def plot_elipse():
    a, b, x0, y0 = 3, 2, -2, 1
    t = np.linspace(-1, 2 * np.pi, 100)
    x = a * np.cos(t) + x0
    y = b * np.sin(t) + y0
    fig, ax = plt.subplots()
    ax.plot(x, y, label='Elipse')
    ax.legend()
    ax.axis([-6, 2, -2, 5])
    st.pyplot(fig)

def plot_elipse_espelhada():
    a, b, x0, y0 = 3, 2, -2, 1
    t = np.linspace(-1, 1, 100)
    x = a * np.cos(t) + x0
    y = b * np.sin(t) + y0
    fig, ax = plt.subplots()
    ax.plot(x, y, color='red')
    ax.plot(-x, y, color='red')
    ax.set_title('Elipse Espelhada')
    ax.axis([-5, 5, -2, 4])
    st.pyplot(fig)

def plot_parabola():
    p, x0, y0 = 2, -2, 1
    t = np.linspace(-4, 4, 100)
    x = t + x0
    y = (1 / (4 * p)) * t ** 2
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.axis([-7, 3, -1, 3])
    st.pyplot(fig)

def plot_polar():
    n = 20
    t = np.linspace(0, 2 * np.pi, 500)
    r = np.cos(n * t)
    x = r * np.cos(t)
    y = r * np.sin(t)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    st.pyplot(fig)

plot_elipse()
plot_elipse_espelhada()
plot_parabola()
plot_polar()

st.header("Resolução de Sistemas Lineares")
A = np.array([[2, -1], [-1, 2]])
B = np.array([3, 0])
solucao = np.linalg.solve(A, B)
st.write("Solução do sistema 2x2:", solucao)

st.header("Multiplicação de Matrizes")
A = np.array([[2, 1], [1, 3], [0, 1]])
B = np.array([[0, 3, 0], [4, 1, 1]])
AB = np.dot(A, B)
st.write("A:", A)
st.write("B:", B)
st.write("Produto AB:", AB)

st.header("Tipos de Matrizes")
def matriz_quadrada(matriz):
    return matriz.shape[0] == matriz.shape[1]

def matriz_nula(matriz):
    return np.all(matriz == 0)

def matriz_identidade(matriz):
    return matriz_quadrada(matriz) and np.all(matriz == np.eye(matriz.shape[0]))

def matriz_simetrica(matriz):
    return matriz_quadrada(matriz) and np.all(matriz == matriz.T)

a = np.array([[1, 2, 3], [2, 4, 5], [3, 5, 6]])
b = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
c = np.zeros((3, 3))
d = np.array([[1, 2], [3, 4]])

st.write("A é quadrada?", matriz_quadrada(a))
st.write("B é identidade?", matriz_identidade(b))
st.write("C é nula?", matriz_nula(c))
st.write("A é simétrica?", matriz_simetrica(a))

st.header("Transposição de Matrizes")
A = np.array([[2, 3, 5], [3, 1, -1], [0, 0, 3]])
transposta = A.T
st.write("Matriz A:", A)
st.write("Transposta de A:", transposta)

st.header("Multiplicação Final")
A = np.array([[1,0], [1,3]])
B = np.array([[1,0,2], [1,3,0]])
st.write("Produto A * B:", np.dot(A,B))