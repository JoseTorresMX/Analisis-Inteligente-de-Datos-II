# Creamos una lista
numeros = []

# Leemos las entradas del usuario
while True:
    entrada = input("Ingresa un numero, para salir deja en blanco (enter):")

    if entrada == "":
        break  # Salimos del programga
    else:
        valor = float(entrada)
        numeros.append(valor)

# Calculo de promedi de los numeros
if len(numeros) == 0:
    print("No se han ingresado numero o solo han sido ceros.")
else:
    promedio = sum(numeros)/len(numeros)
    print("Promedio de los valores ingresados: ", promedio)

    # Separar los numeros por debajo, igual y por encima del promedio
    debajo_promedio = [num for num in numeros if num < promedio]
    igual_promedio = [num for num in numeros if num == promedio]
    encima_promedio = [num for num in numeros if num > promedio]

    # Mostrar resultados
    print("\nValores por debajo del promedio: ", debajo_promedio)
    print("\nValores igual al promedio: ", igual_promedio)
    print("\nValores por encima del promedio: ", encima_promedio)
