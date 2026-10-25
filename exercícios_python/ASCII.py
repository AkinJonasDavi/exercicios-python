import pyfiglet

texto = input("Insira uma palavra para converter para ASCII: ")
print(""" - LISTA DE FONTES - 

standard 
slant
3-d
alphabet 
banner3-D 
bubble 
digital 
graffiti 
isometric1 
block

""")
fonte = input("qual fonte você escolhe? ")
print(pyfiglet.figlet_format(texto, font=fonte))