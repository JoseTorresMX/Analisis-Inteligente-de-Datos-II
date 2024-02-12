R = 0.08314

volumen_inicial = int(input("Ingresa volumen en Litros: "))
presion_inicial = float(input("Ingresa la presion: "))
temperatura = float(input("Ingresa la temperatura en Kelvin"))
cantidad_utilizada = float(input("Ingresa la cantidad utilizada en litros: "))


class TannqueSCUBA:
    def __init__(self, volumen_inicial, presion_inicial, temperatura):
        self.volumen = volumen_inicial
        self.presion = presion_inicial
        self.temperatura = temperatura

    def calcular_cantidad_sustancia(self):
        cantidad_sustancia = (self.presion*self.volumen)/(R*self.temperatura)
        return cantidad_sustancia

    def utilizar_aire(self, cantidad_utilizada):
        self.presion = (self.presion*self.volumen-R *
                        self.temperatura*cantidad_utilizada)/self.volumen


tanque_scuba = TannqueSCUBA(volumen_inicial, presion_inicial, temperatura)
tanque_scuba.utilizar_aire(cantidad_utilizada)

print("Cantidad inicial de sustancia en el tanque",
      tanque_scuba.calcular_cantidad_sustancia, " moles")
print("Cantidad de sustancia despues de usar ", cantidad_utilizada,
      " moles: ", tanque_scuba.calcular_cantidad_sustancia, " moles")
