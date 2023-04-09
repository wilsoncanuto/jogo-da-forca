import random

palavras = ["computador\n","cachorro\n","mulher\n","brasil\n","parede\n"]

palavra = random.choice(palavras)

print(palavra)

tentativas = 0

chances = 8

letras_escolhidas = []

estado_atual =["_"] * len(palavra)

print(" Bem vindo ao jogo da forca\n")

print("Seu objetivo é acerta a palavra secreta")

print("Você terá que acertar uma letra por vez")

print("caso você acerte, a letra será colocada da palavra para você correspondente a letra")

print("caso você erre, você terar uma chance,você tem no maximo", chances, "tentativas\n")

while tentativas < chances:

   letra = input("\nQual a letra você quer tentar!!")
   letras_escolhidas.append(letra)

if letra in palavra:
   print ("Parabéns, você acertou a letra !")
# completar
else:
   print (" Que pena, você errou!")
   tentativas = tentativas + 1

# quantas tentativas ele tem
print ("você já fez", tentativas, "tentativas e ainda tem",chances-tentativas,"tentativas")

# qual é estado atual da palavra
print("Esse é o estado atual")
print("estado_atual")

# quais as letras ele já tentou
print ("as letras que você já tentou são:") 
print (letras_escolhidas)










  






