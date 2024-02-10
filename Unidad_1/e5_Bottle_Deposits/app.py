"""En muchas jurisdicciones se añade un pequeño depósito a los envases de bebidas para animar a la gente a reciclarlos.
a reciclarlos. En una jurisdicción concreta, los envases de bebidas de un litro o menos tienen un depósito de 0,10
litro o menos tienen un depósito de 0,10 dólares, y los de más de un litro tienen un depósito de 0,25 dólares.
0,25 $ de depósito.
Escribe un programa que lea el número de envases de cada tamaño del usuario.
Su programa debe continuar calculando y mostrando el reembolso que se recibirá por devolver esos envases.
por devolver esos envases. Formatee la salida de modo que incluya un signo
y muestre siempre exactamente dos decimales."""

menos_deposito = 0.10
mas_deposito = 0.25

menos = int(input("Cuantos envases de 1 litro o menos tiene? "))
mas = int(input("Cuantos envases de mas de 1 litro tiene? "))

reembolso = menos*menos_deposito+mas*mas_deposito

print("El total de tu reembolse sera de: $%.2f" % reembolso)
