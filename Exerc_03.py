a = float(input("Digite a nota do aluno A: "))
b = float(input("Digite a nota do aluno B: "))
c = float(input("Digite a nota do aluno C: "))
media = (a+b+c)/3
media_pond = (a*2 + b*3 + c*5)/ (2+3+5)
media_pond = round(float(media_pond), 1)
media = round(float(media), 1)
print(f'MÉDIA PONDERADA = {media_pond}')
print(f'MÉDIA = {media}')
