entrada = input("Ingresa una letra del afabeto: ")

# Lista de vocales
vocales = ['a', 'e', 'i', 'o', 'u']

# Veirifcamos si la entra es una vocal
if entrada.lower() in vocales:
    print(f"La letra ingresada {entrada}, es una vocal.")
elif entrada.lower() == 'y':
    print(f"A veces la letra {entrada} es una vocal y otras es un consonante")
else:
    print(f"La letra ingresada {entrada}, es una consonante. ")