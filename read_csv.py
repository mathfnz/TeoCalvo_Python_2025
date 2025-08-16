# %%
# Simulação do seu arquivo "dados.csv"
linhas = [
    "nome;idade;profissao\n",
    "Matheus;30;player\n",
    "Felipe;27;gamer\n"
]

dados: dict = {}

# %%

# criar a key do dicionário dados, criando uma lista
keys = linhas[0].strip("\n").split(";")
print(f"As chaves são: {keys}")
print("-" * 20)

# %%
print(f"O dicionário iniciado está assim: {dados}")
for k in keys:
    # Correto: Para cada chave, cria uma entrada no dicionário com uma lista vazia.
    dados[k] = []
print(f"Após o for de inicialização, está assim: {dados}")
print("-" * 20)

# %% 
# CORREÇÃO APLICADA AQUI:
# O próximo passo é colocar os valores dentro das listas.
# Para cada linha de dados (pulando o cabeçalho)...
for linha in linhas[1:]:
    # Remove quebras de linha e divide os valores
    values = linha.strip("\n").split(";")

    # Para cada par de (chave, valor) naquela linha...
    for k, v in zip(keys, values):
        # ...use a chave `k` para encontrar a lista certa no dicionário,
        # e adicione o valor `v` correspondente a ela.
        dados[k].append(v)
    
print(f"Dicionário final: {dados}")