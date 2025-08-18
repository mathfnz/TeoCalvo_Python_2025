# %%

import requests
import json

ceps: list = [
    "02423030",
    "01519000",
    "21870370",
    "58038200"
]
url = "https://viacep.com.br/ws/{cep}/json/"
dados = []
 
for cep in ceps:   
    resposta = requests.get(url.format(cep=cep))
    if resposta.status_code == 200:
        dados.append(resposta.json())
        
# %%
dados

# %%
with open("ceps.json", "w", encoding="UTF-8") as open_file:
    json.dump(dados, open_file)