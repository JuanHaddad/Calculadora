class Banco:
    numConta = int()
    tipo = str()
    dono = str()
    saldo = float()
    status = bool()
    
    def __init__(self) -> None:
        self.status = False
        self.saldo = 0

    def estadoAtual(self):
        print(f'----------------------')
        print(F'Conta: {self.getNumConta()}')
        print(F'Tipo: {self.getTipo()}')
        print(f'Dono: {self.getDono()}')
        print(f'Saldo: {self.getSaldo()}')
        print(f'Status: {self.getStatus()}')

    def abrirConta(self, tipo):
        tipo = tipo.upper()
        self.status = True
        if tipo not in "CCCP":
            print(f'Tipo da conta deve ser CC ou CP.')
        else:
            self.tipo = tipo
            if self.tipo == 'CC':
                self.saldo = 50
            elif self.tipo == 'CP':
                self.saldo = 150

    def fecharConta(self):
        if self.status == False:
            print(f'Conta já fechada...')
        else:
            if self.saldo != 0:
                print(f'Erro ao fechar a conta, saldo não zerado.')
            else:
                self.status == False
                print(f'Conta fechada com sucesso.')

    def depositar(self, valor):
        if self.status == False:
            print(f'Conta fechada, depósito negado.')
        else:
            self.saldo += valor
            print(f'Depósito de R${valor:.2f} na conta de {self.dono} realizado com sucesso.')

    def sacar(self, valor):
        if self.getStatus() == False:
            print(f'Conta fechada, saque negado.')
        else:
            if self.getSaldo() < valor:
                print(f'Saldo insuficiente para saque de R${valor:.2f}')
            else:
                self.setSaldo(self.getSaldo() - valor)
                print(f'Saque de R${valor:.2f} na conta de {self.getDono()} realizado com sucesso.')

    def pagarMensal(self):
        v = 0
        if self.getStatus() == False:
            print(f'Conta fechada, impossível pagar mensalidade.')
        else:
            if self.getTipo() == "CC":
                v = 12
            elif self.getTipo() == "CP":
                v = 20
            if self.getSaldo() < v:
                print(f'Saldo insuficiente para pagar a mensalidade.')
            else:
                self.setSaldo(self.getSaldo() - v)
                print(f'Mensalidade de R${v:.2f} paga com sucesso.')
    
    def getNumConta(self):
        return self.numConta
    
    def setNumConta(self, num):
        self.numConta = num

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        tipo = tipo.upper()
        if tipo is not "CC" or tipo is not 'CP':
            print(f'Tipo de conta não identificado. Tente CC ou CP')
        else:
            self.tipo = tipo
    
    def getDono(self):
        return self.dono

    def setDono(self, nome):
        self.dono = nome

    def getSaldo(self):
        return self.saldo
    
    def setSaldo(self, valor):
        self.saldo = valor
    
    def getStatus(self):
        return self.status

    def setStatus(self, stts):
        self.status = stts