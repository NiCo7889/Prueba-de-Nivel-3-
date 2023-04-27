from operaciones import *
 
a, b, c, d = (10, 5, 0, "Hola")
 
print( "{} + {} = {}".format(a, b, Calculadora.suma(a, b) ) )
print( "{} - {} = {}".format(b, d, Calculadora.resta(b, d) ) )
print( "{} * {} = {}".format(b, b, Calculadora.producto(b, b) ) )
print( "{} / {} = {}".format(a, c, Calculadora.division(a, c) ) )