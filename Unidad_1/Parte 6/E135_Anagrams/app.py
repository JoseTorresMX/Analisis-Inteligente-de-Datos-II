def es_anagrama(cadena1, cadena2):
    # Cadenas a minusculas y sin espacios
    cadena1 = cadena1.lower().replace(" ", "")
    cadena2 = cadena2.lower().replace(" ", "")

    # Verificar si lo cadena de caracteres son iguales
    return sorted(cadena1) == sorted(cadena2)


# Capturar las cadenas del usuaior
palabra1 = input("Ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")

#Verificar si realmente las palabras son anagramas
if es_anagrama(palabra1,palabra2):
    print(f"Las palabras {palabra1} y {palabra2}, son anagramas.")
else:
    print(f"Las palabras {palabra1} y {palabra2}, NO son anagramas.")