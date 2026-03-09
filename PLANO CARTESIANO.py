def espaços():
    print("-"*50)

espaços()
print("Bem vindo ao programa de Plano Cartesiano da Lídia :D")
espaços()

nome = input("Qual o seu nome? ")
print("")
print(f"{nome}, vamos definir as abscissas e ordenadas dos pontos A e B do seu plano cartesiano!")

while True:
    #PONTO A
    abscissa_A = int(input("\nPrimeiro, vamos definir o ponto A!\nInforme a abscissa de A: "))
    ordenada_A = int(input("Informe a ordenada de A: "))

    #PONTO B
    abscissa_B = int(input("\nAgora o ponto B!\nInforme a abscissa de B: "))
    ordenada_B = int(input("Informe a ordenada de B: "))
    
    #QUADRANTE A
    if abscissa_A > 0 and ordenada_A > 0:
        quadrante_A = "1º"
    elif abscissa_A < 0 and ordenada_A > 0:
        quadrante_A = "2º"
    elif abscissa_A < 0 and ordenada_A < 0:
        quadrante_A = "3º"
    elif abscissa_A > 0 and ordenada_A < 0:
        quadrante_A = "4º"

    #QUADRANTE B
    if abscissa_B > 0 and ordenada_B > 0:
        quadrante_B = "1º"
    elif abscissa_B < 0 and ordenada_B > 0:
        quadrante_B = "2º"
    elif abscissa_B < 0 and ordenada_B < 0:
        quadrante_B = "3º"
    elif abscissa_B > 0 and ordenada_B < 0:
        quadrante_B = "4º"
        
    #DISTÂNCIA ENTRE OS PONTOS
    distancia = ((abscissa_A - abscissa_B)**2 + (ordenada_A - ordenada_B)**2)**0.5
    
    print(f"\n{nome}, o ponto A({abscissa_A},{ordenada_A}) está no {quadrante_A} quadrante, e o ponto B({abscissa_B},{ordenada_B}) está no {quadrante_B} quadrante!")
    print(f"E a distância entre esses ponto é: {distancia}")

    reiniciar = input("\nOque você gostaria de fazer agora?\na)Sair\nb)Reiniciar\n")

    if reiniciar == "a" or reiniciar == "A":
        break
    else:
        pass

print("Obrigada por usar o meu programa! :)")
