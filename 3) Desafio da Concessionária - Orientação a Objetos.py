class Carro(object):
    comprado = False
    ligado = False
    testdrive = False
    
    def __init__(self, estado, modelo, ano):
        self.estado = estado
        self.modelo = modelo
        self.ano = ano    
    
    def Printar(self):
        print(f'Nome do carro: {self.modelo}\nEstado do carro: {self.estado}\nAno do carro: {self.ano}')
    
    def Comprar(self):
        if self.comprado == False:
            self.comprado = True
            print (f'O carro {self.modelo},{self.ano},{self.estado} foi comprado!')
        else:
            print (f'O carro {self.modelo} desejado já foi comprado.')
    
    def LigaDesliga (self):
        if self.ligado == False:
            self.ligado = True
            print (f'O carro {self.modelo} foi ligado.')
        else:
            print (f'O carro {self.modelo} já está ligado e pronto para uso.')

    def Testdrive(self):
        if self.comprado == False and self.ligado == True:
            testdrive = True
            print ('Test drive sendo realizado!')
        else:
            print (f'O carro {self.modelo} já foi comprado ou está desligado.')
    
    def Dirigir(self):
        if self.comprado == True and self.ligado == True:
            print (f'O carro {self.modelo} está sendo dirigido normalmente.')
        else:
            print (f'O carro {self.modelo} não foi comprado ou não está ligado, não possível ser dirigido.')

    def Acelerar(self):
        if self.comprado == True and self.testdrive == False:
            print (f'O carro {self.modelo} está em aceleração.')
        else:
            print (f'O carro {self.modelo} deve ser comprado antes de ser acelerado.')


carro1 = Carro('Semi-novo', 'BMW', '2019')
carro2 = Carro('Usado', 'Corsa', '2011')
carro3 = Carro ('Usado', 'Fusca', '1985')

carro3.LigaDesliga()
carro3.Testdrive()
carro3.Acelerar()
carro3.Dirigir()
print(carro3.estado)
