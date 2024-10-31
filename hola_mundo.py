
# 1. Imprime "Hola, mundo"

print( "Hola, mundo" )

# 2. Imprime "Hola, Valeria" con el nombre en una variable

nombre = "Leidy"

print( "Hola",nombre) # con una coma

print( "Hola " + nombre ) # con un +

# 3. Imprimir "Hola 156!" con el número en una variable

numero = 19

print( "Hola",numero,"!" ) # con una coma

print( "Hola " + format(numero) + "!") # con un + -- este debería arrojar un error!, corrígelo con conversión

# 4. Imprimir "Me encanta comer tacos y arepas" con las comidas en variables

comida1 = "salmón"

comida2 = "postres"

print("¡Me encanta comer {} y {}".format(comida1, comida2)+"!") # con .format()

print(f"¡Me encanta comer {comida1} y {comida2}!") # con una cadena f

#otras formas de imprimir cadenas:

print("Me encanta comer %s y %s" % (comida1, comida2))

print("Me encanta comer {0} y {1}".format(comida1, comida2))

print("Me encanta comer {c1} y {c2}".format(c1=comida1, c2=comida2))


