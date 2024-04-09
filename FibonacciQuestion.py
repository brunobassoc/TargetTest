#  2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será \
#  a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), \
#  escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci \
#  e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

import math

def isPerfectSquare(x):
    sqrt_x = int(math.sqrt(x))
    return sqrt_x * sqrt_x == x

def isFibonacci(n):
    return isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4)

numberInfo = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

if isFibonacci(numberInfo):
    print(numberInfo, "pertence à sequência de Fibonacci.")
else:
    print(numberInfo, "não pertence à sequência de Fibonacci.")
