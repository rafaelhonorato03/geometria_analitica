"""
Interface Streamlit para Geometria Analítica
Aplicação web interativa para cálculos de matrizes, vetores e geometria analítica
"""

import streamlit as st
import numpy as np
import sys
import os

# Adicionar o diretório src ao path para importar os módulos
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.matriz_operations import *
from core.vector_operations import *
from core.geometric_operations import *

st.set_page_config(page_title="Geometria Analítica - Calculadora Interativa", layout="centered")

st.title("🧮 Calculadora de Geometria Analítica")

# Centralizar imagem pequena
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Frans_Hals_-_Portret_van_Ren%C3%A9_Descartes.jpg/800px-Frans_Hals_-_Portret_van_Ren%C3%A9_Descartes.jpg" width="150">
        <p style="font-size:12px;">"René Descartes, o pai da geometria analítica."</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar para seleção de categoria
categoria = st.sidebar.selectbox(
    "Escolha a categoria:",
    ["Matrizes", "Vetores", "Geometria Analítica"]
)

if categoria == "Matrizes":
    st.header("📊 Operações com Matrizes")
    
    st.markdown("Digite a matriz separando colunas por espaço e linhas por ENTER:")
    entrada = st.text_area("Exemplo:", "1 2 3\n0 1 4\n5 6 0")
    
    opcao = st.selectbox(
        "Escolha a operação:",
        [
            "Determinante (Regra de Sarrus)",
            "Determinante da Matriz",
            "Transposta da Matriz",
            "Forma Escada (Gauss-Jordan)",
            "Inversa da Matriz",
            "Verificar se é Invertível",
            "Posto da Matriz",
            "Resolver Sistema Linear",
            "Produto de Matrizes",
            "Verificar Tipo de Matriz"
        ]
    )
    
    def parse_matrix(texto):
        try:
            return np.array([list(map(float, linha.split())) for linha in texto.strip().split('\n')])
        except:
            return None
    
    if st.button("Calcular"):
        matriz = parse_matrix(entrada)
        if matriz is None:
            st.error("Formato inválido! Use espaço entre números e ENTER para nova linha.")
        else:
            st.write("Matriz inserida:")
            st.write(matriz)
            
            if opcao == "Determinante (Regra de Sarrus)":
                resultado = regra_de_sarrus(matriz)
                st.write(f"**Resultado:** {resultado}")
                
            elif opcao == "Determinante da Matriz":
                resultado = determinante(matriz)
                st.write(f"**Resultado:** {resultado}")
                
            elif opcao == "Transposta da Matriz":
                resultado = transposta(matriz)
                st.write("**Matriz Transposta:**")
                st.write(resultado)
                
            elif opcao == "Forma Escada (Gauss-Jordan)":
                resultado = forma_escada(matriz)
                st.write("**Forma Escada:**")
                st.write(resultado)
                
            elif opcao == "Inversa da Matriz":
                resultado = inversa_matriz(matriz)
                st.write("**Matriz Inversa:**")
                st.write(resultado)
                
            elif opcao == "Verificar se é Invertível":
                resultado = eh_invertivel(matriz)
                if resultado:
                    st.success("✅ Sim. A matriz é invertível.")
                else:
                    st.error("❌ Não. A matriz NÃO é invertível.")
                    
            elif opcao == "Posto da Matriz":
                resultado = calcular_posto(matriz)
                st.write(f"**Resultado:** {resultado}")
                
            elif opcao == "Resolver Sistema Linear":
                resultado = resolver_sistema(matriz)
                st.write(f"**Solução:** {resultado}")
                
            elif opcao == "Produto de Matrizes":
                st.write("Digite a segunda matriz:")
                entrada2 = st.text_area("Segunda matriz:", "1 0\n0 1\n1 1")
                matriz2 = parse_matrix(entrada2)
                if matriz2 is not None:
                    resultado = produto_matrizes(matriz, matriz2)
                    st.write("**Produto das Matrizes:**")
                    st.write(resultado)
                    
            elif opcao == "Verificar Tipo de Matriz":
                resultado = verificar_tipo_matriz(matriz)
                st.write("**Propriedades da Matriz:**")
                for prop, valor in resultado.items():
                    if valor:
                        st.write(f"✅ {prop.capitalize()}")
                    else:
                        st.write(f"❌ {prop.capitalize()}")

