# Tabla de ruidos y sus respectivos dB
from tabulate import tabulate
tabla = [
    ["Jackhammer", "130dB"],
    ["Gas Iawnmower", "106dB"],
    ["Alarm Clock", "70dB"],
    ["Quiet Room", "40dB"]
]

# Creadmos las cabeceras (header)
cabecera = ["Ruido", "Decibelio (dB)"]

# Mostramos la tabla
print(tabulate(tabla, headers=cabecera, tablefmt="grid"))


def identificar_ruido(nivel_decibelios):
    if nivel_decibelios < 40:
        return f"El ruido de {nivel_decibelios}dB es un ruido muy muy bajo, como si estuvieras en lugar muy quieto."
    elif 40 <= nivel_decibelios < 70:
        return f"El ruido de {nivel_decibelios}dB es un ruido menor, como si fue de una alarma despertador."
    elif 70 <= nivel_decibelios < 106:
        return f"El ruido de {nivel_decibelios}dB es un ruido medio-alto, como una aspiradora o un cortacesped."
    elif 106 <= nivel_decibelios < 130:
        return f"El ruido de {nivel_decibelios}dB es muy fuerte, como de una sierra electrica se tratese."
    elif nivel_decibelios >= 130:
        return f"El ruido de {nivel_decibelios}dB, es el ruido mas fuerte de la tabla"
    else:
        return "Entrada no valida."


# Entrada de datos
try:
    decibel = float(input("Ingresa el nivel de sonido en decibelios (dB):"))
    resultado = identificar_ruido(decibel)
    print(resultado)
except ValueError:
    print("Error: El decibelio debe ser un valor numerico.")
