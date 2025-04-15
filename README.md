# Geometria Analítica e Álgebra Linear com Python 🧮

Este repositório reúne scripts e ferramentas interativas para explorar conceitos de **Geometria Analítica** e **Álgebra Linear** com Python. O objetivo é oferecer uma base prática para estudantes, professores e profissionais interessados em cálculos matriciais, resolução de sistemas lineares e visualização gráfica de curvas.

🔗 **Acesse diretamente a interface web interativa no Streamlit:**  
👉 [Resolutor de Matrizes - Rafael Honorato](https://resolutormatrizesrafaelhonorato.streamlit.app/)

---

## ⚙️ Funcionalidades

### 🔢 Operações com Matrizes
- **Forma Escada (Gauss-Jordan)**: Escalonamento para resolver sistemas.
- **Matriz Inversa**: Cálculo da inversa, se existir.
- **Verificação de Invertibilidade**
- **Cálculo do Posto da Matriz**
- **Resolução de Sistemas Lineares** com matriz aumentada.

### 📊 Visualizações Gráficas
- **Elipses e Parábolas** em coordenadas cartesianas.
- **Curvas Polares**
- **Personalização** com títulos, legendas e eixos.

### 🧮 Operações com Vetores
- Soma, multiplicação por escalar, produto escalar e vetorial.
- **Produto Misto**: Cálculo de volumes em 3D.

---

## 🧰 Tecnologias Utilizadas

- `Python` – linguagem principal
- `NumPy` – operações matriciais e vetoriais
- `Matplotlib` – visualizações gráficas
- `Streamlit` – interface web interativa

---

## 🚀 Como Usar

### Pré-requisitos
Tenha o Python instalado. Em seguida, instale as dependências:

```bash
pip install numpy matplotlib streamlit
```

### Executando o Projeto

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/geometria_analitica.git
cd geometria_analitica
```

Execute os scripts:

- Scripts de cálculo e visualização:
  ```bash
  python geometria_analitica.py
  ```

- Interface web:
  ```bash
  streamlit run resolutor_matrizes.py
  ```

Ou acesse diretamente:  
👉 [https://resolutormatrizesrafaelhonorato.streamlit.app/](https://resolutormatrizesrafaelhonorato.streamlit.app/)

---

## 💡 Exemplos de Uso

### 📐 Resolução de Sistema Linear

**Entrada:**
```
2  1 -1  8  
-3 -1  2 -11  
-2  1  2 -3
```

**Resultado:**  
```
Solução: [2. 3. -1.]
```

### 📈 Gráfico de Elipse com Matplotlib

```python
a, b, x0, y0 = 3, 2, -2, 1
t = np.linspace(-1, 2 * np.pi, 100)
x = a * np.cos(t) + x0
y = b * np.sin(t) + y0

plt.plot(x, y)
plt.title("Gráfico da Elipse")
plt.axis("equal")
plt.show()
```

---

## 📁 Estrutura do Repositório

```
geometria_analitica/
├── geometria_analitica.py      # Scripts para gráficos e vetores
├── resolutor_matrizes.py       # Interface interativa com Streamlit
├── README.md                   # Documentação do projeto
└── requirements.txt            # Dependências do projeto
```

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