elif categoria == "Vetores":
    st.header("➡️ Operações com Vetores")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Vetor 1")
        v1_x = st.number_input("x1:", value=1.0)
        v1_y = st.number_input("y1:", value=1.0)
        v1_z = st.number_input("z1:", value=0.0)
        
    with col2:
        st.subheader("Vetor 2")
        v2_x = st.number_input("x2:", value=-1.0)
        v2_y = st.number_input("y2:", value=1.0)
        v2_z = st.number_input("z2:", value=0.0)
    
    vetor1 = np.array([v1_x, v1_y, v1_z])
    vetor2 = np.array([v2_x, v2_y, v2_z])
    
    opcao_vetor = st.selectbox(
        "Escolha a operação:",
        [
            "Soma de Vetores",
            "Multiplicação por Escalar",
            "Produto Escalar",
            "Produto Vetorial",
            "Ângulo entre Vetores",
            "Norma do Vetor",
            "Vetor Unitário",
            "Distância entre Pontos",
            "Projeção Vetorial",
            "Verificar se são Ortogonais",
            "Verificar se são Paralelos"
        ]
    )
    
    escalar = st.number_input("Escalar (para multiplicação):", value=2.0)
    
    if st.button("Calcular Operação Vetorial"):
        st.write("**Vetor 1:**", vetor1)
        st.write("**Vetor 2:**", vetor2)
        
        if opcao_vetor == "Soma de Vetores":
            resultado = soma_vetores(vetor1, vetor2)
            st.write("**Soma:**", resultado)
            
        elif opcao_vetor == "Multiplicação por Escalar":
            resultado = multiplicacao_escalar(vetor1, escalar)
            st.write(f"**{escalar} × Vetor 1:**", resultado)
            
        elif opcao_vetor == "Produto Escalar":
            resultado = produto_escalar(vetor1, vetor2)
            st.write("**Produto Escalar:**", resultado)
            
        elif opcao_vetor == "Produto Vetorial":
            resultado = produto_vetorial(vetor1, vetor2)
            st.write("**Produto Vetorial:**", resultado)
            
        elif opcao_vetor == "Ângulo entre Vetores":
            resultado = angulo_entre_vetores(vetor1, vetor2)
            st.write(f"**Ângulo:** {resultado:.2f}°")
            
        elif opcao_vetor == "Norma do Vetor":
            resultado1 = norma_vetor(vetor1)
            resultado2 = norma_vetor(vetor2)
            st.write(f"**Norma do Vetor 1:** {resultado1:.2f}")
            st.write(f"**Norma do Vetor 2:** {resultado2:.2f}")
            
        elif opcao_vetor == "Vetor Unitário":
            resultado1 = vetor_unitario(vetor1)
            resultado2 = vetor_unitario(vetor2)
            st.write("**Vetor Unitário 1:**", resultado1)
            st.write("**Vetor Unitário 2:**", resultado2)
            
        elif opcao_vetor == "Distância entre Pontos":
            resultado = distancia_entre_pontos(vetor1, vetor2)
            st.write(f"**Distância:** {resultado:.2f}")
            
        elif opcao_vetor == "Projeção Vetorial":
            resultado = projecao_vetorial(vetor1, vetor2)
            st.write("**Projeção de v1 sobre v2:**", resultado)
            
        elif opcao_vetor == "Verificar se são Ortogonais":
            resultado = sao_ortogonais(vetor1, vetor2)
            if resultado:
                st.success("✅ Os vetores são ortogonais")
            else:
                st.info("❌ Os vetores não são ortogonais")
                
        elif opcao_vetor == "Verificar se são Paralelos":
            resultado = sao_paralelos(vetor1, vetor2)
            if resultado:
                st.success("✅ Os vetores são paralelos")
            else:
                st.info("❌ Os vetores não são paralelos")

