import math
x1 = float(input("Digite um valor para o ponto X1: "))
y1 = float(input("Digite um valor para o ponto Y1: "))
x2 = float(input("Digite um valor para o ponto X2: "))
y2 = float(input("Digite um valor para o ponto Y2: "))
raiz = (x2-x1)**2 + (y2-y1)**2
distancia = math.sqrt(raiz)
distancia = round(float(distancia), 4)
print(f'A distância é equivalente a {distancia}.')
