def buscar_palabras(ruta):
    try:
        with open(ruta, 'r') as file:
            contenido = file.read()
            palabras = contenido.split()

            if not palabras:
                print(f"El archivo {ruta} esta vacio.")
                return

            longuitud_max = max(len(palabra) for palabra in palabras)
            palabra_grandota = [
                palabra for palabra in palabras if len(palabra) == longuitud_max]

            print(f"La(s) palabra(s) mas larga en el archivo tiene {
                  longuitud_max}:")
            for la_grandota in palabra_grandota:
                print(palabra_grandota)

    except FileNotFoundError:
        print(f"No se encontro: {ruta}")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

buscar_palabras('../docs/ejemplo_txt.txt')