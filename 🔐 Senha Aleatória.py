import random
print("_"*48, "\n")
#Caracteres possíveis na senha:
x = "abcdefghijklmnqoprstuvwxyzABCDEFGHIJKLMNQOPRSTUVWXYZ1234567890"
#Quantidade de caracteres:
z = int(input("Informe a quantidade de caracteres da sua senha: "))
#Aleatorização dos caracteres:
a = random.choice(x)
b = random.choice(x)
c = random.choice(x)
d = random.choice(x)
e = random.choice(x)
f = random.choice(x)
g = random.choice(x)
h = random.choice(x)
i = random.choice(x)
j = random.choice(x)
k = random.choice(x)
l = random.choice(x)
m = random.choice(x)
n = random.choice(x)
p = random.choice(x)
q = random.choice(x)
#Testes para definir a quantidade de caracteres:
if z == 6:
    print(f"Sua senha é: {a}{b}{c}{d}{e}{f}")
elif z == 7:
    print(f"Sua senha é: {a}{b}{c}{d}{e}{f}{g}")
elif z == 8:
    print(f"Sua senha é: {a}{b}{c}{d}{e}{f}{g}{h}")
elif z == 9:
    print(f"Sua senha é: {a}{b}{c}{d}{e}{f}{g}{h}{i}")
elif z == 10:
    print(f"Sua senha é: {a}{b}{c}{d}{e}{f}{g}{h}{i}{j}")
elif z == 11:
    print(f"Sua senha é: {a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}")
elif z == 12:
    print(f"Sua senha é: {a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}")
elif z == 13:
    print(f"Sua senha é: {a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}{m}")
elif z == 14:
    print(f"Sua senha é: {a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}{m}{n}")
elif z == 15:
    print(f"Sua senha é: {a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}{m}{n}{p}")
elif 16 < z:
    print("Essa quantidade de caracteres é inválida :C")
elif z < 6:
    print("Essa quantidade de caracteres é inválida :C")
else:
    print(f"Sua senha é: {a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}{m}{n}{p}{q}")
print("_"*48)
