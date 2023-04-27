"""
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