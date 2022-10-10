class Lutador():
    nome = str()
    nacionalidade = str()
    idade = int()
    altura = float()
    peso = float()
    categoria = str()
    vitorias = int()
    derrotas = int()
    empates = int()

    def __getNome(self):
        return self.nome
        
    def __getNacionalidade(self):
        return self.nacionalidade

    def __getIdade(self):
        return self.idade

    def __getAltura(self):
        return self.altura

    def __getPeso(self):
        return self.peso

    def __getCategoria(self):
        return self.categoria

    def __getVitorias(self):
        return self.vitorias

    def __getDerrotas(self):
        return self.derrotas

    def __getEmpates(self):
        return self.empates

    def __setNome(self, n):
        self.nome = n

    def __setNacionalidade(self, n):
        self.nacionalidade = n

    def __setIdade(self, i):
        self.idade = i

    def __setAltura(self, a):
        self.altura = a

    def __setPeso(self, p):
        self.peso = p
        if p <= 68.5:
            c = 'Pena'
        elif p <= 70.3:
            c = 'Leve'
        elif p <= 77.1:
            c = 'Meio-Médio'
        elif p <= 83.9:
            c = 'Médio'
        else:
            c = 'Pesado'
        self.categoria = f'Peso {c}'                

    def __setVitorias(self, v):
        self.vitorias = v

    def __setDerrotas(self, d):
        self.derrotas = d

    def __setEmpates(self, e):
        self.empates = e

    def __init__(self, no, na, id, al, pe, vi, de, em):
        self.__setNome(no)
        self.__setNacionalidade(na)
        self.__setIdade(id)
        self.__setAltura(al)
        self.__setPeso(pe)
        self.__setVitorias(vi)
        self.__setDerrotas(de)
        self.__setEmpates(em)

    def apresentar(self):
        print(f'Lutador: {self.__getNome()}')
        print(f'Origem: {self.__getNacionalidade()}')
        print(F'{self.__getIdade()} anos')
        print(f'{self.__getAltura()}m de altura')
        print(F'{self.__getPeso()}Kg ')
        print(f'Categoria: {self.__getCategoria()}')
        print(F'Vitórias: {self.__getVitorias()}')
    
    def status(self):
        print('-----------------')
        print(f'{self.__getNome()}')
        print(f'É um {self.__getCategoria()}')
        print(f'{self.__getVitorias()} vitórias')
        print(f'{self.__getDerrotas()} derrotas')
        print(f'{self.__getEmpates()} empates')

    def ganharLuta(self):
        self.__setVitorias(self.__getVitorias() + 1)

    def perderLuta(self):
        self.__setDerrotas(self.__getDerrotas() + 1)

    def empatarLuta(self):
        self.__setEmpates(self.__getEmpates() + 1)