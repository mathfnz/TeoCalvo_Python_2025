# %%
#Escreva um programa que receba uma lista de números do usuário e conte quantas vezes um
# número específico aparece na lista. Solicite ao usuário um número e exiba a contagem.

numbers: list = [1, 2, 3, 3, 2, 1, 1, 1, 1, 1, 5, 6, 7, 7, 6, 5]

number_user = float(input("Type a number: "))
print(f"{number_user} yout number")
count = 0

for number in numbers:
    if number == number_user:
        count += 1
print(f"Your number shows {count} times in the list")

#sae
#sae
#sae
#sae