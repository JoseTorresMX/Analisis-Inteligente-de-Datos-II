def calcular_mediana(num1, num2, num3):
    # Ordenar los numero de forma ascendente
    nums_orden = sorted([num1, num2, num3])

    # Dovolver el num del medio
    return nums_orden[1]


def main():
    # Obtener datos desl usuario
    num1 = float(input("Ingremar el primer valor: "))
    num2 = float(input("Ingremar el segundo valor: "))
    num3 = float(input("Ingremar el tercer valor: "))

    # MMArcar los valores a la funcion
    mediana = calcular_mediana(num1, num2, num3)

    # Mostrar el resultado
    print(f"La mediana entre {num1}, {num2} y {num3} es {mediana}")


if __name__ == "__main__":
    main()
