print("*******************************")
print("Bem vindo ao jogo da advinhacao")
print("*******************************")

numero_secreto = 42

chute_str = input("Digite o seu numero:")


Trabalhar essas variaveis aqui.

print("Voce digitou", chute_str)

chute = int(chute_str)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if(numero_secreto == chute):
    print("voce acertou")
else:
    if(chute > numero_secreto):
        print("Voce errou! O seu chute foi maior do que o numero secreto")
    elif(chute < numero_secreto):
        print("Voce errou! O seu chute foi menor do que o numero secreto")

print("Fim do jogo")