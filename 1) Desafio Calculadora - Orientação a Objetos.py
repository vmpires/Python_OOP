class Calculadora (object):

    def Soma(self,primeiro_valor,segundo_valor):
        return (primeiro_valor + segundo_valor)    

    def Subt(self,primeiro_valor,segundo_valor):
        return (primeiro_valor - segundo_valor)
      
    def Mult(self,primeiro_valor,segundo_valor):
        return (primeiro_valor * segundo_valor)   

    def Div(self,primeiro_valor,segundo_valor):
        try:
           return(primeiro_valor / segundo_valor)
        except ZeroDivisionError:
            print ('Não existe divisão por 0.')

Calc = Calculadora()
print(Calc.Soma(10,4))
print(Calc.Subt(10, 5))
print(Calc.Mult(5,5))
print(Calc.Div(10,0))