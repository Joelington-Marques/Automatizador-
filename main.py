print("*******************************")
print("Bem vindo ao jogo da advinhacao")
print("*******************************")

numero_secreto = 42

chute_str = input("Digite o seu numero:")

print("Voce digitou", chute_str)

chute = int(chute_str)

if(numero_secreto == chute):
    print("voce acertou")
else:
    print("voce errou")