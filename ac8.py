# 1 

#figurinhas

def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

# Número de casos de teste
N = int(input())

# Para cada caso de teste
for _ in range(N):
    F1, F2 = map(int, input().split())
    max_pilha = mdc(F1, F2)
    print(max_pilha)


# 2

#dama

def min_movimentos_dama(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return 0
    elif x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return 1
    else:
        return 2

while True:
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
        break
    else:
        movimentos = min_movimentos_dama(x1, y1, x2, y2)
        print(movimentos)


# 3


#soma de fatoriais

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

while True:
    try:
        M, N = map(int, input().split())
        soma = fatorial(M) + fatorial(N)
        print(soma)
    except EOFError:
        break



# 4
def calcular_dias_comida(C):
    dias = 0
    while C > 1:
        C /= 2  # Blobs come metade do suprimento a cada dia
        dias += 1
    return dias

N = int(input())

for _ in range(N):
    C = float(input())  # Quantidade inicial de comida
    dias = calcular_dias_comida(C)
    print(f"{dias} dias")


# 5

#frequencia de numeros

# Número de valores a serem lidos
N = int(input())


contador = {}

for _ in range(N):
    valor = int(input())
    if valor in contador:
        contador[valor] += 1
    else:
        contador[valor] = 1


for chave in sorted(contador.keys()):
    print(f"{chave} aparece {contador[chave]} vez(es)")

# 6

#primo rapido

import math

def eh_primo(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

N = int(input())

for _ in range(N):
    x = int(input())
    if eh_primo(x):
        print("Prime")
    else:
        print("Not Prime")


# 7


#cara ou coroa

while True:
    N = int(input())
    
    if N == 0:
        break
    
    resultados = list(map(int, input().split()))
    
    vitorias_maria = 0
    vitorias_joao = 0
    
    for resultado in resultados:
        if resultado == 0:
            vitorias_maria += 1
        else:
            vitorias_joao += 1
    
    print(f"Mary won {vitorias_maria} times and John won {vitorias_joao} times")


# 8

#Funções

def r(x, y):
    return (3*x)**2 + y**2

def b(x, y):
    return 2*(x**2) + (5*y)**2

def c(x, y):
    return -100*x + y**3

N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    
    resultado_r = r(x, y)
    resultado_b = b(x, y)
    resultado_c = c(x, y)
    
    if resultado_r > resultado_b and resultado_r > resultado_c:
        print("Rafael ganhou")
    elif resultado_b > resultado_r and resultado_b > resultado_c:
        print("Beto ganhou")
    else:
        print("Carlos ganhou")

