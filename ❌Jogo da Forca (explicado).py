print("_"*25, "\nJogo da Forca:\n")

#A palavra escolhida foi "lid"
palavra = "lid"

#Escrevi uma variável para cada letra:
l = "_"
i = "_"
d = "_"

#Uma que remete a cada letra acertada:
o = 0

#Uma para as chances do usuário, outra para armazenar a quantidade de letras erradas:
chances_use = 7
letras_erradas = 0

#E outra para armazenar as letras escolhidas que não se encontram na palavras (letras erradas):
l_e = ""

print(l, i, d)

#O while True vai repetir o código ou até o usuário perder ou até o usuário ganhar
#Essa repetição pode se encerrar na linha 82 ou 87, onde se tem o break
#O break vai tranformar o True em False, oque vai encerrar a repetição
while True:
    x = input("\nChute uma letra: ")

    #if para se a letra que o usuário chutar for "l"
    if x == "l":
        #Excluí o "_" da variável 'l' e adicionei a letra "l", indo de: _ _ _  para  l _ _
        l = ""
        l += "l"
        
        #Adicionei 1 a variável 'o', para dizer que o usuário acertou mais uma letra
        o += 1

        print("\nVocê acertou uma letra :>")
        print(f"\nAté agora você errou {letras_erradas} letras, ainda lhe restam {chances_use} chances")
        if letras_erradas >= 1:
            print(f"As letras erradas foram: {l_e}")
        print(l, i, d)
    
    #elif para se a letra que o usuário chutar for "i"
    elif x == "i":
        i = ""
        i += "i"
        o += 1
        print("\nVocê acertou uma letra :>")
        print(f"\nAté agora você errou {letras_erradas} letras, ainda lhe restam {chances_use} chances")
        if letras_erradas >= 1:
            print(f"As letras erradas foram: {l_e}")
        print(l, i, d)
    
    #elif para se a letra que o usuário chutar for "d"
    elif x == "d":
        d = ""
        d += "d"
        o += 1
        print("\nVocê acertou uma letra :>")
        print(f"\nAté agora você errou {letras_erradas} letras, ainda lhe restam {chances_use} chances")
        if letras_erradas >= 1:
            print(f"As letras erradas foram: {l_e}")
        print(l, i, d)
    
    #else para se o usuário errar a letra
    else:
        chances_use -= 1
        print("\nVocê errou a letra :/")
        letras_erradas += 1

        #Adicionei a letra que o usuário errou a variável 'l_e', para depois mostrar ao usuário:
        l_e += x

        print(f"\nAté agora você errou {letras_erradas} letras, ainda lhe restam {chances_use} chances")
        print(f"As letras erradas foram: {l_e}")
        print(l, i, d)
    
    #Um if para se o usuário perder (se acabar suas chances):
    if chances_use == 0:
        print("Você perdeu :C")
        break
    
     #Um if para se o usuário ganhar (acertar todas as letras):
    if o == 3:
        print("Você venceu :D")
        break
