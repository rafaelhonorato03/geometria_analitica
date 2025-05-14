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
        # Operações básicas com matrizes
        "Determinante (Regra de Sarrus)",
        "Determinante da Matriz",
        "Transposta da Matriz",
        "Forma Escada (Gauss-Jordan)",
        "Inversa da Matriz",
        "Verificar se é Invertível",
        "Posto da Matriz",
        "Resolver Sistema Linear",

        # Operações com pontos e vetores
        "Distância entre Pontos",
        "Ângulo entre Vetores",

        # Operações com retas
        "Equações da Reta (Paramétricas e Forma Simétrica)",
        "Ângulo entre Retas",
        "Distância entre Duas Retas",

        # Operações com planos
        "Equação Paramétrica do Plano",
        "Equação Cartesiana do Plano",
        "Ângulo entre Planos",
        "Interseção entre Três Planos"
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

def distancia_entre_duas_retas(p1, d1, p2, d2):
    """
    Calcula a distância entre duas retas no espaço 3D.
    :param p1: Ponto em uma das retas (numpy array).
    :param d1: Vetor diretor da primeira reta (numpy array).
    :param p2: Ponto na outra reta (numpy array).
    :param d2: Vetor diretor da segunda reta (numpy array).
    :return: Distância entre as retas.
    """
    try:
        vetor_conexao = p2 - p1
        vetor_normal = np.cross(d1, d2)
        norma_normal = np.linalg.norm(vetor_normal)
        if norma_normal == 0:
            return "As retas são paralelas ou coincidentes."
        distancia = abs(np.dot(vetor_conexao, vetor_normal)) / norma_normal
        return f"A distância entre as retas é {distancia:.2f}"
    except Exception as e:
        return f"Erro ao calcular a distância entre as retas: {str(e)}"

def distancia_entre_pontos(p1, p2):
    """
    Calcula a distância entre dois pontos no espaço.
    :param p1: Primeiro ponto (numpy array).
    :param p2: Segundo ponto (numpy array).
    :return: Distância entre os pontos.
    """
    try:
        distancia = np.linalg.norm(p2 - p1)
        return f"A distância entre os pontos é {distancia:.2f}"
    except Exception as e:
        return f"Erro ao calcular a distância entre os pontos: {str(e)}"

def intersecao_tres_planos(A, B, C, D):
    """
    Verifica a interseção de três planos no espaço.
    :param A, B, C: Coeficientes das equações dos planos (numpy arrays).
    :param D: Termos independentes dos planos (numpy array).
    :return: Ponto de interseção ou mensagem de erro.
    """
    try:
        coeficientes = np.array([A, B, C])
        termos_independentes = np.array(D)
        if np.linalg.matrix_rank(coeficientes) < 3:
            return "Os planos não se intersectam em um único ponto."
        ponto_intersecao = np.linalg.solve(coeficientes, termos_independentes)
        return f"O ponto de interseção é {np.round(ponto_intersecao, 2)}"
    except Exception as e:
        return f"Erro ao calcular a interseção: {str(e)}"

def angulo_entre_retas(d1, d2):
    """
    Calcula o ângulo entre duas retas no espaço 3D.
    :param d1: Vetor diretor da primeira reta (numpy array).
    :param d2: Vetor diretor da segunda reta (numpy array).
    :return: Ângulo entre as retas em graus.
    """
    try:
        produto_escalar = np.dot(d1, d2)
        norma_d1 = np.linalg.norm(d1)
        norma_d2 = np.linalg.norm(d2)
        cos_theta = produto_escalar / (norma_d1 * norma_d2)
        cos_theta = np.clip(cos_theta, -1.0, 1.0)
        angulo = np.degrees(np.arccos(cos_theta))
        return f"O ângulo entre as retas é {angulo:.2f} graus"
    except Exception as e:
        return f"Erro ao calcular o ângulo entre as retas: {str(e)}"

