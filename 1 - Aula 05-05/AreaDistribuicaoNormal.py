# Fórmula score z: (x - media) / desvio padrão

from scipy.stats import norm


def calcularScoreZ(x, media, desvio_padrao):
    return (x - media) / desvio_padrao

def menu():
    opc = -1

    print('- Calcular área abaixo da curva normal')
    print('1 - Área a esquerda')
    print('2 - Área direita')
    print('3 - Área central')

    while opc < 1 or opc > 3:
        opc = int(input('Insira a opção: '))
        if opc < 1 or opc > 3:
            print('Opção inválida.')
    
    return opc

def main():
    opc = menu()

    if opc == 1:
        print('\n\n Área a esquerda selecionada\n')

        x = float(input('Insira um valor para x: '))
        media = float(input('Insira um valor para média: '))
        desvio_padrao = float(input('Insira um valor para desvio padrão: '))

        score_z = calcularScoreZ(x, media, desvio_padrao)
        area = norm.cdf(score_z)

        print(f'\nScore z: {score_z}')
        print(f'Área: {area}')
    
    elif opc == 2:
        print('\n\n Área a direita selecionada\n')

        x = float(input('Insira um valor para x: '))
        media = float(input('Insira um valor para média: '))
        desvio_padrao = float(input('Insira um valor para desvio padrão: '))

        score_z = calcularScoreZ(x, media, desvio_padrao)
        area = 1 - norm.cdf(score_z)

        print(f'\nScore z: {score_z}')
        print(f'Área: {area}')
    
    else:
        print('\n\n Área central selecionada\n')

        x1 = float(input('Insira um valor para x1: '))
        x2 = float(input('Insira um valor para x2: '))
        media = float(input('Insira um valor para média: '))
        desvio_padrao = float(input('Insira um valor para desvio padrão: '))

        score_z1 = calcularScoreZ(x1, media, desvio_padrao)
        score_z2 = calcularScoreZ(x2, media, desvio_padrao)

        if score_z1 > score_z2:
            area = norm.cdf(score_z1) - norm.cdf(score_z2)
        else:
            area = norm.cdf(score_z2) - norm.cdf(score_z1)

        print(f'\nScore z1: {score_z1}')
        print(f'\nScore z2: {score_z2}')
        print(f'\nÁrea: {area}')

main()