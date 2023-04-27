"""
Resuelva el siguiente problema utilizando árboles de decisión. El problema es el siguiente:
Nick Fury, líder de la agencia S.H.I.E.L.D., tiene la difícil tarea de decidir qué vengador asignará a cada nueva misión (por ahora considere que solo se asignará un 
superhéroe por cada misión). Teniendo en cuenta el listado de superhéroes es el siguiente:Iron Man, The incredible Hulk, Khan, Thor, Captain América, Capitana Marvel, 
Ant-Man, Nick Fury, The Winter Soldier.

Nos solicita desarrollar un árbol de decisión para resolver esta tarea con los siguientes requerimientos:
- Cada nodo hoja del árbol debe ser un superhéroe y en cada nodo intermedio inclusive la raíz debe haber una pregunta. Si la respuesta es sí, se debe desplazar hacia el subárbol izquierdo, si es no al subárbol derecho. Además, debéis desarrollar una función que determine el superhéroe para una misión;
- Khan es ideal para misiones intergalácticas en equipo;
- Ant-Man es excelente en misiones de recuperación donde sea necesario no se detectado;
- para misiones de destrucción Hulk es una excelente opción;
- el Capitán América es un supersoldado de ética incorruptible ideal para comandar misiones de defensa y de recuperación;
- Capitana Marvel es muy poderosa y puede viajar por las distintas galaxias;
- Khan es muy hábil y puede ser útil para varias misiones;
- para misiones de recuperación donde requiera infiltrarse con personas del lugar, The Winter Soldier es la persona indicada;
- Iron Man es un líder para planear misiones de defensa, además es un genio y domina el manejo de tecnología avanzada, cuenta con un traje muy poderoso;
- cuando se requiere elegir cuál será la próxima acción para tomar y moverse rápidamente de un lugar a otro, es el propio Nick Fury es la opción más lógica;
- Thor tiene el poder para destruir ejércitos completos;
- no se debe utilizar árbol balanceado.
"""


class nodoArbol:
    def __init__(self, info):
        self.izq = None
        self.der = None
        self.info = info

class Superheroe:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return self.nombre
    
class ArbolDecision:
    def __init__(self, arbol_decision):
        self.arbol_decision = arbol_decision
    def asignar_superheroe(self):
        nodo_actual = self.arbol_decision

        while True:
            if isinstance(nodo_actual.info, Superheroe):
                return nodo_actual.info
            else:
                respuesta = input(f"{nodo_actual.info} (Sí/No): ")
                if respuesta.lower() == "sí" or respuesta.lower() == "si" or respuesta.lower() == "s":
                    nodo_actual = nodo_actual.izq
                else:
                    nodo_actual = nodo_actual.der

def main():
    # Crear superhéroes
    iron_man = Superheroe("Iron Man", "Líder para planear misiones de defensa, genio y domina el manejo de tecnología avanzada")
    hulk = Superheroe("The Incredible Hulk", "Excelente opción para misiones de destrucción")
    khan = Superheroe("Khan", "Ideal para misiones intergalácticas en equipo")
    thor = Superheroe("Thor", "Poder para destruir ejércitos completos")
    cap_america = Superheroe("Captain América", "Supersoldado de ética incorruptible ideal para comandar misiones de defensa y de recuperación")
    cap_marvel = Superheroe("Capitana Marvel", "Muy poderosa y puede viajar por las distintas galaxias")
    ant_man = Superheroe("Ant-Man", "Excelente en misiones de recuperación donde sea necesario no ser detectado")
    nick_fury = Superheroe("Nick Fury", "El propio Nick Fury es la opción más lógica para elegir la próxima acción y moverse rápidamente de un lugar a otro")
    winter_soldier = Superheroe("The Winter Soldier", "Ideal para misiones de recuperación donde requiera infiltrarse con personas del lugar")

    # Crear árbol de decisión
    arbol_decision = nodoArbol("¿La misión es intergaláctica?")

    arbol_decision.izq = nodoArbol("¿La misión es en equipo?")
    arbol_decision.der = nodoArbol("¿La misión es de defensa?")

    arbol_decision.izq.izq = nodoArbol(khan)
    arbol_decision.izq.der = nodoArbol(cap_marvel)

    arbol_decision.der.izq = nodoArbol("¿La misión requiere tecnología avanzada?")
    arbol_decision.der.der = nodoArbol("¿La misión es de recuperación?")

    arbol_decision.der.izq.izq = nodoArbol(iron_man)
    arbol_decision.der.izq.der = nodoArbol(nick_fury)

    arbol_decision.der.der.izq = nodoArbol("¿Es necesario infiltrarse con personas del lugar?")
    arbol_decision.der.der.der = nodoArbol("¿La misión es de destrucción?")

    arbol_decision.der.der.izq.izq = nodoArbol(winter_soldier)
    arbol_decision.der.der.izq.der = nodoArbol(cap_america)

    arbol_decision.der.der.der.izq = nodoArbol("¿Hay ejércitos completos?")
    arbol_decision.der.der.der.der = nodoArbol(ant_man)

    arbol_decision.der.der.der.izq.izq = nodoArbol(thor)
    arbol_decision.der.der.der.izq.der = nodoArbol(hulk)

    # Ejemplo de uso
    arbol = ArbolDecision(arbol_decision)
    superheroe_seleccionado = arbol.asignar_superheroe()
    print(f"\nSuperhéroe seleccionado: {superheroe_seleccionado}\nDescripción: {superheroe_seleccionado.descripcion}")

if __name__ == "__main__":
    main()