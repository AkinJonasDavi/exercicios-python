import time

numero = int(input("Digite um número para ver a tabuada: "))

for yuri in range(0, 11):
    resultado = numero * yuri
    time.sleep(0.2)
    print(f"{numero} x {yuri} = {resultado}")


#laço yuri no intervalo(0, 9)
