"""
Desarrollar un algoritmo que permita cargar 1000 número enteros, generados de manera aleatoria y que resuelva las siguientes actividades:
 
- realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
- determinar si un número está cargado en el árbol o no;
- eliminar tres valores del árbol;
- determinar la altura del subárbol izquierdo y del subárbol derecho;
- determinar la cantidad de ocurrencias de un elemento en el árbol;
- contar cuántos números pares e impares hay en el árbol.
"""


import random


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
    
    def agregar(self, valor):
        if valor < self.valor:
            if self.izquierda is None:
                self.izquierda = Nodo(valor)
            else:
                self.izquierda.agregar(valor)
        else:
            if self.derecha is None:
                self.derecha = Nodo(valor)
            else:
                self.derecha.agregar(valor)
    
    def buscar(self, valor):
        if self.valor == valor:
            return True
        elif valor < self.valor:
            if self.izquierda is None:
                return False
            else:
                return self.izquierda.buscar(valor)
        else:
            if self.derecha is None:
                return False
            else:
                return self.derecha.buscar(valor)
    
    def eliminar(self, valor):
        if valor < self.valor:
            if self.izquierda is not None:
                self.izquierda = self.izquierda.eliminar(valor)
        elif valor > self.valor:
            if self.derecha is not None:
                self.derecha = self.derecha.eliminar(valor)
        else:
            if self.izquierda is None:
                return self.derecha
            elif self.derecha is None:
                return self.izquierda
            else:
                self.valor = self.izquierda.maximo()
                self.izquierda = self.izquierda.eliminar(self.valor)
        return self
    
    def maximo(self):
        if self.derecha is None:
            return self.valor
        else:
            return self.derecha.maximo()
    
    def altura_izquierda(self):
        if self.izquierda is None:
            return 0
        else:
            return 1 + self.izquierda.altura_izquierda()

    
    def altura_derecha(self):
        if self.derecha is None:
            return 0
        else:
            return 1 + self.derecha.altura()
    
    def cantidad(self, valor):
        if self.valor == valor:
            if self.izquierda is not None:
                return 1 + self.izquierda.cantidad(valor)
            else:
                return 1
        elif valor < self.valor:
            if self.izquierda is None:
                return 0
            else:
                return self.izquierda.cantidad(valor)
        else:
            if self.derecha is None:
                return 0
            else:
                return self.derecha.cantidad(valor)
    
    def contar_pares_impares(self):
        if self.raiz is None:
            return 0, 0
        else:
            pares = 0
            impares = 0
            if self.raiz.valor % 2 == 0:
                pares += 1
            else:
                impares += 1
            pares_izq, impares_izq = self.raiz.izquierda.contar_pares_impares() if self.raiz.izquierda is not None else (0, 0)
            pares_der, impares_der = self.raiz.derecha.contar_pares_impares() if self.raiz.derecha is not None else (0, 0)
            return pares + pares_izq + pares_der, impares + impares_izq + impares_der

class ArbolBinario:
    def __init__(self):
        self.raiz = None
    
    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self.raiz.agregar(valor)
    
    def buscar(self, valor):
        if self.raiz is not None:
            return self.raiz.buscar(valor)
        else:
            return False

    def eliminar(self, valor):
        if self.raiz is not None:
            self.raiz = self.raiz.eliminar(valor)

    def preorden(self, nodo):
        if nodo is not None:
            print(nodo.valor, end=" ")
            self.preorden(nodo.izquierda)
            self.preorden(nodo.derecha)

    def inorden(self, nodo):
        if nodo is not None:
            self.inorden(nodo.izquierda)
            print(nodo.valor, end=" ")
            self.inorden(nodo.derecha)

    def postorden(self, nodo):
        if nodo is not None:
            self.postorden(nodo.izquierda)
            self.postorden(nodo.derecha)
            print(nodo.valor, end=" ")

    def por_nivel(self):
        if self.raiz is not None:
            nivel_actual = [self.raiz]
            while nivel_actual:
                nivel_siguiente = []
                for nodo in nivel_actual:
                    print(nodo.valor, end=" ")
                    if nodo.izquierda is not None:
                        nivel_siguiente.append(nodo.izquierda)
                    if nodo.derecha is not None:
                        nivel_siguiente.append(nodo.derecha)
                nivel_actual = nivel_siguiente

    def altura_izquierda(self):
        if self.raiz is None:
            return 0
        else:
            return self.raiz.altura_izquierda()

    def altura_derecha(self):
        if self.raiz is None:
            return 0
        else:
            return self.raiz.altura_derecha()


    def cantidad(self, valor):
        if self.raiz is not None:
            return self.raiz.cantidad(valor)
        else:
            return 0

    def contar_pares_impares(self):
        if self is None:
            return 0, 0
        else:
            pares_izq, impares_izq = self.izquierda.contar_pares_impares()
            pares_der, impares_der = self.derecha.contar_pares_impares()
            if self.valor % 2 == 0:
                return pares_izq + pares_der + 1, impares_izq + impares_der
            else:
                return pares_izq + pares_der, impares_izq + impares_der + 1


arbol = ArbolBinario()

for i in range(1000):
    arbol.agregar(random.randint(1, 10000))


if __name__ == "__main__":

    # realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado
    print("Barrido preorden:")
    arbol.preorden(arbol.raiz)
    print()

    print("Barrido inorden:")
    arbol.inorden(arbol.raiz)
    print()

    print("Barrido postorden:")
    arbol.postorden(arbol.raiz)
    print()

    print("Barrido por nivel:")
    arbol.por_nivel()
    print()

    # determinar si un número está cargado en el árbol o no
    print("El número 5000 está en el árbol:", arbol.buscar(5000))

    arbol.eliminar(5000)
    arbol.eliminar(7500)
    arbol.eliminar(10000)

    # determinar la altura del subárbol izquierdo y del subárbol derecho
    print("Altura del subárbol izquierdo:", arbol.altura_izquierda())
    print("Altura del subárbol derecho:", arbol.altura_derecha())

    # determinar la cantidad de ocurrencias de un elemento en el árbol
    print("El número 300 aparece", arbol.cantidad(300), "veces en el árbol")

    # contar cuántos números pares e impares hay en el árbol
    pares, impares = arbol.contar_pares_impares()
    print("Cantidad de números pares:", pares)
    print("Cantidad de números impares:", impares)