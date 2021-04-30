class Aluno (object):
    Nota1 = None
    Nota2 = None
    Media = None
    Status = None

    def __init__(self, Nome):
        self.Nome = Nome
    def inserir_nota(self, Nota1, Nota2):
        self.Nota1 = Nota1
        self.Nota2 = Nota2
    def calcular_media (self):
        self.Media = (self.Nota1+self.Nota2)/2
    def print_info(self):
        if self.Media >= 6:
            self.Status = "Aprovado"
            print (f'Nome: {self.Nome}, Média: {self.Media}, Status: {self.Status}')
        else:
            self.Status = "Reprovado"
            print (f'Nome: {self.Nome}, Média: {self.Media}, Status: {self.Status}')

Aluno1 = Aluno("Victor")
Aluno1.inserir_nota(5,5)
Aluno1.calcular_media()
Aluno1.print_info()
