def animal_zodiaco_chino(anio):
    # Lista de animales en el ciclo de 12 años
    animales_zc = ["Mono", "Gallo", "Perro", "Cerdo", "Rata", "Buey",
                   "Tigre", "Conejo", "Dragón", "Serpiente", "Caballo", "Cabra"]

    # Calcularmos el indece zodica asociado al año
    indice_zodiaco = (anio-1924) % 12

    # Mostrar el resuldado
    print(f"El animal asociado al año {anio} en el Zodiaco Chino es el/la {
          animales_zc[indice_zodiaco]}")


# Obtener datos del suaurio
try:
    anio_usuario = int(input("Ingresa un año, mayor o igual a cero: "))
    if anio_usuario >= 0:
        animal_zodiaco_chino(anio_usuario)
    else:
        print("Error...")
except ValueError:
    print("Error. Ingresa un año valido.")
