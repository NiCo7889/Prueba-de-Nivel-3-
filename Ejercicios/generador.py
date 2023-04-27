"""
Crea un script llamado generador.py que cumpla las siguientes necesidades:

- Debe incluir una función llamada leer_numero(). Esta función tomará 3 valores: ini, fin y mensaje. El objetivo es leer por pantalla un número >= que ini y <= que fin. 
Además a la hora de hacer la lectura se mostrará en el input el mensaje enviado a la función. Finalmente se devolverá el valor. Esta función tiene que devolver un número, y 
tiene que repetirse hasta que el usuario no lo escriba bien (lo que incluye cualquier valor que no sea un número del ini al fin).

- Una vez la tengas creada, deberás crear una nueva función llamada generador, no recibirá ningún parámetro. Dentro leerás dos números con la función leer_numero():
El primer numero será llamado numeros, deberá ser entre 1 y 20, ambos incluidos, y se mostrará el mensaje ¿Cuantos números quieres generar? [1-20]:
El segundo número será llamado modo y requerirá un número entre 1 y 3, ambos incluidos. El mensaje que mostrará será: ¿Cómo quieres redondear los números? 
[1]Al alza [2]A la baja [3]Normal:.

- Una vez sepas los números a generar y cómo redondearlos, tendrás que realizar lo siguiente:
Generarás una lista de números aleatorios decimales entre 0 y 100 con tantos números como el usuario haya indicado.
A cada uno de esos números deberás redondearlos en función de lo que el usuario ha especificado en el modo.
Para cada número muestra durante el redondeo, el número normal y después del redondeo.

- Finalmente devolverás la lista de números redondeados.

El objetivo de este ejercicio es  la reutilización de código y los módulos random y math.
"""


import random
import math


def leer_numero(ini, fin, mensaje):
    """Lee un número entre ini y fin (ambos incluidos) desde la entrada estándar.
    Se muestra el mensaje especificado en la entrada. La función se repite hasta que
    se introduce un número válido."""
    while True:
        try:
            num = int(input(mensaje))
            if num < ini or num > fin:
                raise ValueError()
            return num
        except ValueError:
            print(f"Error: debe introducir un número entre {ini} y {fin}.")

def redondear(num, modo):
    """Redondea el número según el modo especificado: al alza (1), a la baja (2) o normal (3)."""
    if modo == 1:
        return math.ceil(num)
    elif modo == 2:
        return math.floor(num)
    else:
        return round(num)

def generador():
    """Genera una lista de números aleatorios y los redondea según la especificación del usuario."""
    numeros = leer_numero(1, 20, "¿Cuantos números quieres generar? [1-20]: ")
    modo = leer_numero(1, 3, "¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ")

    # Construir el grafo de opciones de redondeo
    grafo = {
        "al alza": ["normal", "al alza"],
        "a la baja": ["normal", "a la baja"],
        "normal": ["normal"]
    }

    # Función recursiva para recorrer el grafo y redondear los números
    def redondear_rec(num, opciones_siguientes):
        if num == numeros:
            return []
        else:
            num_aleatorio = random.uniform(0, 100)
            num_redondeado = redondear(num_aleatorio, modo)
            print(f"Número generado: {num_aleatorio:.2f}, redondeado: {num_redondeado:.2f}")
            if num_redondeado > num_aleatorio:
                opciones_siguientes = grafo["al alza"]
            elif num_redondeado < num_aleatorio:
                opciones_siguientes = grafo["a la baja"]
            else:
                opciones_siguientes = grafo["normal"]
            return [num_redondeado] + redondear_rec(num+1, opciones_siguientes)

    # Llamada inicial a la función recursiva y devolución del resultado
    return redondear_rec(0, grafo["normal"])


if __name__ == "__main__":

    numeros_redondeados = generador()
    print("Lista de números redondeados:")
    print(numeros_redondeados)