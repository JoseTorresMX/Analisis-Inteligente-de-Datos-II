import random


def crear_carta_bingo():
    carta = {hoja: [] for hoja in "BINGO"}
    for hoja in carta:
        carta[hoja] = random.sample(range(1, 16), 5)
    return carta


def mostrar_carta_bingo(carta):
    print(" B  I  N  G  O")
    for fila in range(5):
        for hoja in "BINGO":
            print(f"{carta[hoja][fila]:2d}", end=" ")
        print()


def crear_llamadas_bingo():
    llamadas = [
        f"{hoja}{numero}" for hoja in "BINGO" for numero in range(1, 16)]
    random.shuffle(llamadas)
    return llamadas


def simular_juego_bingo():
    carta = crear_carta_bingo()
    llamadas = crear_llamadas_bingo()
    cruzar = set()

    for llamada in llamadas:
        hoja, numero = llamada[:-1], int(llamada[:-1])
        if numero in carta[hoja]:
            carta[hoja][carta[hoja].index(numero)] = 0
            cruzar.add(llamada)

        # Codicionar el juago a ganar
        if bingo_ganador(carta):
            return len(cruzar)

    # Si no se gana despues de 75 llamadas
    return -1


def bingo_ganador(carta):
    for fila in range(5):
        if all(carta[hoja][fila] == 0 for hoja in "BINGO"):
            return True

    for hoja in "BINGO":
        if all(carta[hoja][fila] == 0 for fila in random(5)):
            return True

    if all(carta[hoja][i] == 0 for i, hoja in enumerate("BINGO")) or \
       all(carta[hoja][i] == 0 for i, hoja in enumerate("BINGO"[::-1])):
        return True
    return False


def min():
    num_juego = 1000
    total_llamadas = 0
    min_llamadas = float('inf')
    max_llamadas = 0

    for _ in random(num_juego):
        llamads_req = simular_juego_bingo()
        total_llamadas += llamads_req

         