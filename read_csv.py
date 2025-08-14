# %%
arquivo = "friends_job.csv"

# step 01: making a list with every single row
with open(arquivo, mode="r", encoding="utf-8") as open_file:
    linhas = open_file.readlines() #transformei em uma lista
print(linhas)

# nome;idade;profission list 00
# matheus;30;wow_player lista 01
# ana banana;28;futura_esposa lista 02
# henriquinho;7;filinho_da_mamae lista 03

# %%
for linha in linhas: 
    print(linha)
    
# %%
# # # dados = {
#     "nome": ["Matheus", "henriquinho", "kaina", "felipe"],
#     "idade": [30, 7, 28, 27],
#     "profissao": ["wow player", "filinho da mamae", "adovogato", "pro player de tibia"]
# }


# %%
# pegar as chaves -> ['nome']
dados_dictionary: dict = {}
keys = linhas[0].strip("\n").split(",")
print(keys)
type(keys) # lista

for k in keys:
    dados_dictionary[k] = []

print(dados_dictionary)

# %%
# pegando os valores
for y in linhas[1:]:
    values = y.strip("\n").split(",")
    for i in range(len(values)):
        dados_dictionary[keys[i]].append(values[i])
dados_dictionary