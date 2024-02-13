def texto_tecla_pulsada(mensaje):
    teclas_lista = {
        'a': '2', 'b': '22', 'c': '222',
        'd': '3', 'e': '33', 'f': '333',
        'g': '4', 'h': '44', 'i': '444',
        'j': '5', 'k': '55', 'l': '555',
        'm': '6', 'n': '66', 'o': '666',
        'p': '7', 'q': '77', 'r': '777', 's': '7777',
        't': '8', 'u': '88', 'v': '888',
        'w': '9', 'x': '99', 'y': '999', 'z': '9999',
        ' ': '0',
        '!': '1111', ',': '111', '.': '1111',
        '?': '11111', '\'': '1'
    }

    # Convertir mensajes en minusculas
    mensaje = mensaje.lower()
    tecla_pulsada = ''
    for caracter in mensaje:
        if caracter in teclas_lista:
            tecla_pulsada += teclas_lista[caracter]

    return tecla_pulsada


# Capturar mensajes del uusaio
entrada = input("Ingresa el mensaje: ")

# Enviar el mensaje y mostrar las teclas presionadas
teclas_pulsadas = texto_tecla_pulsada(entrada)
print("Tecla pulsada: ", teclas_pulsadas)
