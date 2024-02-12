menos_deposito = 0.10
mas_deposito = 0.25

menos = int(input("Cuantos envases de 1 litro o menos tiene? "))
mas = int(input("Cuantos envases de mas de 1 litro tiene? "))

reembolso = menos*menos_deposito+mas*mas_deposito

print("El total de tu reembolse sera de: $%.2f" % reembolso)
