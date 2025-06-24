#!/usr/bin/env python3
"""
Sistema de Geometria Analítica - Arquivo Principal
Ponto de entrada principal para o sistema
"""

import sys
import os

# Adicionar o diretório src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def mostrar_menu():
    """
    Mostra o menu principal do sistema.
    """
    print("🧮 SISTEMA DE GEOMETRIA ANALÍTICA")
    print("=" * 50)
    print("Escolha uma opção:")
    print("1. Executar exemplos básicos")
    print("2. Iniciar interface web (Streamlit)")
    print("3. Iniciar interface desktop (Tkinter)")
    print("4. Sair")
    print("=" * 50)

def executar_exemplos():
    """
    Executa os exemplos básicos do sistema.
    """
    try:
        from examples.exemplos_basicos import main as executar_exemplos_basicos
        executar_exemplos_basicos()
    except ImportError as e:
        print(f"Erro ao importar exemplos: {e}")
        print("Certifique-se de que todas as dependências estão instaladas.")

def iniciar_interface_web():
    """
    Inicia a interface web com Streamlit.
    """
    try:
        import subprocess
        import sys
        
        # Verificar se streamlit está instalado
        try:
            import streamlit
        except ImportError:
            print("❌ Streamlit não está instalado!")
            print("Instale com: pip install streamlit")
            return
        
        print("🌐 Iniciando interface web...")
        print("A aplicação será aberta no seu navegador.")
        print("Para parar, pressione Ctrl+C no terminal.")
        
        # Executar streamlit
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", 
            "src/interfaces/streamlit_app.py"
        ])
        
    except Exception as e:
        print(f"Erro ao iniciar interface web: {e}")

def iniciar_interface_desktop():
    """
    Inicia a interface desktop com Tkinter.
    """
    try:
        print("🖥️ Iniciando interface desktop...")
        
        # Importar e executar a interface Tkinter
        from interfaces.tkinter_app import main as executar_tkinter
        executar_tkinter()
        
    except ImportError as e:
        print(f"Erro ao importar interface desktop: {e}")
        print("Certifique-se de que tkinter está disponível.")
    except Exception as e:
        print(f"Erro ao iniciar interface desktop: {e}")

def main():
    """
    Função principal do sistema.
    """
    while True:
        mostrar_menu()
        
        try:
            opcao = input("Digite sua opção (1-4): ").strip()
            
            if opcao == "1":
                print("\n" + "="*50)
                executar_exemplos()
                input("\nPressione ENTER para continuar...")
                
            elif opcao == "2":
                print("\n" + "="*50)
                iniciar_interface_web()
                
            elif opcao == "3":
                print("\n" + "="*50)
                iniciar_interface_desktop()
                
            elif opcao == "4":
                print("\n👋 Obrigado por usar o Sistema de Geometria Analítica!")
                break
                
            else:
                print("❌ Opção inválida! Digite um número de 1 a 4.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")
            input("Pressione ENTER para continuar...")

if __name__ == "__main__":
    main() 