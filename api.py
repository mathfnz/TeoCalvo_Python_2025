# %%

import requests # para realizar requisicoes na web
import json # para tratar json de list/dict para arquivos
from tqdm import tqdm

# %% pegando os urls
ceps: list = [
    "02423030",
    "01519000",
    "21870370",
    "58038200"
]
url = "https://viacep.com.br/ws/{cep}/json/"

dados = [] # armazenamos os ceps em listas

# navegamos nos ceps, verificamos se deu ok (200) e se sim, transformamos em json e adicionamos na lista
for cep in tqdm(ceps):   
    resposta = requests.get(url.format(cep=cep))
    if resposta.status_code == 200:
        dados.append(resposta.json())
        
# %%
dados

# %%
# salvamos essas informacoes em um arquivo para 
with open("ceps.json", "w", encoding="UTF-8") as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)
