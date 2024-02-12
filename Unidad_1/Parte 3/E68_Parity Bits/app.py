def calular_bits(bits):
    if len(bits) != 8 or not bits.isdigit():
        return f"Error. La entrada {bits} no es exacto a 8 bits."

    # Contar la cantidad de 1
    cantidad_uno = bits.count('1')

    #SAber si la cantidad de unos es: par o no
    if cantidad_uno %2==0:
        return "El bit de paridad dese ser 0."
    else:
        return "El bit de paridad debe ser 1."

def main():
    while True:
        print("Pueden no ingresar nada, y el programa se termina.")
        entrada_usuario=input("Ingresa 8 bits: ")

        #Para cuando no se ingresa nada
        if not entrada_usuario:
            break

        resultado=calular_bits(entrada_usuario)
        print(resultado)

if __name__=="__main__":
    main()