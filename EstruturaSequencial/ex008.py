'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''

value_hour = float(input('Digite o valor que você ganha por hora trabalhada: '))
amount_hour = float(input('Digite quantas horas você trabalha por mês: '))
total_salary = value_hour * amount_hour
print(f'O seu salário mensal é igual a R${total_salary:.2f}')
