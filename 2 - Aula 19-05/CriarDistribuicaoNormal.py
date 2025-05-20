import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

# Criar uma população não-normal (distribuição exponencial)
np.random.seed(42) # Gera uma "semente" para a geração de números aleatórios (Reprodutibilidade)
populacao = np.random.exponential(scale=2, size=100000) # Criação de 100000 valores de forma exponencial
df_pop = pd.DataFrame({'valor': populacao}) # Dataframe armazenando valores

# Amostragem repetida
tamanho_amostra = 50
n_amostras = 1000
medias_amostrais = []

for _ in range(n_amostras): # Calcula a média das amostras e adiciona na lista
    amostra = df_pop['valor'].sample(n=tamanho_amostra, replace=True)
    medias_amostrais.append(amostra.mean())

df_medias = pd.DataFrame({'media_amostral': medias_amostrais})

# Plotar gráficos
fig, axs = plt.subplots(1, 2, figsize=(14, 5))

# População original (não normal)
axs[0].hist(df_pop['valor'], bins=50, color='skyblue', edgecolor='black', density=True)
axs[0].set_title('Distribuição da População (Exponencial)')
axs[0].set_xlabel('Valor')
axs[0].set_ylabel('Frequência')

# Médias amostrais (distribuição aproximada normal)
axs[1].hist(df_medias['media_amostral'], bins=50, color='lightgreen', edgecolor='black', density=True)

# Curva normal teórica para comparação
mu = np.mean(df_medias['media_amostral'])
sigma = np.std(df_medias['media_amostral'])
x = np.linspace(min(df_medias['media_amostral']), max(df_medias['media_amostral']), 100)
axs[1].plot(x, norm.pdf(x, mu, sigma), 'r--', label='Curva Normal')

axs[1].set_title('Distribuição das Médias Amostrais (Aproximadamente Normal)')
axs[1].set_xlabel('Média Amostral')
axs[1].set_ylabel('Frequência')
axs[1].legend()

plt.tight_layout()
plt.show()
