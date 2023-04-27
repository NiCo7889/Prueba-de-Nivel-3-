def suma(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Error: Tipo de dato no válido.")
    if b == 0:
        return a
    return suma(a + 1, b - 1)

def resta(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Error: Tipo de dato no válido.")
    if b == 0:
        return a
    return resta(a - 1, b - 1)

def producto(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Error: Tipo de dato no válido.")
    if b == 0:
        return 0
    return a + producto(a, b - 1)

def division(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Error: Tipo de dato no válido.")
    if b == 0:
        raise ZeroDivisionError("Error: No es posible dividir entre cero.")
    if a < b:
        return 0
    return 1 + division(a - b, b)





class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

def add_operation_node(node_a, node_b):
    result = GraphNode(node_a.val + node_b.val)
    node_a.neighbors.append(result)
    node_b.neighbors.append(result)
    return result

def multiply_operation_node(node_a, node_b):
    result = GraphNode(node_a.val * node_b.val)
    node_a.neighbors.append(result)
    node_b.neighbors.append(result)
    return result

def subtract_operation_node(node_a, node_b):
    result = GraphNode(node_a.val - node_b.val)
    node_a.neighbors.append(result)
    node_b.neighbors.append(result)
    return result

def divide_operation_node(node_a, node_b):
    if node_b.val == 0:
        raise ZeroDivisionError("Error: No es posible dividir entre cero.")
    result = GraphNode(node_a.val / node_b.val)
    node_a.neighbors.append(result)
    node_b.neighbors.append(result)
    return result

# Ejemplo de uso
node_10 = GraphNode(10)
node_5 = GraphNode(5)
node_0 = GraphNode(0)
node_hello = GraphNode("Hola")

try:
    result_sum = add_operation_node(node_10, node_5)
    print("10 + 5 = ", result_sum.val)
except TypeError:
    print("Error: Tipo de dato no válido.")

try:
    result_sub = subtract_operation_node(node_5, node_hello)
    print("5 - Hola = ", result_sub.val)
except TypeError:
    print("Error: Tipo de dato no válido.")

result_mul = multiply_operation_node(node_5, node_5)
print("5 * 5 = ", result_mul.val)

try:
    result_div = divide_operation_node(node_10, node_0)
    print("10 / 0 = ", result_div.val)
except ZeroDivisionError as e:
    print(e)
