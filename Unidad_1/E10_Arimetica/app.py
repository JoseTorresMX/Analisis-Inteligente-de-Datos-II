from math import log10

a = int(input("Ingresa el valor de A: "))
b = int(input("Ingresa el valor de B: "))

# Mostrando las operaciones basicas
print(a, "+", b, " = ", a+b)
print(a, "-", b, " = ", a-b)
print(a, "*", b, " = ", a*b)
print(a, "/", b, " = ", a/b)
print(a, "%", b, " = ", a % b)

# Calculador el logaritmo
print("La Base 10 logaritmica de ", a, " es ", log10(a))
print(a, "^", b, " es ", a**b)
