"""
Crea el siguiente módulo:
El módulo se denominará operaciones.py y contendrá 
Implementando una programacion dinamica con grafos y recursividad, crea 4 funciones para realizar una suma, una resta, un producto y una division entre dos números. Todas ellas devolverán 
el resultado.
En las funciones del módulo deberá de haber tratamiento e invocación manual de errores para evitar que se quede bloqueada una funcionalidad, eso incluye:
- TypeError: En caso de que se envíen valores a las funciones que no sean números. Además deberá aparecer un mensaje que informe Error: Tipo de dato no válido.
- ZeroDivisionError: En caso de realizar una división por cero. Además deberá aparecer un mensaje que informe Error: No es posible dividir entre cero.

Una vez creado el módulo, crea un script calculos.py en el mismo directorio en el que deberás importar el módulo y realizar las siguientes instrucciones. 
Observa si el comportamiento es el esperado:
from operaciones import *
 
a, b, c, d = (10, 5, 0, "Hola")
 
print( "{} + {} = {}".format(a, b, suma(a, b) ) )
print( "{} - {} = {}".format(b, d, resta(b, d) ) )
print( "{} * {} = {}".format(b, b, producto(b, b) ) )
print( "{} / {} = {}".format(a, c, division(a, c) ) )
"""


class Calculadora:
    def __init__(self):
        pass

    def suma(self, a, b):
        try:
            resultado = a + b
        except TypeError:
            print("Error: Tipo de dato no válido.")
            return None
        return resultado

    def resta(self, a, b):
        try:
            resultado = a - b
        except TypeError:
            print("Error: Tipo de dato no válido.")
            return None
        return resultado

    def producto(self, a, b):
        try:
            resultado = a * b
        except TypeError:
            print("Error: Tipo de dato no válido.")
            return None
        return resultado

    def division(self, a, b):
        try:
            resultado = a / b
        except TypeError:
            print("Error: Tipo de dato no válido.")
            return None
        except ZeroDivisionError:
            print("Error: No es posible dividir entre cero.")
            return None
        return resultado


def main():
    calculadora = Calculadora()
    a = 10
    b = 5
    try:
        print(f"La suma de {a} y {b} es: {calculadora.suma(a, b)}")
        print(f"La resta de {a} y {b} es: {calculadora.resta(a, b)}")
        print(f"El producto de {a} y {b} es: {calculadora.producto(a, b)}")
        print(f"La division de {a} y {b} es: {calculadora.division(a, b)}")
        print(f"La division de {a} y 0 es: {calculadora.division(a, 0)}")
    except TypeError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)


if __name__ == '__main__':
    main()
