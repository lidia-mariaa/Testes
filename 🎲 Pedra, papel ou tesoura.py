import random
print("")
print("Hora de jogarmos pedra, papel ou tesoura!!")
print("")
#Opções
escolha = int(input("Escolha sua jogada!! \n (0)Pedra \n (1)Papel \n (2)Tesoura\n-> "))
n0 = "pedra"
n1 = "papel"
n2 = "tesoura"
opcoes = "pedra", "papel", "tesoura"
#Aleatorização:
pc = random.choice(opcoes)
#Testes:
#Se a escolha for inválida...
if 0 > escolha:
    print("jogada inválida >:C")
elif escolha > 2:
    print("jogada inválida >:C")
#Se a escolha for válida...
elif 0 <= escolha <= 2:
    print("")
    print("PEDRA \nPAPEL \nTESOURA!!\n")
    print(f"seu adiversário jogou {pc}!\n")
    #Se o usuário jogar pedra...
    if escolha == 0:
        if pc == n0:
            print("empate!")
        elif pc == n1:
            print("você perdeu... :(")
        elif pc == n2:
            print("você venceu!!")
    #Se o usuário jogar papel...
    if escolha == 1:
        if pc == n0:
            print("você venceu!!")
        elif pc == n1:
            print("empate!")
        elif pc == n2:
            print("você perdeu... :(")
    #Se o usuário jogar tesoura...
    if escolha == 2:
        if pc == n0:
            print("você perdeu... :(")
        elif pc == n1:
            print("você venceu!!")
        elif pc == n2:
            print("empate!")
