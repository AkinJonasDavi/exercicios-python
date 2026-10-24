import turtle

pen = turtle.Turtle()
pen.speed(0)  # Velocidade máxima de desenho
turtle.bgcolor("black")
pen.color("green")

tamanho = 8
for i in range(200):
    pen.forward(tamanho)
    pen.left(200)  # Ângulo de 120 graus forma o triângulo
    tamanho += 6# Aumenta o tamanho a cada linha para criar a espiral

turtle.exitonclick()