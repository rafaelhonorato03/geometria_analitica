import streamlit as st
import numpy as np

st.set_page_config(page_title="Resolutor de Matrizes", layout="centered")

st.title("🧮 Resolutor de Matrizes")

st.markdown("Digite a matriz separando colunas por espaço e linhas por ENTER:")
entrada = st.text_area("Exemplo:", "1 2 3\n0 1 4\n5 6 0")

opcao = st.selectbox(
    "Escolha a operação:",
    (
        "Forma Escada (Gauss-Jordan)",
        "Inversa da Matriz",
        "Verificar se é Invertível",
        "Posto da Matriz",
        "Resolver Sistema Linear"
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

        if isinstance(resultado, np.ndarray):
            st.write("Matriz Resultante:")
            st.dataframe(resultado)
        else:
            st.write(resultado)