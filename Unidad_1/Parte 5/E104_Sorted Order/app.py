
# Creamos una lista para los enteres
enteros = []

# Leer los enteros hasta que se digite 0
while True:
    valores = int(input("Ingresa un entero, el numero 0 es para salir."))

    if valores == 0:
        # Salimos del programa cuando se ingrese un cero.
        break
    else:
        enteros.append(valores)

# Ordenar la lista
enteros.sort()

# Mostrar la lista
print("Valores que entraron:")
for valor in enteros:
    print(valor)
