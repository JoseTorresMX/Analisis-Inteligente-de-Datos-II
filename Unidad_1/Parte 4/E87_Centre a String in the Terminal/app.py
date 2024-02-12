def centrar_string(cadena, ancho_terminal):
    # Calcula cantidad de espacios para centrer la cadena
    espacios = (ancho_terminal-len(cadena))//2

    # Centrar la cadena
    cadena_central = ' '*espacios+cadena
    return cadena_central


def main():
    # Obtener datos del usuario
    cadena_original = input("ingresa una cadena de caracteres: ")
    ancho_terminal = int(input("Ingresa el ancho de de la terminal: "))

    # Mandar los datos a la funcion
    cadena_centralizada = centrar_string(cadena_original, ancho_terminal)

    # Mostrar el resulado
    print("Cadena centrada en la terminal: ")
    print(cadena_centralizada)


if __name__ == "__main__":
    main()
