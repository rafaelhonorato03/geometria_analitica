import streamlit as st
import numpy as np

st.set_page_config(page_title="Resolutor de Matrizes", layout="centered")

st.title("🧮 Resolutor de Matrizes")

#st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Frans_Hals_-_Portret_van_Ren%C3%A9_Descartes.jpg/800px-Frans_Hals_-_Portret_van_Ren%C3%A9_Descartes.jpg',
         #caption="René Descartes, o pai da álgebra linear.",
         #width=150)

# Centralizar título
st.markdown("<h1 style='text-align: center;'>Bem-vindo ao mundo de René Descartes</h1>", unsafe_allow_html=True)

# Centralizar imagem pequena
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Frans_Hals_-_Portret_van_Ren%C3%A9_Descartes.jpg/800px-Frans_Hals_-_Portret_van_Ren%C3%A9_Descartes.jpg" width="300">
        <p style="font-size:20px;">“Penso, logo existo.”</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("Digite a matriz separando colunas por espaço e linhas por ENTER:")
entrada = st.text_area("Exemplo:", "1 2 3\n0 1 4\n5 6 0")

opcao = st.selectbox(
    "Escolha a operação:",
    (
        "Forma Escada (Gauss-Jordan)",
        "Inversa da Matriz",
        "Verificar se é Invertível",
        "Posto da Matriz",
        "Resolver Sistema Linear",
        "Determinante (Regra de Sarrus)",
        "Determinante da Matriz",
        "Transposta da Matriz"
    )
)

def parse_matrix(texto):
    try:
        return np.array([list(map(float, linha.split())) for linha in texto.strip().split('\n')])
    except:
        return None

def forma_escada(matriz):
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

def inversa(matriz):
    try:
        return np.round(np.linalg.inv(matriz), 2)
    except:
        return "Matriz não é invertível."

def eh_invertivel(matriz):
    try:
        np.linalg.inv(matriz)
        return "✅ Sim. A matriz é invertível."
    except:
        return "❌ Não. A matriz NÃO é invertível."

def calcular_posto(matriz):
    return f"O posto da matriz é {np.linalg.matrix_rank(matriz)}"

def resolver_sistema(matriz):
    try:
        linhas, colunas = matriz.shape
        if colunas != linhas + 1:
            return "A matriz deve ser aumentada (última coluna = termos independentes)."
        A = matriz[:, :-1]
        b = matriz[:, -1]
        x = np.linalg.solve(A, b)
        return f"Solução: {np.round(x, 2)}"
    except Exception as e:
        return f"Erro ao resolver sistema: {str(e)}"

def regra_de_sarrus(matriz):
    """
    Calcula o determinante de uma matriz 3x3 usando a Regra de Sarrus.
    :param matriz: Matriz 3x3 (numpy array).
    :return: Determinante da matriz ou mensagem de erro.
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
        return f"O determinante da matriz é {np.round(det, 2)}"
    except Exception as e:
        return f"Erro ao calcular determinante: {str(e)}"

def transposta(matriz):
    """
    Calcula a matriz transposta.
    :param matriz: Matriz (numpy array).
    :return: Matriz transposta.
    """
    try:
        return matriz.T
    except Exception as e:
        return f"Erro ao calcular a transposta: {str(e)}"

def determinante(matriz):
    """
    Calcula o determinante de uma matriz.
    :param matriz: Matriz quadrada (numpy array).
    :return: Determinante da matriz ou mensagem de erro.
    """
    try:
        # Verificar se a matriz é quadrada
        if matriz.shape[0] != matriz.shape[1]:
            return "O determinante só pode ser calculado para matrizes quadradas."
        
        # Calcular o determinante
        det = np.linalg.det(matriz)
        return f"O determinante da matriz é {np.round(det, 2)}"
    except Exception as e:
        return f"Erro ao calcular o determinante: {str(e)}"

if st.button("Executar"):
    matriz = parse_matrix(entrada)

    if matriz is None:
        st.error("Formato inválido! Use espaço para colunas e ENTER para linhas.")
    else:
        st.subheader("Resultado:")

        if opcao == "Forma Escada (Gauss-Jordan)":
            resultado = forma_escada(matriz)
        elif opcao == "Inversa da Matriz":
            resultado = inversa(matriz)
        elif opcao == "Verificar se é Invertível":
            resultado = eh_invertivel(matriz)
        elif opcao == "Posto da Matriz":
            resultado = calcular_posto(matriz)
        elif opcao == "Resolver Sistema Linear":
            resultado = resolver_sistema(matriz)
        elif opcao == "Determinante (Regra de Sarrus)":
            resultado = regra_de_sarrus(matriz)
        elif opcao == "Determinante da Matriz":
            resultado = determinante(matriz)
        elif opcao == "Transposta da Matriz":
            resultado = transposta(matriz)

        if isinstance(resultado, np.ndarray):
            st.write("Matriz Resultante:")
            st.dataframe(resultado)
        else:
            st.write(resultado)