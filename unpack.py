# %% 
# trocando valo de variáveis

a = 1
b = 2

print(f"a antes do unpac: {a}")
print(f"b antes do unpac: {b}")

a, b = b, a
print(f"a depois do unpac: {a}")
print(f"b depois do unpac: {b}")