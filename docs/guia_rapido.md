# Guia Rápido - Sistema de Geometria Analítica

## 🚀 Início Rápido

### 1. Instalação
```bash
pip install -r requirements.txt
```

### 2. Executar o Sistema
```bash
python main.py
```

## 📋 Funcionalidades Principais

### Operações com Matrizes
```python
from src.core import *

# Criar matriz
A = np.array([[1, 2], [3, 4]])

# Operações básicas
det = determinante(A)           # Determinante
inv = inversa_matriz(A)         # Inversa
escada = forma_escada(A)        # Forma escada
posto = calcular_posto(A)       # Posto
```

### Operações com Vetores
```python
from src.core import *

u = np.array([1, 1, 0])
v = np.array([-1, 1, 0])

# Operações vetoriais
soma = soma_vetores(u, v)       # Soma
prod_esc = produto_escalar(u, v) # Produto escalar
prod_vet = produto_vetorial(u, v) # Produto vetorial
angulo = angulo_entre_vetores(u, v) # Ângulo
```

### Geometria Analítica
```python
from src.core import *

# Retas
ponto = np.array([0, 0, 0])
vetor = np.array([1, 0, 0])
eq_param = equacao_parametrica_reta(ponto, vetor)

# Planos
normal = np.array([1, 1, 1])
eq_cart = equacao_cartesiana_plano(ponto, normal)
```

### Visualização
```python
from src.visualization import *

# Curvas básicas
plotar_elipse(3, 2, title="Elipse")
plotar_parabola(2, title="Parábola")
plotar_circulo(2, title="Círculo")

# Curva polar
def r_func(theta):
    return np.cos(3 * theta)
plotar_curva_polar(r_func, title="Curva Polar")
```

## 🖥️ Interfaces

### Interface Web (Streamlit)
```bash
streamlit run src/interfaces/streamlit_app.py
```

### Interface Desktop (Tkinter)
```bash
python src/interfaces/tkinter_app.py
```

## 📚 Exemplos Completos

Execute os exemplos para ver todas as funcionalidades:
```bash
python src/examples/exemplos_basicos.py
```

## 🔧 Dicas de Uso

1. **Matrizes**: Use `np.array()` para criar matrizes
2. **Vetores**: Representados como arrays numpy
3. **Sistemas**: Use matriz aumentada (última coluna = termos independentes)
4. **Visualização**: Funções retornam figuras matplotlib que podem ser salvas

## ❓ Problemas Comuns

### Erro de Importação
```python
# Adicione ao início do script:
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
```

### Matriz não Invertível
- Verifique se o determinante é zero
- Use `eh_invertivel()` para verificar antes de calcular a inversa

### Erro de Dimensões
- Verifique se as matrizes têm dimensões compatíveis
- Para produto vetorial, vetores devem ter 3 componentes 