# Trabao práctico N°5.1:
#                        LISTAS

'''
1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
'''
print("Ejercicio 1\n") 

multiplos_4 = list(range(4,101,4))
print(multiplos_4)
print()


'''
2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el 
penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el 
indexing con números negativos! 
'''
print("Ejercicio 2\n")


# Se crea lista de 5 elementos
lista5 = ['Azul', "Blanco", 77, True, 25.7 ]

# Se imprime el penúltimo elemento de la lista.
print(lista5[-2])
print()


'''
3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por 
pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por 
ejemplo: 
lista_vacia = []
'''
print("Ejercicio 3\n")

# Se crea una lista vacía
lista_colores = []

# Se agregan palabras a la lista vacía
lista_colores.append("Rojo")
lista_colores.append("Blanco")
lista_colores.append("Azul")

# Se imprime el resultado
print(lista_colores)
print()


'''
4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, 
respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los 
videos o bien investigar cómo funciona el indexing con números negativos! 
'''
print("Ejercicio 4\n")


# Lista de animales
animales = ["perro", "gato", "conejo", "pez"] 

# Se reemplaza el segundo elemento de la lista
animales[1] = "loro"

# Se reemplaza el último elemento de la lista
animales[-1] = "oso"

# Se imprime el resultado
print(animales)
print()


'''
5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
'''

print("Ejercicio 5\n")

print("Lo que realiza el programa en cuestión es eliminar el elemento de mayor valor de la lista \"numeros\".")
print()

'''
6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por 
pantalla los dos primeros.
'''
print("Ejercicio 6\n")

# Se crea lista solicitada:
numeros = list(range(10,31,5))

# Se muestran sólo los dos primeros números de la lista "numeros".
print(numeros[0:2]) 
print()


'''
7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores 
cualesquiera. 
'''
print("Ejercicio 7\n")

# Se crea lista de marcas de autos
autos = ["sedan", "polo", "suran", "gol"]

# Se reemplazan los índices 1 y 2 de la lista

# Índice 1:
autos[1] = "vento"
# Índice 2:
autos[2] = "bora"

# Se iprime el resultado
print(autos)
print()


'''
8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append 
directamente. Imprimir la lista resultante por pantalla.
'''
print("Ejercicio 8\n")

# Se crear la lista vacía
dobles = []  

# Se agregar el doble de 5
dobles.append(5 * 2)
# Se agregar el doble de 10
dobles.append(10 * 2)
# Se agregar el doble de 15
dobles.append(15 * 2)

# Se imprime el resultado
print(dobles)
print()


'''
9) Dada la lista “compras”, cuyos elementos representan los productos comprados por 
diferentes clientes: 
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

a) Agregar "jugo" a la lista del tercer cliente usando append. 
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
c) Eliminar "pan" de la lista del primer cliente.  
d) Imprimir la lista resultante por pantalla.
'''
print("Ejercicio 9\n")


# Lista de compras de clientes
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# Punto a: Se agrega "jugo" a la tercer lista anidada
compras[2].append("jugo")

# Punto b: Se reemplaza "fideos" por "tallarines"
compras[1][1] = "tallarines"

# Punto c: Se elimina "pan" de la primer lista
compras[0].remove("pan")

# punto c: Se imprime el resultado
print(compras)
print()


'''
10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 
● Posición lista_anidada[0]: 15 
● Posición lista_anidada[1]: True 
● Posición lista_anidada[2][0]: 25.5 
● Posición lista_anidada[2][1]: 57.9 
● Posición lista_anidada[2][2]: 30.6 
● Posición lista_anidada[3]: False 
Imprimir la lista resultante por pantalla.
'''
print("Ejercicio 10\n")

# Se crea la lista anidada solicitada
lista_anidada = [[15], [True], [25.5, 57.9, 30.6], [False]]

# Se imprime el resultado
print(lista_anidada)
print()