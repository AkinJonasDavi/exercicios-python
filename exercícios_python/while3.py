senha_correta = "python123"
tentativas_restantes = 3

while tentativas_restantes > 0:
    tentativa = input("Digite a senha secreta: ")
    
    if tentativa == senha_correta:
        print("Acesso concedido! Bem-vindo ao sistema.")
        break  # Sai do loop imediatamente se acertar
    else:
        tentativas_restantes -= 1
        if tentativas_restantes > 0:
            print(f"Senha incorreta! Você ainda tem {tentativas_restantes} tentativa(s).")
        else:
            print("Acesso negado por excesso de tentativas!")