import math
a = float(input("Digite um valor para A: "))
b = float(input("Digite um valor para B: "))
c = float(input("Digite um valor para C: "))

raiz = b**2 - 4*a*c
def raiz_neg(raiz):
    if raiz < 0:
        return "Impossível de calcular."
    else:
        raiz1 = -b + math.sqrt(raiz) / 2*a
        raiz2 = -b - math.sqrt(raiz) / 2*a
        print(f'R1 = {raiz1:.5f}. R2 = {raiz2:5f}')
raiz_neg(raiz)
