import math
a = float(input("Digite um valor para A: "))
b = float(input("Digite um valor para B: "))
c = float(input("Digite um valor para C: "))
raiz = b**2 - 4*a*c
raiz = math.sqrt(raiz)
def raiz_neg(raiz):
    if raiz < 0:
        return "Impossível de calcular."
raiz_1 = -b + raiz / 2*a
raiz_2 = -b - raiz / 2*a
raiz_1 = round(float(raiz_1), 5)
raiz_2 = round(float(raiz_2), 5)
print(f'R1 = {raiz_1} e R2= {raiz_2}.')
