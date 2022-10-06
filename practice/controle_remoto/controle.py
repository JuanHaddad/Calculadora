class Controle:
    volume = int()
    ligado = bool()
    tocando = bool()

    def __init__(self):
        self.volume = 50
        self.tocando = False
        self.ligado = False

    def __getVolume(self):
        return self.volume

    def __getTocando(self):
        return self.tocando

    def __getLigado(self):
        return self.ligado

    def __setVolume(self, v):
        self.volume = v

    def __setTocando(self, t):
        self.tocando = t

    def __setLigado(self, l):
        self.ligado = l

    def ligar(self):
        if self.__getLigado():
            print(f'Já está ligado...')
        else:
            self.__setLigado(True)
            print(f'Ligandooo!!!')

    def desligar(self):
        if not self.__getLigado():
            print(f'Já está desligado...')
        else:
            self.__setLigado(False)
            print(f'Desligandoo.')

    def abrirMenu(self):
        print(F'-------MENU-------')
        print(F'Está ligado? {self.__getLigado()}')
        print(F'Está tocando? {self.__getTocando()}')
        print(f'Volume: ', end='')
        for i in range(0,self.__getVolume(), 10):
            print(f'|',end='')

    def maisVolume(self):
        if self.__getLigado():
            self.__setVolume(self.__getVolume() + 5)
            print(f'Volume: {self.__getVolume()}')
        else:
            print(f'Controle desligado...')

    def menosVolume(self):
        if self.__getLigado():
            self.__setVolume(self.__getVolume() - 5)
            print(f'Volume: {self.__getVolume()}')

    def play(self):
        if self.__getLigado():
            if not self.__getTocando():
                self.__setTocando(True)
                print(f'>play')
            else:
                print(f'Já está tocando.')
        else:
            print(f'Está desligado.')

    def pause(self):
        if self.__getLigado():
            if self.__getTocando():
                self.__setTocando(False)
                print(F'<pause')
            else:
                print(F'Já está pausado.')
        else:
            print(f'Está desligado.')

c1 = Controle()
c1.ligar()
c1.maisVolume()
c1.menosVolume()
c1.abrirMenu()