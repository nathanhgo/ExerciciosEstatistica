# Margem de erro: Desvio padrão / raiz do tamanho da amostra * score z de 95%

# Nível de confiança de 95%: 1.96

import numpy as np

array_alturas = np.random.normal(loc=1.60, scale=0.1, size=100)
n = len(array_alturas)
media = np.mean(array_alturas)
desvio_padrao = np.std(array_alturas, ddof=1)

erro_padrao = desvio_padrao / np.sqrt(n)

valor_critico = 1.96

margem_erro = valor_critico * erro_padrao

limite_inferior_ic = media - margem_erro
limite_superior_ic = media + margem_erro

print('Média: ', media)
print('Desvio padrão: ', desvio_padrao)
print('Erro padrão: ', erro_padrao)
print('Limite do i.c inferior: ', limite_inferior_ic)
print('Limite do i.c superior: ', limite_superior_ic)