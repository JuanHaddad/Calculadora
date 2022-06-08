from funcoes import *

# Calculadora básica em python

menu('CALCULADORA')
op = operacoes() # Chama a função que vai perguntar qual das operações será feita
if op <= 5:
    if op == 1:
        menu('SOMA') # Vai somar dois números
    elif op == 2:
        menu('SUBTRAÇÃO') # Vai subtrair dois números
    elif op == 3:
        menu('MULTIPLICAÇÃO') # Vai multiplicar dois números
    elif op == 4:
        menu('DIVISÃO') # Dividir
    elif op == 5:
        menu('POTENCIAÇÃO') # Um numero elevado a outro
    v = operando(op)

if op == 6:
    menu('RAIZ') # A raiz que o usuário escolher de outro número
    v = raiz()
if op == 7:
    menu('FATORIAL') # Fatorial de um número, só aparece se o número no sistema for inteiro
    v = fat()

print(f'O resultado dessa operação foi \033[36m{v:.2f}\033[m')
while True:
    # Verifica se o usuário quer continuar com o resultado da operação anterior
    r = str(input(f'Quer partir pra outra operação com o valor {v:.2f}? [S/N] ')).upper().strip()[0]
    if r not in 'SN':
        r = str(input('ERRO! Digite S ou N.'))
    if r == 'N':
        break

    print('-'*32)
    op = operacoes(v)
    if op <= 5:
        if op == 1:
            menu('SOMA')
        elif op == 2:
            menu('SUBTRAÇÃO')
        elif op == 3:
            menu('MULTIPLICAÇÃO')
        elif op == 4:
            menu('DIVISÃO')
        elif op == 5:
            menu('POTENCIAÇÃO')
        v = operando(op, v)

    if op == 6:
        menu('RAIZ')
        v = raiz(v)

    elif op == 7:
        menu('FATORIAL')
        v = fat(v)

    print(f'O resultado dessa operação foi \033[36m{v:.2f}\033[m')

print(f'\nSeu valor final é --> \033[35m{v:.2f}\033[m\n<< VOLTE SEMPRE >>')
