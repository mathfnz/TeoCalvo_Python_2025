
# %%
file_name = "history.txt"

text = "Ola, obrigado por me mandar mensagem! me chamo Matheus Fernandes."
add = "\nE moro no Brasil! Mas em breve, vou morar com a minha mae em Portugal. Vamos comigo nessa aventura?"
# using "w" if I alter the text will overwrite
# using "a" will add to the current text
with open(file_name, mode="a") as open_file:
    open_file.write(add)
    

