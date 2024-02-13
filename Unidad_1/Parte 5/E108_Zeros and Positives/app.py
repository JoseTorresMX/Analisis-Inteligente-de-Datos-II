# Creamos listas para los negativos. positivos y ceros
positivos = []
negativos = []
ceros = []

# Capturar los enteros entrantes
while True:
    entrada = input(
        "Ingrese un numero entero, dejar en blanco(enter) para salir.")
    if entrada == "":
        break  # Salimos del programa
    else:
        valor = int(entrada)
        if valor < 0:
            negativos.append(valor)
        elif valor == 0:
            ceros.append(valor)
        else:
            positivos.append(valor)

# Mostramos los numeros entrantes
resultado = negativos+ceros+positivos

print("Valores ingresados")
for valor in resultado:
    print(valor)