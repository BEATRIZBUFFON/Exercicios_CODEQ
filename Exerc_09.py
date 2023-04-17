import pandas as pd
infos = {"DDD": [61, 71, 11, 21, 32, 19, 27, 31, 55],
         "Destino " : ["Brasília", "Salvador", "São Paulo",
                       "Rio de Janeiro", "Juiz de Fora",
                       "Campinas", "Vitória",
                       "Belo Horizonte", "Santa Maria"]}
infos = pd.DataFrame(infos)
ddd = int(input("Informe o DDD: "))
def ddd_destino(ddd):
    if ddd in infos['DDD'].tolist():
        destino = infos.loc[infos['DDD'] == ddd, 'Destino '].iloc[0]
        return destino
    else:
        return "O DDD não está cadastrado."
print(f'Seu DDD é referente ao destino: {ddd_destino(ddd)}.')
