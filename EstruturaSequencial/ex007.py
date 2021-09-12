'''Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.'''

side = float(input('Digite o valor do lado do quadrado: '))
area = side ** 2
double_area = area * 2
print(f'A área do quadrado é igual a {area:.2f}')
print(f'O dobro da área do quadrado é igual a {double_area:.2f}')
