'''Faça um Programa que peça as 4 notas bimestrais e mostre a média.'''


one_grade = float(input('Digite a Primeira Nota do Aluno: '))
two_grade = float(input('Digite a Segunda Nota do Aluno: '))
three_grade = float(input('Digite a Terceira Nota do Aluno: '))
four_grade = float(input('Digite a Quarta Nota do Aluno: '))
average = (one_grade + two_grade + three_grade + four_grade) / 4

print(f'A média do aluno é igual a {average}')
