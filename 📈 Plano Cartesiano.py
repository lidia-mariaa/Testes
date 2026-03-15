#PLANO CARTESIANO

#INÍCIO
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
        quadrante_A = "1"
    elif abscissa_A < 0 and ordenada_A > 0:
        quadrante_A = "2"
    elif abscissa_A < 0 and ordenada_A < 0:
        quadrante_A = "3"
    elif abscissa_A > 0 and ordenada_A < 0:
        quadrante_A = "4"
    else:
        quadrante_A = "origem"

    #QUADRANTE B
    if abscissa_B > 0 and ordenada_B > 0:
        quadrante_B = "1"
    elif abscissa_B < 0 and ordenada_B > 0:
        quadrante_B = "2"
    elif abscissa_B < 0 and ordenada_B < 0:
        quadrante_B = "3"
    elif abscissa_B > 0 and ordenada_B < 0:
        quadrante_B = "4"
    else:
        quadrante_B = "origem"
        
    #DISTÂNCIA ENTRE OS PONTOS
    distancia = ((abscissa_A - abscissa_B)**2 + (ordenada_A - ordenada_B)**2)**0.5

    #PONTO MÉDIO
    ponto_medio_x = ((abscissa_A + abscissa_B)/2)
    ponto_medio_y = ((ordenada_A + ordenada_B)/2)
    
    #EXIBINDO INFORMAÇÕES
    print(f"\n{nome}, o ponto A({abscissa_A},{ordenada_A}) está no quadrante {quadrante_A}, e o ponto B({abscissa_B},{ordenada_B}) está no quadrante {quadrante_B}!")
    print(f"A distância entre esses pontos é: {distancia}")
    print(f"E o ponto médio entre esses pontos é: {ponto_medio_x},{ponto_medio_y}")

    #PONTO 3
    p3_decisão = input("Gostaria de saber se o ponto A e B estão alinhados com um ponto C? ").lower()

    if p3_decisão == "sim":
        abscissa_C = int(input("\nÓtimo!\nInforme a abscissa de C: "))
        ordenada_C = int(input("Informe a ordenada de C: "))

        #DETERMINANTE
        determinante = abscissa_A * (ordenada_B - ordenada_C) + abscissa_B * (ordenada_C - ordenada_A) + abscissa_C * (ordenada_A - ordenada_B)

        if determinante ==  0:
            print("O ponto A, B, C estão alinhados!")
        else:
            print("O ponto A, B, C não estão alinhados.")
    else:
        pass

    #REINICIAR OU NÃO?
    reiniciar = input("\nOque você gostaria de fazer agora?\na)Sair\nb)Reiniciar\n")

    if reiniciar == "a" or reiniciar == "A":
        break
    else:
        pass

print("Obrigada por usar o meu programa! :)")
