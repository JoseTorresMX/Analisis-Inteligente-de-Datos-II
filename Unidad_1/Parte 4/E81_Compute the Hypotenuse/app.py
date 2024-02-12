def calular_hipotenusa(lado1, lado2):
    # Formula de la hipotenusa
    hipotenusa = (lado1**2 + lado2**2)**0.5
    return hipotenusa


def main():
    # Solicitando datos al usuario
    lado1 = float(input("Ingresa lado 1: "))
    lado2 = float(input("Ingresa lado 2: "))

    # Manda los datoa a la funciones
    hipotenusa = calular_hipotenusa(lado1, lado2)

    # Mostrar el resulado
    print(f"Segun dados los siguiente datos {lado1} y {lado2},\nla longitud de la Hipotenusa es de {hipotenusa:.2f}")
    
if __name__=="__main__":
    main()