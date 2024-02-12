def redondear(monto):
    centavos_totales = round(monto*100)
    resto = centavos_totales % 5

    if resto < 2.5:
        monto_redondeado = centavos_totales-resto
    else:
        monto_redondeado = centavos_totales+(5-resto)

    monto_redondeado /= 100.0


def main():
    total = 0.0

    while True:
        print("Puedes no ingresar nada y salir del programa")
        precio_usuario = input("Ingresa el precion del articulo: ")

        if not precio_usuario:
            break

        try:
            precio = float(precio_usuario)
            total += precio
        except ValueError:
            print("Ingresa un valor numerico valido.")

    # Mostrar el costo toal de los articulos
    print(f"\nCosto total de los articulos: ${total:.2f}")

    # Calculo del monto si se paga en efectivo.
    # Se redondea al mas cercano
   # monto_efectivo = redondear(total)
    # print(f"Monto debido en efectivo ${monto_efectivo:.2f}")


if __name__ == "__main__":
    main()
