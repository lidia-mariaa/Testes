senha = "12345"
usuario = "lidia"

while True:
    usuario2 = input("Informe o usuário: ")
    senha2 = input("Informe a senha: ")
    if senha2 != senha or usuario2 != usuario:
        print("\nSenha incorreta ou usuário incorreto :C")
        oque_quer = input("\nOque vc quer?\na)Reescrever\nb)Mudar a senha\n").lower()
        if oque_quer == "b":
            senha_nv = input("Informe a nova senha: ")
            senha = ""
            senha += senha_nv
    else:
        print("\nSenha e usuário correto!")
        break
