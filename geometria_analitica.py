import numpy as np

# Declarando vetor u
vetor_u = np.array([1, -2, 0])

# Declarando vetor v
vetor_v = np.array([0, 2, 2])

# Declarando o vetor w
vetor_w = np.array([1, 2, -1])

# Soma de vetores
soma_vetores = vetor_u + vetor_v
print("Soma dos vetores u e v: ", soma_vetores)

# Multiplicaçao de vetor com escalar
multiplicacao_escalar = 7 * vetor_u
print("Multiplicação do vetor u por 7: ", multiplicacao_escalar)

# Produto escalar de u com v
produto_escalar = np.dot(vetor_u, vetor_v)
print("Produto escalar de u e v: ", produto_escalar)

# Produto vetorial de u com v
produto_vetorial = np.cross(vetor_u, vetor_v)
print("Produto vetorial de u e v: ", produto_vetorial)

# Produto misto de u, v e w
produto_misto = np.linalg.det([
    vetor_u, vetor_v, vetor_w])
print("Produto misto de u, v e w: ", produto_misto)
