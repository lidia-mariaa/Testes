alunos = []

for _ in range(3):
    aluno = {"nome": "", "matricula": ""}
    aluno["nome"] = input("Informe o nome: ")
    aluno["matricula"] = input("Informe a matrícula: ")
    alunos.append(aluno)

m = input("Informe a matrícula do aluno que você quer saber o nome:")
for valor in alunos:
    if valor["matricula"]== m:
        print(valor["nome"])
