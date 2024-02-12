def es_palindromo(cadena):

    # Borrar los espacios en blanco
    # Y convertir a minusculas
    cadena = cadena.replace(" ", "").lower()

    # invertir la cadena
    cadena_invertida = cadena[::-1]

    # Verificar si la cadena original e invertida son iguales
    if cadena == cadena_invertida:
        return True
    else:
        return False


def main():
    # Entra de datos
    entrada = input("Ingresa una cadena para ver si es un palindromo: ")

    # Pasar la cadena y verificar si el palindromo
    if es_palindromo(entrada):
        print(f"La cadena [{entrada}] es un palindromo")
    else:
        print(f"La cadena [{entrada}] no es un palindromo")


if __name__ == "__main__":
    main()
