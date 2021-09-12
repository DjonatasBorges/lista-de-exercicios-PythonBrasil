'''Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.'''
from math import pi


radios = float(input('Digite o raio do círculo: '))
area = pi * (radios ** 2)
print(f'A área do círculo é igual a {area:.2f}')
