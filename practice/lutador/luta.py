from lutador import Lutador
from random import randint
from time import sleep

class Luta():
    desafiado = Lutador
    desafiante = Lutador
    rounds = int()
    aprovada = bool()

    def setDesafiado(self, l1=Lutador):
        self.desafiado = l1
    
    def marcarLuta(self, l1=Lutador, l2=Lutador):
        if l1.categoria == l2.categoria and l1.nome != l2.nome:
            self.aprovada = True
            self.desafiado = l1
            self.desafiante = l2
        else:
            self.aprovada = False
            self.desafiado = None
            self.desafiante = None

    def lutar(self):
        if self.aprovada:
            print(f'---DESAFIADO---')
            self.desafiado.apresentar()
            print(F'---DESAFIANTE---')
            self.desafiante.apresentar()
            print(F'!!!!!Fight!!!!')
            sleep(1)
            print(F'1...')
            sleep(1)
            print(f'2...')
            sleep(1)
            vencedor = randint(0, 2)
            if vencedor == 0: #Empate
                print(f'Empate entre {self.desafiado.nome} e {self.desafiante.nome}!!!')
                self.desafiado.empatarLuta()
                self.desafiante.empatarLuta()
            elif vencedor == 1: #desafiado ganhou
                print(f'{self.desafiado.nome} ganhou!!!')
                self.desafiado.ganharLuta()
                self.desafiante.perderLuta()
            elif vencedor == 2: #desafiante ganhou
                print(f'{self.desafiante.nome} ganhou!!!')
                self.desafiado.perderLuta()
                self.desafiante.ganharLuta()        
        else:
            print(f'Luta não foi aprovada')