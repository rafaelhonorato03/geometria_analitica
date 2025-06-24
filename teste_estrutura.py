#!/usr/bin/env python3
"""
Teste da estrutura reorganizada
Verifica se todos os módulos estão funcionando corretamente
"""

import sys
import os

# Adicionar src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def testar_importacoes():
    """
    Testa se todas as importações estão funcionando.
    """
    print("🧪 Testando importações...")
    
    try:
        # Testar importações do core
        from core import determinante, inversa_matriz, forma_escada
        from core import soma_vetores, produto_escalar, angulo_entre_vetores
        from core import equacao_parametrica_reta, distancia_entre_pontos
        print("✅ Módulo core importado com sucesso")
        
        # Testar importações de visualização
        from visualization import plotar_elipse, plotar_circulo
        print("✅ Módulo visualization importado com sucesso")
        
        # Testar importações de exemplos
        from examples import exemplo_operacoes_matrizes
        print("✅ Módulo examples importado com sucesso")
        
        return True
        
    except ImportError as e:
        print(f"❌ Erro de importação: {e}")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False

def testar_funcionalidades():
    """
    Testa algumas funcionalidades básicas.
    """
    print("\n🧪 Testando funcionalidades...")
    
    try:
        import numpy as np
        from core import determinante, soma_vetores, produto_escalar
        
        # Teste de matriz
        A = np.array([[1, 2], [3, 4]])
        det = determinante(A)
        print(f"✅ Determinante de [[1,2],[3,4]] = {det}")
        
        # Teste de vetores
        u = np.array([1, 1, 0])
        v = np.array([-1, 1, 0])
        soma = soma_vetores(u, v)
        prod_esc = produto_escalar(u, v)
        print(f"✅ Soma de vetores: {soma}")
        print(f"✅ Produto escalar: {prod_esc}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao testar funcionalidades: {e}")
        return False

def mostrar_estrutura():
    """
    Mostra a estrutura do projeto.
    """
    print("\n📁 Estrutura do projeto:")
    print("geometria_analitica/")
    print("├── main.py                    # Menu interativo")
    print("├── requirements.txt           # Dependências")
    print("├── README.md                  # Documentação")
    print("├── teste_estrutura.py         # Este arquivo")
    print("│")
    print("├── src/                       # Código fonte")
    print("│   ├── __init__.py           # Pacote principal")
    print("│   │")
    print("│   ├── core/                 # Operações fundamentais")
    print("│   │   ├── __init__.py")
    print("│   │   ├── matriz_operations.py")
    print("│   │   ├── vector_operations.py")
    print("│   │   └── geometric_operations.py")
    print("│   │")
    print("│   ├── visualization/        # Visualização")
    print("│   │   ├── __init__.py")
    print("│   │   └── plotting.py")
    print("│   │")
    print("│   ├── interfaces/           # Interfaces")
    print("│   │   ├── __init__.py")
    print("│   │   ├── streamlit_app.py")
    print("│   │   └── tkinter_app.py")
    print("│   │")
    print("│   └── examples/             # Exemplos")
    print("│       ├── __init__.py")
    print("│       └── exemplos_basicos.py")
    print("│")
    print("└── docs/                     # Documentação")
    print("    └── guia_rapido.md")

def main():
    """
    Função principal do teste.
    """
    print("🧮 TESTE DA ESTRUTURA REORGANIZADA")
    print("=" * 50)
    
    # Mostrar estrutura
    mostrar_estrutura()
    
    # Testar importações
    if testar_importacoes():
        # Testar funcionalidades
        if testar_funcionalidades():
            print("\n✅ Todos os testes passaram!")
            print("\n🎉 A estrutura está funcionando corretamente!")
            print("\n📖 Para usar o sistema:")
            print("1. python main.py                    # Menu interativo")
            print("2. python src/examples/exemplos_basicos.py  # Exemplos")
            print("3. streamlit run src/interfaces/streamlit_app.py  # Interface web")
            print("4. python src/interfaces/tkinter_app.py     # Interface desktop")
        else:
            print("\n❌ Alguns testes de funcionalidade falharam.")
    else:
        print("\n❌ Alguns testes de importação falharam.")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    main() 