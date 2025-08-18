# %%
lista: list = [numero for numero in range(1, 101)]

lista

def eh_par(x):
    return x % 2 == 0

# %%
z = [eh_par(numero) for numero in range(1, 101)]
z

# %%
w = [numero for numero in range(1, 101) if eh_par(numero)]
w