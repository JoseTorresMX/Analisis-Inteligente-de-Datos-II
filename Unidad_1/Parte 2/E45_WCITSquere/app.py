def color_cuadrado(posicion):

    # Extraer la col y fil segun la posucion
    columna = posicion[0].lower()
    fila = int(posicion[1])

    # Chacar si la col empieza won un cuadrado negro
    if columna in ['a', 'c', 'e', 'g']:
        # Se usae el modulo (%) para calcular el color basado en la fila
        if fila % 2 == 0:
            return f"La posicion {columna}{fila} esta en un cuadro negro"
        else:
            return f"La posicion {columna}{fila} esta en un cuadro blanco"
    else:
        # Nuevamente se usa el modulo (%) para calcular el color
        # basado en la fila segun la columna
        if fila % 2 == 0:
            return f"La posicion {columna}{fila} esta en un cuadro blanco"
        else:
            return f"La posicion {columna}{fila} esta en un cuadro negro"


try:
    posicion_usuario = input("Ingresa la position (ej., a1 or d5)")
    resultado = color_cuadrado(posicion_usuario)
    print(resultado)
except ValueError:
    print("error")
