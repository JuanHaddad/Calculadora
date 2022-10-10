from lutador import Lutador
from luta import Luta

l = []
for i in range(0, 6):
    if i == 0:
        lut = Lutador("Pretty Boy",
                       "França",
                        31, 1.75, 68.9,
                        11, 3, 1) 
        l.append(lut)
    elif i == 1:
        lut = Lutador('Putscript', 
                       'Brasil', 
                       29, 1.68, 57.8,
                       14, 2, 3)
        l.append(lut)
                    
    elif i == 2:
        lut = Lutador('Snapshadow',
                       'EUA',
                       35, 1.65, 80.9,
                       12, 2, 1)
        l.append(lut)
    elif i == 3:
        lut = Lutador('Dead Code',
                       'Austrália',
                       28, 1.93, 81.6,
                       13, 0, 2)
        l.append(lut)
    elif i == 4:
        lut = Lutador('UFOCobol',
                       'Brasil',
                       37, 1.70, 119.3,
                       5, 4, 3)
        l.append(lut)
    elif i == 5:
        lut = Lutador('Nerdaart',
                       'EUA',
                       30, 1.81, 105.7,
                       12, 2, 4)
        l.append(lut)    

lul = Luta()

lul.marcarLuta(l[3], l[2])
lul.lutar()

l[3].status()
l[2].status()