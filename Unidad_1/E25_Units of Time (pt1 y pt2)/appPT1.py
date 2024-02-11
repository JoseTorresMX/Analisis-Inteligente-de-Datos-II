def duracion_a_segundos(dias, horas, minutos, segundos):
    total_segundos = (dias*24*60*60)+(horas*60*60)+(minutos*60)+segundos
    return total_segundos

dias = int(input("Ingresas los dias: "))
horas = int(input("Ingresas las horas: "))
minutos = int(input("Ingresas los minutos: "))
segundos = int(input("Ingresas los segundos: "))

total_segundos=duracion_a_segundos(dias,horas,minutos,segundos)

print(f"\nEl numero total de segundos segun la duracion es: {total_segundos:,} segundos")
