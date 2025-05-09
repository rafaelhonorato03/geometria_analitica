import streamlit as st
import numpy as np

st.set_page_config(page_title="Resolutor de Matrizes e Operações com Vetores", layout="centered")

st.title("🧮 Resolutor de Matrizes")

# Centralizar imagem pequena
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Frans_Hals_-_Portret_van_Ren%C3%A9_Descartes.jpg/800px-Frans_Hals_-_Portret_van_Ren%C3%A9_Descartes.jpg" width="150">
        <p style="font-size:12px;">“René Descartes, o pai da álgebra linear.”</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("Digite a matriz separando colunas por espaço e linhas por ENTER:")
entrada = st.text_area("Exemplo:", "1 2 3\n0 1 4\n5 6 0")

opcao = st.selectbox(
    "Escolha a operação:",
    (
        "Determinante (Regra de Sarrus)",
        "Determinante da Matriz",
        "Forma Escada (Gauss-Jordan)",
        "Inversa da Matriz",
        "Posto da Matriz",
        "Resolver Sistema Linear",
        "Transposta da Matriz",
        "Verificar se é Invertível"
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

def soma_vetores(vetor1, vetor2):
    return vetor1 + vetor2

def multiplicacao_escalar(vetor, escalar):
    return escalar * vetor

def produto_escalar(vetor1, vetor2):
    return np.dot(vetor1, vetor2)

def produto_vetorial(vetor1, vetor2):
    return np.cross(vetor1, vetor2)

def angulo_entre_vetores(vetor1, vetor2):
    try:
        produto_escalar = np.dot(vetor1, vetor2)
        norma_vetor1 = np.linalg.norm(vetor1)
        norma_vetor2 = np.linalg.norm(vetor2)
        cos_theta = produto_escalar / (norma_vetor1 * norma_vetor2)
        cos_theta = np.clip(cos_theta, -1.0, 1.0)
        angulo = np.degrees(np.arccos(cos_theta))
        return angulo
    except Exception as e:
        return f"Erro ao calcular o ângulo: {str(e)}"

def reta_entre_vetores(vetor1, vetor2):
    """
    Retorna a equação paramétrica da reta definida por dois vetores.
    :param vetor1: Primeiro vetor (numpy array).
    :param vetor2: Segundo vetor (numpy array).
    :return: Equação paramétrica da reta.
    """
    try:
        vetor_direcao = vetor2 - vetor1
        return f"r(t) = {vetor1} + t * {vetor_direcao}"
    except Exception as e:
        return f"Erro ao calcular a reta: {str(e)}"

def produto_misto(vetor1, vetor2, vetor3):
    """
    Calcula o produto misto de três vetores no espaço 3D.
    :param vetor1: Primeiro vetor (numpy array).
    :param vetor2: Segundo vetor (numpy array).
    :param vetor3: Terceiro vetor (numpy array).
    :return: Produto misto (escalar).
    """
    try:
        # Produto vetorial entre vetor2 e vetor3
        produto_vetorial = np.cross(vetor2, vetor3)
        
        # Produto escalar entre vetor1 e o resultado do produto vetorial
        produto_misto = np.dot(vetor1, produto_vetorial)
        
        return produto_misto
    except Exception as e:
        return f"Erro ao calcular o produto misto: {str(e)}"

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

st.title("🧮 Operações com Vetores")

# Escolher a quantidade de vetores
quantidade_vetores = st.radio("Quantos vetores você deseja usar?", ("Dois Vetores", "Três Vetores"))

# Entrada dos vetores
vetor1 = st.text_input("Digite o primeiro vetor (separado por vírgulas):", "1, 2, 3")
vetor2 = st.text_input("Digite o segundo vetor (separado por vírgulas):", "4, 5, 6")

# Converter os vetores para arrays NumPy
try:
    vetor1 = np.array([float(x) for x in vetor1.split(",")])
    vetor2 = np.array([float(x) for x in vetor2.split(",")])
except ValueError:
    st.error("Por favor, insira os vetores corretamente (números separados por vírgulas).")

# Entrada do terceiro vetor, se necessário
if quantidade_vetores == "Três Vetores":
    vetor3 = st.text_input("Digite o terceiro vetor (separado por vírgulas):", "7, 8, 9")
    try:
        vetor3 = np.array([float(x) for x in vetor3.split(",")])
    except ValueError:
        st.error("Por favor, insira o terceiro vetor corretamente (números separados por vírgulas).")

# Escolher a operação
if quantidade_vetores == "Dois Vetores":
    operacao = st.selectbox(
        "Escolha a operação:",
        (
            "Ângulo entre Vetores",
            "Multiplicação por Escalar",
            "Produto Escalar",
            "Produto Vetorial",
            "Soma de Vetores"
        )
    )
else:  # Três Vetores
    operacao = st.selectbox(
        "Escolha a operação:",
        (
            "Produto Misto",
        )
    )

# Executar a operação
if st.button("Calcular"):
    if operacao == "Soma de Vetores":
        resultado = soma_vetores(vetor1, vetor2)
        st.write("Resultado da soma:", resultado)
    elif operacao == "Multiplicação por Escalar":
        escalar = st.number_input("Digite o escalar:", value=1.0)
        resultado = multiplicacao_escalar(vetor1, escalar)
        st.write(f"Resultado da multiplicação de {vetor1} por {escalar}:", resultado)
    elif operacao == "Produto Escalar":
        resultado = produto_escalar(vetor1, vetor2)
        st.write("Resultado do produto escalar:", resultado)
    elif operacao == "Produto Vetorial":
        if len(vetor1) == 3 and len(vetor2) == 3:
            resultado = produto_vetorial(vetor1, vetor2)
            st.write("Resultado do produto vetorial:", resultado)
        else:
            st.error("O produto vetorial só é definido para vetores 3D.")
    elif operacao == "Ângulo entre Vetores":
        resultado = angulo_entre_vetores(vetor1, vetor2)
        st.write(f"Ângulo entre os vetores (em graus): {resultado:.2f}")
    elif operacao == "Produto Misto":
        if len(vetor1) == 3 and len(vetor2) == 3 and len(vetor3) == 3:
            resultado = produto_misto(vetor1, vetor2, vetor3)
            st.write("Resultado do produto misto:", resultado)
            st.write(f"Volume do paralelepípedo: {abs(resultado):.2f}")
        else:
            st.error("O produto misto só é definido para vetores 3D.")