# %%
person: list = ["Matheus Fernandes", 177, "white", "latino", ["Marina", "Monica", "Bruna Lodi", "Mariana", "Ligia"]]

# first girlfiend
print(person[4][0])

# %%
print(person[0:2])

# %% 
# fatiando lista
# [ start : stop : step] -> se o primeiro estivar em branco comeco no comeco /// -> se o ultimo estiver em branco e ate o fim
print(person[4])
print(person[4][:-2])
print(person[4][-2:])
print(person[4][1: 4: 2])

