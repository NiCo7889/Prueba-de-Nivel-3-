"""
Dada una pila de cartas, que representa un mazo de cartas de baraja española, resolver las siguientes actividades:
- generar las cartas del mazo de forma aleatoria;
- separar la pila mazo en cuatro pilas una por cada palo;
- ordenar una de las cuatro pilas (espada, basto, copa u oro) de manera creciente.
"""


import random


class Carta:
    def __init__(self, palo, numero):
        self.palo = palo
        self.numero = numero

    def __repr__(self):
        return f'{self.numero} de {self.palo}'

class Mazo:
    def __init__(self):
        self.cartas = []
        self.palos = ['espada', 'basto', 'copa', 'oro']
        for palo in self.palos:
            for numero in range(1, 13):
                carta = Carta(palo, numero)
                self.cartas.append(carta)

    def barajar(self):
        random.shuffle(self.cartas)

    def repartir(self):
        pilas = {palo: [] for palo in self.palos}
        for carta in self.cartas:
            pilas[carta.palo].append(carta)
        return pilas

    def ordenar_pila(self, pila):
        def quicksort(pila):
            if len(pila) <= 1:
                return pila
            else:
                pivot = pila[0]
                menores = []
                mayores = []
                iguales = [pivot]
                for carta in pila[1:]:
                    if carta.numero < pivot.numero:
                        menores.append(carta)
                    elif carta.numero > pivot.numero:
                        mayores.append(carta)
                    else:
                        iguales.append(carta)
                return quicksort(menores) + iguales + quicksort(mayores)
        return quicksort(pila)

mazo = Mazo()

if __name__ == "__main__":

    mazo.barajar()
    print(f'Mazo: {mazo.cartas}')

    pilas = mazo.repartir()
    for palo in mazo.palos:
        print(f'Pila de {palo}: {pilas[palo]}')

    pila_ordenada = mazo.ordenar_pila(pilas['espada'])
    print(f'Pila de espada ordenada: {pila_ordenada}')