def equacao_parametrica_plano(ponto, vetor1, vetor2):
    """
    Retorna a equação paramétrica de um plano.
    :param ponto: Ponto no plano (numpy array).
    :param vetor1: Primeiro vetor diretor do plano (numpy array).
    :param vetor2: Segundo vetor diretor do plano (numpy array).
    :return: Equação paramétrica do plano.
    """
    try:
        return f"r(u, v) = {ponto} + u * {vetor1} + v * {vetor2}"
    except Exception as e:
        return f"Erro ao calcular a equação paramétrica do plano: {str(e)}"

def equacao_cartesiana_plano(ponto, normal):
    """
    Retorna a equação cartesiana de um plano.
    :param ponto: Ponto no plano (numpy array).
    :param normal: Vetor normal ao plano (numpy array).
    :return: Equação cartesiana do plano.
    """
    try:
        d = -np.dot(normal, ponto)
        return f"{normal[0]}x + {normal[1]}y + {normal[2]}z + ({d}) = 0"
    except Exception as e:
        return f"Erro ao calcular a equação cartesiana do plano: {str(e)}"

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
        elif opcao == "Distância entre Duas Retas":
            # Solicitar entrada de pontos e vetores
            p1 = np.array([float(x) for x in st.text_input("Digite o ponto P1 (separado por vírgulas):").split(",")])
            d1 = np.array([float(x) for x in st.text_input("Digite o vetor diretor D1 (separado por vírgulas):").split(",")])
            p2 = np.array([float(x) for x in st.text_input("Digite o ponto P2 (separado por vírgulas):").split(",")])
            d2 = np.array([float(x) for x in st.text_input("Digite o vetor diretor D2 (separado por vírgulas):").split(",")])
            resultado = distancia_entre_duas_retas(p1, d1, p2, d2)
        elif opcao == "Interseção entre Três Planos":
            # Solicitar entrada de coeficientes
            A = np.array([float(x) for x in st.text_input("Digite os coeficientes do plano 1 (separado por vírgulas):").split(",")])
            B = np.array([float(x) for x in st.text_input("Digite os coeficientes do plano 2 (separado por vírgulas):").split(",")])
            C = np.array([float(x) for x in st.text_input("Digite os coeficientes do plano 3 (separado por vírgulas):").split(",")])
            D = np.array([float(x) for x in st.text_input("Digite os termos independentes (separado por vírgulas):").split(",")])
            resultado = intersecao_tres_planos(A, B, C, D)
        elif opcao == "Ângulo entre Retas":
            # Solicitar entrada de vetores diretores
            d1 = np.array([float(x) for x in st.text_input("Digite o vetor diretor D1 (separado por vírgulas):").split(",")])
            d2 = np.array([float(x) for x in st.text_input("Digite o vetor diretor D2 (separado por vírgulas):").split(",")])
            resultado = angulo_entre_retas(d1, d2)
        elif opcao == "Equação Paramétrica do Plano":
            # Solicitar entrada de ponto e vetores diretores
            ponto = np.array([float(x) for x in st.text_input("Digite o ponto no plano (separado por vírgulas):").split(",")])
            vetor1 = np.array([float(x) for x in st.text_input("Digite o primeiro vetor diretor (separado por vírgulas):").split(",")])
            vetor2 = np.array([float(x) for x in st.text_input("Digite o segundo vetor diretor (separado por vírgulas):").split(",")])
            resultado = equacao_parametrica_plano(ponto, vetor1, vetor2)
        elif opcao == "Equação Cartesiana do Plano":
            # Solicitar entrada de ponto e vetor normal
            ponto = np.array([float(x) for x in st.text_input("Digite o ponto no plano (separado por vírgulas):").split(",")])
            normal = np.array([float(x) for x in st.text_input("Digite o vetor normal ao plano (separado por vírgulas):").split(",")])
            resultado = equacao_cartesiana_plano(ponto, normal)
        elif opcao == "Distância entre Pontos":
            # Solicitar entrada de dois pontos
            p1 = np.array([float(x) for x in st.text_input("Digite o ponto P1 (separado por vírgulas):").split(",")])
            p2 = np.array([float(x) for x in st.text_input("Digite o ponto P2 (separado por vírgulas):").split(",")])
            resultado = distancia_entre_pontos(p1, p2)

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