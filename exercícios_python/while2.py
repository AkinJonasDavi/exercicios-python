senha = ("python")  
c = 3

while c > 0:
  s = input("Qual a sua senha? ")

  if s == senha:
     print("Acesso liberado!!")
     break
  else:
    c -= 1
    if c > 0:
        print(f"Acesso negado, você ainda tem mais {c}.")
    else:
        print("Acesso negado por excesso de tentativas! ")  
        break

 