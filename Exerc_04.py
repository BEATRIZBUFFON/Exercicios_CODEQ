
#Exercício 4:
a = float(input("Digite um valor para o ponto A: "))
b = float(input("Digite um valor para o ponto B: "))
c = float(input("Digite um valor para o ponto C: "))
area_triang = a * c
area_triang = round(float(area_triang), 3)
area_circ = 3.14159 * c**2
area_circ = round(float(area_circ), 3)
area_trap = (a+b)*c/2
area_trap = round(float(area_trap), 3)
area_quad = b**2
area_quad = round(float(area_quad), 3)
area_retang = a*b
area_retang = round(float(area_retang), 3)
print(f'A área do triângulo retângulo é de: {area_triang}')
print(f'A área do círculo é de: {area_circ}')
print(f'A área do trapézio é de: {area_trap}')
print(f'A área do quadrado é de: {area_quad}')
print(f'A área do retângulo é de: {area_retang}')
