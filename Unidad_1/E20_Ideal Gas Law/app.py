R = 0.08314


def calcular_presion(volumen, cantidad_sustancia, temperatura):
    presion = (cantidad_sustancia*R*temperatura)/volumen
    return presion


volumen = int(input("Ingresa volumen en litros: "))
cantidad_sustancia = float(input("Ingresa cantidad en Moles: "))
temperatura = int(input("Ingresa temperatura en Kelvin: "))

presion_resultado = calcular_presion(volumen, cantidad_sustancia, temperatura)

print("Presión: %.2f" % presion_resultado, "atm")
