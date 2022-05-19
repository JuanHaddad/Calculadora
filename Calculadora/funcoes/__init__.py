import math

def menu(msg):
    print("-" * 32)
    print(f'{msg}'.center(32))
    print("-" * 32)

def operacoes(a=0):
    operacoes = ['Soma', 'Subtração', 'Multiplicação', 'Divisão', 'Potenciação', 'Raiz']
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
        b = float(input(f'Por quanto você quer somar {a}? '))
    else:
        a = float(input('Digite o número a somar: '))
        b = float(input(f'Por quanto você quer somar {a}? '))
    c = a + b
    return c

def subtracao(a=0):
    if a != 0:
        b = float(input(f'Por quanto você quer subtrair {a}? '))
    else:
        a = float(input('Digite o número a ser subtraído: '))
        b = float(input(f'Por quanto você quer subtrair {a}? '))
    c = a - b
    return c

def multiplicacao(a=0):
    if a != 0:
        b = float(input(f'Por quanto você quer multiplicar {a}? '))
    else:
        a = float(input('Digite o número a ser multiplicado: '))
        b = float(input(f'Por quanto você quer multiplicar {a}? '))
    c = a * b
    return c

def divisao(a=0):
    if a != 0:
        b = float(input(f'Por quanto você quer dividir {a}? '))
    else:
        a = float(input('Digite o número a ser dividido: '))
        b = float(input(f'Por quanto você quer dividir {a}? '))
    c = a / b
    return c

def potenciacao(a=0):
    if a != 0:
        b = float(input(f'Por quanto você quer elevar {a}? '))
    else:
        a = float(input('Digite o número a ser elevado: '))
        b = float(input(f'Por quanto você quer elevar {a}? '))
    c = a ** b
    return c

def raiz(a=0):
    if a != 0:
        b = float(input(
            f'Qual o índice para o radicando {a}? (\033[32m2\033[m = Raiz quadrada, \033[32m3\033[m = Raiz cubica, ...) '))
    else:
        a = float(input('Digite o número a ser o radicando: '))
        b = float(input(
            f'Qual o índice para o radicando {a}? (\033[32m2\033[m = Raiz quadrada, \033[32m3\033[m = Raiz cubica, ...)'))
    c = a ** (1 / b)
    return c
