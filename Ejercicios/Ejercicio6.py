"""
Implementando una programacion dinamica orientada a objetos, resuelve. 
Dada una pila de cartas, que representa un mazo de cartas de baraja española, resolver las siguientes actividades:
- generar las cartas del mazo de forma aleatoria;
- separar la pila mazo en cuatro pilas una por cada palo;
- ordenar una de las cuatro pilas (espada, basto, copa u oro) de manera creciente.
 

"""


import random

# Definimos la clase de la carta
class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

# Definimos la clase del mazo de cartas
class Mazo:
    def __init__(self):
        self.cartas = []
    
    def generar_mazo(self):
        palos = ['espada', 'basto', 'copa', 'oro']
        for palo in palos:
            for valor in range(1, 13):
                carta = Carta(valor, palo)
                self.cartas.append(carta)
        random.shuffle(self.cartas) # mezclar el mazo
    
    def separar_pilas(self):
        pilas = { 'espada': [], 'basto': [], 'copa': [], 'oro': [] }
        for carta in self.cartas:
            pilas[carta.palo].append(carta)
        return pilas

# Definimos la clase de la pila de cartas
class Pila:
    def __init__(self, cartas):
        self.cartas = cartas
    
    def ordenar_lista(self):
        if len(self.cartas) <= 1:
            return self.cartas
        else:
            minimo = self.cartas[0]
            for carta in self.cartas:
                if carta.valor < minimo.valor:
                    minimo = carta
            self.cartas.remove(minimo)
            lista_ordenada = Pila.ordenar_lista(self)
            lista_ordenada.cartas.insert(0, minimo)
            return lista_ordenada

if __name__ == "__main__":
    # Creamos el mazo de cartas y lo mezclamos
    mazo = Mazo()
    mazo.generar_mazo()
    print('Mazo:', mazo.cartas)

    # Creamos las pilas de cada palo
    pilas = mazo.separar_pilas()
    print('Pila de espadas:', pilas['espada'])

    # Ordenamos la pila de espadas
    pila_ordenada = Pila(pilas['espada'])
    pila_ordenada = pila_ordenada.ordenar_lista()
    print('Pila de espadas ordenada:', pila_ordenada.cartas)
