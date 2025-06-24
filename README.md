# Geometria Analítica e Álgebra Linear com Python 🧮

Este repositório reúne scripts e ferramentas interativas para explorar conceitos de **Geometria Analítica** e **Álgebra Linear** com Python. O objetivo é oferecer uma base prática para estudantes, professores e profissionais interessados em cálculos matriciais, resolução de sistemas lineares e visualização gráfica de curvas.

🔗 **Acesse diretamente a interface web interativa no Streamlit:**  
👉 [Resolutor de Matrizes - Rafael Honorato](https://resolutormatrizesrafaelhonorato.streamlit.app/)

---

## 🏗️ Nova Estrutura Organizada

O projeto foi reorganizado para melhor compreensão e manutenção:

```
geometria_analitica/
├── main.py                    # 🚀 Arquivo principal (menu interativo)
├── requirements.txt           # 📦 Dependências do projeto
├── README.md                  # 📖 Documentação
│
├── src/                       # 📁 Código fonte organizado
│   ├── __init__.py           # Pacote principal
│   │
│   ├── core/                 # 🔧 Operações fundamentais
│   │   ├── __init__.py
│   │   ├── matriz_operations.py    # Operações com matrizes
│   │   ├── vector_operations.py    # Operações com vetores
│   │   └── geometric_operations.py # Geometria analítica
│   │
│   ├── visualization/        # 📊 Funções de visualização
│   │   ├── __init__.py
│   │   └── plotting.py       # Plotagem de curvas e gráficos
│   │
│   ├── interfaces/           # 🖥️ Interfaces de usuário
│   │   ├── __init__.py
│   │   ├── streamlit_app.py  # Interface web (Streamlit)
│   │   └── tkinter_app.py    # Interface desktop (Tkinter)
│   │
│   └── examples/             # 📚 Exemplos de uso
│       ├── __init__.py
│       └── exemplos_basicos.py # Demonstrações práticas
│
└── docs/                     # 📋 Documentação adicional
```

---

## ⚙️ Funcionalidades

### 🔢 Operações com Matrizes
- **Forma Escada (Gauss-Jordan)**: Escalonamento para resolver sistemas
- **Matriz Inversa**: Cálculo da inversa, se existir
- **Verificação de Invertibilidade**
- **Cálculo do Posto da Matriz**
- **Resolução de Sistemas Lineares** com matriz aumentada
- **Determinante** (método geral e Regra de Sarrus)
- **Transposta** e **Produto de Matrizes**
- **Verificação de Tipos** (quadrada, simétrica, identidade, etc.)

### ➡️ Operações com Vetores
- **Soma e Multiplicação por Escalar**
- **Produto Escalar e Vetorial**
- **Produto Misto**: Cálculo de volumes em 3D
- **Ângulo entre Vetores**
- **Norma e Vetor Unitário**
- **Projeção Vetorial**
- **Verificações** (ortogonais, paralelos)

### 📐 Geometria Analítica
- **Equações de Retas** (paramétricas e simétricas)
- **Equações de Planos** (paramétricas e cartesianas)
- **Ângulos entre Retas e Planos**
- **Distâncias** (ponto-reta, ponto-plano, entre retas)
- **Interseções** entre planos
- **Verificações** (paralelas, perpendiculares)

### 📊 Visualizações Gráficas
- **Elipses, Parábolas, Hipérboles e Círculos**
- **Curvas Polares**
- **Retas e Vetores**
- **Múltiplas Curvas** no mesmo gráfico
- **Personalização** com cores, títulos e legendas

---

## 🚀 Como Usar

### Pré-requisitos
Tenha o Python instalado. Em seguida, instale as dependências:

```bash
pip install -r requirements.txt
```

### 🎯 Forma Mais Simples - Menu Interativo

Execute o arquivo principal para acessar um menu interativo:

```bash
python main.py
```

O menu oferece 4 opções:
1. **Executar exemplos básicos** - Demonstrações das funcionalidades
2. **Iniciar interface web** - Aplicação Streamlit no navegador
3. **Iniciar interface desktop** - Aplicação Tkinter
4. **Sair**

### 🔧 Uso Direto dos Módulos

#### Importar funcionalidades:
```python
from src.core import *
from src.visualization import *

# Exemplo: operações com matrizes
A = np.array([[1, 2], [3, 4]])
det = determinante(A)
inv = inversa_matriz(A)

# Exemplo: operações com vetores
u = np.array([1, 1, 0])
v = np.array([-1, 1, 0])
angulo = angulo_entre_vetores(u, v)

# Exemplo: visualização
plotar_elipse(3, 2, title="Minha Elipse")
```

#### Executar exemplos:
```bash
python src/examples/exemplos_basicos.py
```

#### Interfaces individuais:
```bash
# Interface web
streamlit run src/interfaces/streamlit_app.py

# Interface desktop
python src/interfaces/tkinter_app.py
```

---

## 💡 Exemplos de Uso

### 📐 Resolução de Sistema Linear

```python
from src.core import resolver_sistema
import numpy as np

# Sistema: 2x - y + 3z = 8
#          -3x - y + 2z = -11
#          -2x + y + 2z = -3

matriz_aumentada = np.array([
    [2, -1, 3, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3]
])

solucao = resolver_sistema(matriz_aumentada)
print(f"Solução: {solucao}")
# Resultado: [2. 3. -1.]
```

### 📈 Gráfico de Elipse

```python
from src.visualization import plotar_elipse

# Elipse com a=3, b=2, centro em (-2, 1)
plotar_elipse(3, 2, -2, 1, title="Elipse Centrada")
```

### ➡️ Operações com Vetores

```python
from src.core import *

u = np.array([1, 1, 0])
v = np.array([-1, 1, 0])

# Produto escalar
prod_escalar = produto_escalar(u, v)

# Ângulo entre vetores
angulo = angulo_entre_vetores(u, v)

# Verificar se são ortogonais
sao_ort = sao_ortogonais(u, v)
```

---

## 🧰 Tecnologias Utilizadas

- **Python** – Linguagem principal
- **NumPy** – Operações matriciais e vetoriais
- **Matplotlib** – Visualizações gráficas
- **Streamlit** – Interface web interativa
- **Tkinter** – Interface desktop
- **SymPy** – Cálculos simbólicos

---

## 📚 Fontes e Referências

Baseado nos conteúdos do blog de Leandro Cruvinel:  
[Geometria Analítica com Python – Parte 1](https://leandrocruvinel.medium.com/geometria-anal%C3%ADtica-com-python-parte-1-90554f3e862c)

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests com sugestões, melhorias ou novos exemplos.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).