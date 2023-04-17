d = float(input("Número do funcionário: "))
a = float(input("Número de horas trabalhadas: "))
b = float(input("Valor recebido por hora: "))
ganho = a*b
ganho = round(float(ganho), 2)
print(f'Número do funcionário: {d}. Salário do funcionário: R$ {ganho}.')
