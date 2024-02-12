# Entrada de datos
total_segundos = int(input("Ingresa el numero de segundos: "))

# Calculos de los dias, horas, minutos y segundos
dias = total_segundos//(24*3600)
segundos_restantes = total_segundos % (24*3600)
horas = segundos_restantes//3600
segundos_restantes %= 3600
minutos = segundos_restantes//60
segundos = segundos_restantes % 60

# Formateando con ceros a la izquierda, solo si es necesario
horas_formato = '{:02d}'.format(horas)
minutos_formato = '{:02d}'.format(minutos)
segundos_formato = '{:02d}'.format(segundos)

# Mostrando el resultado
tiempo_formateado = f"{dias}:{horas_formato}:{
    minutos_formato}:{segundos_formato}"
print("\nEquivalencia de tiempo:", tiempo_formateado)
