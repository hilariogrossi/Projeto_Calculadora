from Calculadora_Simples.py import Calculadora

c = Calculadora()
x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))
print('Soma: ', c.soma(x, y))
print('Subtração: ', c.subtração(x, y))
print('Multiplicação: ', c.multiplicação(x, y))
print('Divisão: ', c.divisão(x, y))
