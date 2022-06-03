from genericpath import exists
import math
from time import sleep

def menu(msg): # Cria uma interface.
    print("-" * 32)
    print(f'{msg}'.center(32))
    print("-" * 32)

def operacoes(a=0): # Verifica qual a operação a ser feita
    operacoes = ['Soma', 'Subtração', 'Multiplicação', 'Divisão', 'Potenciação', 'Raiz']
    # Se o número no sistema for inteiro, a opção do Fatorial é possível, se não, ela é retirada.
    if a - int(a) == 0:
        operacoes.append('Fatorial')
    else:
        if 'Fatorial' in operacoes:
            operacoes.pop('Fatorial')
        else:
            pass
    for i, n in enumerate(operacoes):
        print(f'\033[32m{i + 1}\033[m - {n}')
    if a == 0:
        n = int(input('Digite o número da operação: '))
    else:
        n = int(input(f'Qual operação você vai fazer com o número {a:.2f}? '))
    while n > len(operacoes) or n <= 0:
        n = int(input(f'ERRO! Digite um número válido: '))
    return n

def soma(a=0):
    if a != 0:
        b = float(input(f'Por quanto você quer somar {a:.2f}? '))
    else:
        a = float(input('Digite o número a somar: '))
        b = float(input(f'Por quanto você quer somar {a:.2f}? '))
    print('Calculando...')
    sleep(1)
    c = a + b
    return c

def subtracao(a=0):
    if a != 0:
        b = float(input(f'Por quanto você quer subtrair {a:.2f}? '))
    else:
        a = float(input('Digite o número a ser subtraído: '))
        b = float(input(f'Por quanto você quer subtrair {a:.2f}? '))
    print('Calculando...')
    sleep(1)
    c = a - b
    return c

def multiplicacao(a=0):
    if a != 0:
        b = float(input(f'Por quanto você quer multiplicar {a:.2f}? '))
    else:
        a = float(input('Digite o número a ser multiplicado: '))
        b = float(input(f'Por quanto você quer multiplicar {a:.2f}? '))
    print('Calculando...')
    sleep(1)
    c = a * b
    return c

def divisao(a=0):
    if a != 0:
        b = float(input(f'Por quanto você quer dividir {a:.2f}? '))
    else:
        a = float(input('Digite o número a ser dividido: '))
        b = float(input(f'Por quanto você quer dividir {a:.2f}? '))
    print('Calculando...')
    sleep(1)
    c = a / b
    return c

def potenciacao(a=0):
    if a != 0:
        b = float(input(f'Por quanto você quer elevar {a:.2f}? '))
    else:
        a = float(input('Digite o número a ser elevado: '))
        b = float(input(f'Por quanto você quer elevar {a:.2f}? '))
    print('Calculando...')
    sleep(1)
    c = a ** b
    return c

def raiz(a=0):
    if a != 0:
        b = float(input(
            f'Qual o índice para o radicando {a:.2f}? (\033[32m2\033[m = Raiz quadrada, \033[32m3\033[m = Raiz cubica, ...) '))
    else:
        a = float(input('Digite o número a ser o radicando: '))
        b = float(input(
            f'Qual o índice para o radicando {a:.2f}? (\033[32m2\033[m = Raiz quadrada, \033[32m3\033[m = Raiz cubica, ...)'))
    print('Calculando...')
    sleep(1)
    c = a ** (1 / b)
    return c

def fat(a=0):
    if a == 0:
        while True:
            a = input('Digite um número inteiro para ter seu fatorial: ')
            try:
                a = int(a)
            except:
                print(f'ERRO! Digite somente números inteiros! ')
            else:
                print('Calculando...')
                sleep(1)
            if type(a) == int:
                break
    c = 1
    while a != 1:
        c = c * a
        a -= 1
    return c
