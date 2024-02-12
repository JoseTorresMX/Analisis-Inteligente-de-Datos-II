# from appE41 import nota_a_frecuencia
def frecuencia_a_nota(frecuencia):
    frec_nota_chart = {
        "A0": 0, "A3": 110, "A6": 880,
        "B0": 0, "B3": 123, "B6": 988,
        "C0": 16, "C3": 131, "C6": 1047,
        "D0": 18, "D3": 147, "D6": 1175,
        "E0": 21, "E3": 165, "E6": 1319,
        "F0": 22, "F3": 175, "F6": 1397,
        "G0": 25, "G3": 196, "G6": 1568,
        "A1": 28, "A4": 220, "A7": 1760,
        "B1": 31, "B4": 247, "B7": 1976,
        "C1": 33, "C4": 262, "C7": 2093,
        "D1": 37, "D4": 294, "D7": 2349,
        "E1": 41, "E4": 330, "E7": 2637,
        "F1": 44, "F4": 349, "F7": 2794,
        "G1": 49, "G4": 392, "G7": 3136,
        "A2": 55, "A5": 440, "A8": 3520,
        "B2": 62, "B5": 494, "B8": 3951,
        "C2": 65, "C5": 523, "C8": 4186,
        "D2": 73, "D5": 587, "D8": 4699,
        "E2": 82, "E5": 659, "E8": 5274,
        "F2": 87, "F5": 698, "F8": 5588,
        "G2": 98, "G5": 784, "G8": 6272
    }

    for nota_nombre, nota_frecuenca in frec_nota_chart.items():
        if abs(frecuencia-nota_frecuenca) <= 1:
            return f"La frecuencia {nota_frecuenca} pertenece a la nota: {nota_nombre}"
    return "La frecuancia no corresponde a alguna nota conocida."

try:
    frecuencia_usuario=float(input("Ingresa la frecuencia en Hertz: "))
    resultado=frecuencia_a_nota(frecuencia_usuario)
    print(resultado)
except ValueError:
    print("errores")