# %%
file_name = "file.txt"

# open_file = open(file_name)

# # %%
# # open file esta abrindo o arquivo, declarei ali em cima
# content = open_file.read() 
# print(content)


# # %%
# open_file.close()
# print("File closed")

# %%
with open(file_name) as open_file: #abrindo o conteudo
    content = open_file.read() #lendo o conteudo
print(content)