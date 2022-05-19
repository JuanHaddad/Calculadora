from funcoes import *

# Calculadora básica em python

menu('CALCULADORA')
op = operacoes() # Call the def which ask for a option to make basics operations
if op == 1:
    menu('SOMA') 
    v = soma()

elif op == 2:
    menu('SUBTRAÇÃO')
    v = subtracao()

elif op == 3:
    menu('MULTIPLICAÇÃO')
    v = multiplicacao()

elif op == 4:
    menu('DIVISÃO')
    v = divisao()

elif op == 5:
    menu('POTENCIAÇÃO')
    v = potenciacao()

elif op == 6:
    menu('RAIZ')
    v = raiz()

elif op == 7:
    menu('FATORIAL')
    v = fat()

print(f'O resultado dessa operação foi \033[36m{v:.2f}\033[m')
while True:
    try:
        v = int(v)
    except:
        pass
    r = str(input(f'Quer partir pra outra operação com o valor {v:.2f}? [S/N] ')).upper().strip()[0]
    if r not in 'SN':
        r = str(input('ERRO! Digite S ou N.'))
    if r == 'N':
        break

    print('-'*32)
    op = operacoes(v)

    if op == 1:
        menu('SOMA')
        v = soma(v)

    elif op == 2:
        menu('SUBTRAÇÃO')
        v = subtracao(v)

    elif op == 3:
        menu('MULTIPLICAÇÃO')
        v = multiplicacao(v)

    elif op == 4:
        menu('DIVISÃO')
        v = divisao(v)

    elif op == 5:
        menu('POTENCIAÇÃO')
        v = potenciacao(v)

    elif op == 6:
        menu('RAIZ')
        v = raiz(v)

    print(f'O resultado dessa operação foi \033[36m{v:.2f}\033[m')

print(f'\nSeu valor final é --> \033[35m{v:.2f}\033[m\n<< VOLTE SEMPRE >>')