elif categoria == "Geometria Analítica":
    st.header("📐 Geometria Analítica")
    
    subcategoria = st.selectbox(
        "Escolha a subcategoria:",
        ["Retas", "Planos", "Distâncias e Ângulos"]
    )
    
    if subcategoria == "Retas":
        st.subheader("📏 Operações com Retas")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Reta 1:**")
            p1_x = st.number_input("Ponto 1 - x:", value=0.0, key="p1x")
            p1_y = st.number_input("Ponto 1 - y:", value=0.0, key="p1y")
            p1_z = st.number_input("Ponto 1 - z:", value=0.0, key="p1z")
            v1_x = st.number_input("Vetor 1 - x:", value=1.0, key="v1x")
            v1_y = st.number_input("Vetor 1 - y:", value=0.0, key="v1y")
            v1_z = st.number_input("Vetor 1 - z:", value=0.0, key="v1z")
            
        with col2:
            st.write("**Reta 2:**")
            p2_x = st.number_input("Ponto 2 - x:", value=1.0, key="p2x")
            p2_y = st.number_input("Ponto 2 - y:", value=0.0, key="p2y")
            p2_z = st.number_input("Ponto 2 - z:", value=0.0, key="p2z")
            v2_x = st.number_input("Vetor 2 - x:", value=0.0, key="v2x")
            v2_y = st.number_input("Vetor 2 - y:", value=1.0, key="v2y")
            v2_z = st.number_input("Vetor 2 - z:", value=0.0, key="v2z")
        
        ponto1 = np.array([p1_x, p1_y, p1_z])
        vetor1 = np.array([v1_x, v1_y, v1_z])
        ponto2 = np.array([p2_x, p2_y, p2_z])
        vetor2 = np.array([v2_x, v2_y, v2_z])
        
        opcao_reta = st.selectbox(
            "Escolha a operação:",
            [
                "Equação Paramétrica da Reta 1",
                "Equação Simétrica da Reta 1",
                "Ângulo entre Retas",
                "Distância entre Retas",
                "Verificar se são Paralelas",
                "Verificar se são Perpendiculares"
            ]
        )
        
        if st.button("Calcular Operação com Retas"):
            if opcao_reta == "Equação Paramétrica da Reta 1":
                resultado = equacao_parametrica_reta(ponto1, vetor1)
                st.write("**Equação Paramétrica:**", resultado)
                
            elif opcao_reta == "Equação Simétrica da Reta 1":
                resultado = equacao_simetrica_reta(ponto1, vetor1)
                st.write("**Equação Simétrica:**", resultado)
                
            elif opcao_reta == "Ângulo entre Retas":
                resultado = angulo_entre_retas(vetor1, vetor2)
                st.write(f"**Ângulo:** {resultado:.2f}°")
                
            elif opcao_reta == "Distância entre Retas":
                resultado = distancia_entre_duas_retas(ponto1, vetor1, ponto2, vetor2)
                st.write(f"**Distância:** {resultado}")
                
            elif opcao_reta == "Verificar se são Paralelas":
                resultado = sao_paralelas_retas(vetor1, vetor2)
                if resultado:
                    st.success("✅ As retas são paralelas")
                else:
                    st.info("❌ As retas não são paralelas")
                    
            elif opcao_reta == "Verificar se são Perpendiculares":
                resultado = sao_perpendiculares_retas(vetor1, vetor2)
                if resultado:
                    st.success("✅ As retas são perpendiculares")
                else:
                    st.info("❌ As retas não são perpendiculares")
    
    elif subcategoria == "Planos":
        st.subheader("🛩️ Operações com Planos")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Plano 1:**")
            p1_x = st.number_input("Ponto - x:", value=0.0, key="pp1x")
            p1_y = st.number_input("Ponto - y:", value=0.0, key="pp1y")
            p1_z = st.number_input("Ponto - z:", value=0.0, key="pp1z")
            n1_x = st.number_input("Normal - x:", value=1.0, key="n1x")
            n1_y = st.number_input("Normal - y:", value=0.0, key="n1y")
            n1_z = st.number_input("Normal - z:", value=0.0, key="n1z")
            
        with col2:
            st.write("**Plano 2:**")
            n2_x = st.number_input("Normal 2 - x:", value=0.0, key="n2x")
            n2_y = st.number_input("Normal 2 - y:", value=1.0, key="n2y")
            n2_z = st.number_input("Normal 2 - z:", value=0.0, key="n2z")
        
        ponto_plano = np.array([p1_x, p1_y, p1_z])
        normal1 = np.array([n1_x, n1_y, n1_z])
        normal2 = np.array([n2_x, n2_y, n2_z])
        
        opcao_plano = st.selectbox(
            "Escolha a operação:",
            [
                "Equação Paramétrica do Plano",
                "Equação Cartesiana do Plano",
                "Ângulo entre Planos"
            ]
        )
        
        if st.button("Calcular Operação com Planos"):
            if opcao_plano == "Equação Paramétrica do Plano":
                # Para equação paramétrica, precisamos de dois vetores direção
                vetor1 = np.array([1, 0, 0])
                vetor2 = np.array([0, 1, 0])
                resultado = equacao_parametrica_plano(ponto_plano, vetor1, vetor2)
                st.write("**Equação Paramétrica:**", resultado)
                
            elif opcao_plano == "Equação Cartesiana do Plano":
                resultado = equacao_cartesiana_plano(ponto_plano, normal1)
                st.write("**Equação Cartesiana:**", resultado)
                
            elif opcao_plano == "Ângulo entre Planos":
                resultado = angulo_entre_planos(normal1, normal2)
                st.write(f"**Ângulo:** {resultado:.2f}°")
    
    elif subcategoria == "Distâncias e Ângulos":
        st.subheader("📏 Distâncias e Ângulos")
        
        st.write("**Ponto:**")
        px = st.number_input("x:", value=1.0)
        py = st.number_input("y:", value=1.0)
        pz = st.number_input("z:", value=1.0)
        
        ponto = np.array([px, py, pz])
        
        opcao_dist = st.selectbox(
            "Escolha a operação:",
            [
                "Distância Ponto-Reta",
                "Distância Ponto-Plano"
            ]
        )
        
        if opcao_dist == "Distância Ponto-Reta":
            st.write("**Ponto da Reta:**")
            pr_x = st.number_input("Ponto Reta - x:", value=0.0)
            pr_y = st.number_input("Ponto Reta - y:", value=0.0)
            pr_z = st.number_input("Ponto Reta - z:", value=0.0)
            
            st.write("**Vetor Direção:**")
            vd_x = st.number_input("Vetor Dir - x:", value=1.0)
            vd_y = st.number_input("Vetor Dir - y:", value=0.0)
            vd_z = st.number_input("Vetor Dir - z:", value=0.0)
            
            ponto_reta = np.array([pr_x, pr_y, pr_z])
            vetor_direcao = np.array([vd_x, vd_y, vd_z])
            
        elif opcao_dist == "Distância Ponto-Plano":
            st.write("**Ponto do Plano:**")
            pp_x = st.number_input("Ponto Plano - x:", value=0.0)
            pp_y = st.number_input("Ponto Plano - y:", value=0.0)
            pp_z = st.number_input("Ponto Plano - z:", value=0.0)
            
            st.write("**Vetor Normal:**")
            vn_x = st.number_input("Vetor Normal - x:", value=1.0)
            vn_y = st.number_input("Vetor Normal - y:", value=0.0)
            vn_z = st.number_input("Vetor Normal - z:", value=0.0)
            
            ponto_plano = np.array([pp_x, pp_y, pp_z])
            vetor_normal = np.array([vn_x, vn_y, vn_z])
        
        if st.button("Calcular Distância"):
            if opcao_dist == "Distância Ponto-Reta":
                resultado = distancia_ponto_reta(ponto, ponto_reta, vetor_direcao)
                st.write(f"**Distância:** {resultado:.2f}")
                
            elif opcao_dist == "Distância Ponto-Plano":
                resultado = distancia_ponto_plano(ponto, ponto_plano, vetor_normal)
                st.write(f"**Distância:** {resultado:.2f}")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center;">
        <p>Desenvolvido com ❤️ para o estudo de Geometria Analítica</p>
        <p>Baseado nos conteúdos de Leandro Cruvinel</p>
    </div>
    """,
    unsafe_allow_html=True
) 