# %%

arquivo = "dados.csv"
dados: dict = {}


with open(arquivo, mode="r", encoding="UTF-8") as open_file:
    linhas: list = open_file.readlines()

for linha in linhas:
    print(linha)

# %%

# criar a key do dicionário dados, criando uma lista
keys = linhas[0].strip("\n").split(";")
print(type(keys))

#agora jogar a lista para dentro do dicionario como chaves
# %%
print(f"O dicionário iniciado está assim: {dados}")
for k in keys:
    dados[k] = [] #estou verificando se existe [nome] no dicionario, como não existe, ele joga la dentro. eu tenho que por a lista vazia porque nao pode existir chaves sem valores, entao coloco o valor vazio junto
print(f"Após o for acima está assim agora: {dados}")

# %% 
# próximo passo é colocar dentro da lista:
for linha in linhas[1:]:
    # Remove quebras de linha e divide os valores
    values = linha.strip("\n").split(";")
    for k, v in zip(keys, values):
        # ...use a chave `k` para encontrar a lista certa no dicionário,
        # e adicione o valor `v` correspondente a ela.
        dados[k].append(v)
    
print(f"Dicionário final: {dados}")
# %%
