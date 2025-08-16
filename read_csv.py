# %%

arquivo = "dados.csv"

with open(arquivo, mode="r", encoding="UTF-8") as open_file:
    linhas: list = open_file.readlines()

for linha in linhas:
    print(linha)

# %%
dados: dict = {}

# criar a key do dicionário dados, criando uma lista
keys = linhas[0].strip("\n").split(";")
print(type(keys))

#agora jogar a lista para dentro do dicionario como chaves
# %%
for k in keys:
    dados[k] = [] #estou verificando se existe [nome] no dicionario, como não existe, ele joga la dentro. eu tenho que por a lista vazia porque nao pode existir chaves sem valores, entao coloco o valor vazio junto
    
dados