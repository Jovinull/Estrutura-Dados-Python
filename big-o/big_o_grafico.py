# Importa a função log da biblioteca math, e as bibliotecas numpy e matplotlib
from math import log
import numpy as np
import matplotlib.pyplot as plt

# Gera 100 números entre 1 e 10 espaçados igualmente
n = np.linspace(1, 10, 100)

# Define os rótulos para os diferentes tipos de complexidade
labels = ['Constant', 'Logarithmic', 'Linear', 'Log Linear', 'Quadratic', 'Cubic', 'Exponential']

# Define as funções de complexidade (Big O) para cada rótulo
big_o = [np.ones(n.shape), np.log(n), n, n * np.log(n), n ** 2, n ** 3, 2 ** n]

# Configura o tamanho do gráfico
plt.figure(figsize=(10, 8))

# Define o intervalo do eixo y de 0 a 100
plt.ylim(0, 100)

# Plota a primeira função (Constant) no gráfico
plt.plot(n, big_o[0])

# Loop sobre as funções de complexidade restantes para plotar no mesmo gráfico
for i in range(len(big_o)):
    plt.plot(n, big_o[i], label=labels[i])

    # Adiciona a legenda ao gráfico
    plt.legend()

    # Adiciona rótulos aos eixos x e y
    plt.ylabel('runtime')
    plt.xlabel('n')
