print("_"*25, "\nJogo da Forca:\n")
palavra = "lid"
l = "_"
i = "_"
d = "_"
o = 0
chances_use = 7
letras_erradas = 0
l_e = ""
print(l, i, d)
while True:
    x = input("\nChute uma letra: ")
    if x == "l":
        l = ""
        l += "l"
        o += 1
        print("\nVocê acertou uma letra :>")
        print(f"\nAté agora você errou {letras_erradas} letras, ainda lhe restam {chances_use} chances")
        if letras_erradas >= 1:
            print(f"As letras erradas foram: {l_e}")
        print(l, i, d)
    elif x == "i":
        i = ""
        i += "i"
        o += 1
        print("\nVocê acertou uma letra :>")
        print(f"\nAté agora você errou {letras_erradas} letras, ainda lhe restam {chances_use} chances")
        if letras_erradas >= 1:
            print(f"As letras erradas foram: {l_e}")
        print(l, i, d)
    elif x == "d":
        d = ""
        d += "d"
        o += 1
        print("\nVocê acertou uma letra :>")
        print(f"\nAté agora você errou {letras_erradas} letras, ainda lhe restam {chances_use} chances")
        if letras_erradas >= 1:
            print(f"As letras erradas foram: {l_e}")
        print(l, i, d)
    else:
        chances_use -= 1
        print("\nVocê errou a letra :/")
        letras_erradas += 1
        l_e += x
        print(f"\nAté agora você errou {letras_erradas} letras, ainda lhe restam {chances_use} chances")
        print(f"As letras erradas foram: {l_e}")
        print(l, i, d)
    if chances_use == 0:
        print("Você perdeu :C")
        break
    if o == 3:
        print("Você venceu :D")
        break
