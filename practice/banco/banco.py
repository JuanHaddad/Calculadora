from conta_banco import Banco

p1 = Banco()
p1.setNumConta(1111)
p1.setDono('Jubileu')
p1.abrirConta('CP')
p1.depositar(50)
p1.pagarMensal()
p1.sacar(179)
p1.estadoAtual()