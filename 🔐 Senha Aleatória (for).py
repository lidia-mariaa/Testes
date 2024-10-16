import random

#A variável senha ficou armanado "" pois o usuário ainda vai definir a quantidade de caracteres e o randow.choice
#ainda vai decidir qual vai ser o caractere que vai ocupar cada espaço

senha = ""
caractere = "abcdfghijklmnopqrtyxyz1234567890"
x = int(input("Informe a quantidade de caracteres da sua senha:"))

for i in range(x):
    a = random.choice(caractere)
    senha += a

print(senha)

#linha 10 -> se x = 2 então vai ser armazenado na variável "i" o número 0 (ficano 0)
#linha 11 -> "a" vai aleatorizar o caractere
#linha 12 -> vai ser adicionado na variável "senha" o caractere sorteado na variável "a" (ficando: a)

#como x = 2 o loop for vai repetir essas 3 linhas mais uma vez

#linha 10 -> vai ser somado na variável "i" o número 1 (ficando 1, pois 0 + 1 = 0)
#linha 11-> "a" vai aleatorizar o caractere
#linha 12 -> vai ser adicionado na variável "senha" o caractere sorteado na variável "a" (vai ficar assim: aa)

#agora que o loop for terminou suas repetições podemos passar para a linha 14

#linha 14 -> vai imprimir a senha com a quantidade de caracteres definidos em x e os caracteres em a

#variáveis>
# i -> ficou armazenado o número 1 (pois o range começa a contar do 0)
# a -> ficou armazendo o segundo caractere sorteado, já que o primeiro foi substituido
