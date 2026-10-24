
Nota1 = float(input("Qual a sua nota do 1º semestre? "))
Nota2 = float(input("Qual a sua nota do 2º semestre? "))
Nota3 = float(input("Qual a sua nota do 3º semestre? "))
Nota4 = float(input("Qual a sua nota do 4º semestre? "))

media = ((Nota1+Nota2+Nota3+Nota4)/4)

print(f"Sua média foi: {media:.2f}")

if media >= 7:
    print("Você foi aprovado!!")
elif media >= 6:
    print("Você precisa fazer a recuperação!!")
else:
    print("Reprovado!!")
 
