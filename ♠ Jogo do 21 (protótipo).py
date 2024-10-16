from random import randint, choice
print("Você está no Jogo do 21!")
for i in range(4):
    print(i)
print("Começou! \n")
cartas_j = 0
cartas_pc = 0

pc_opicoes = "puxou", "não puxou", "puxou"

while cartas_j < 21:
    if cartas_pc >= 21:
        break
    pcjogada = choice(pc_opicoes)
    if pcjogada == "puxou":
        print("Seu adiversário puxou uma carta")
        cartas_pca = randint(1,11)
        cartas_pc += cartas_pca
    else:
        print("Seu adiversário não puxou uma carta")
    jogada = input("Quer puxar uma carta? ")
    if jogada == "sim":
        cartas_ja = randint(1,11)
        cartas_j += cartas_ja
        print(f"A carta puxada foi: {cartas_ja}, você tem {cartas_j} pontos")
        print("\nPróxima rodada: \n")
    else:
        print("\nPróxima rodada: \n")
if cartas_j == 21 or cartas_pc > 21:
    print("Você venceu :D")
elif cartas_j > 21 or cartas_pc == 21:
    print("Você perdeu :C")
