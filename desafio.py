# %%
# construa um programa que realiza o sorteio de um numero entre 1 e 15
# o usuario tera 3 chances de acertar o valor
# a cada tentativa voce deve informar se o chute e maior ou menos que o numero sorteado
# caso ele acerte, de os parabens
import random
acertou = False
vidas = 3
numero_sorteado = random.randint(1, 15)
print(numero_sorteado)


# %%

# %%
for i in range(3, 0, -1):
    numero_usuario = int(input("Digite um numero: "))
    if numero_sorteado == numero_usuario:
        print("Voce acertou!")
        print(f"O numero sorteado foi: {numero_sorteado}")
    else:
        numero_sorteado
        print(f"Tente novamente! Voce tem {i} vidas!")
        
print("Obrigado por jogar")
# %%
