# LIBRERÍA DE MATEMATICAS
import math
pi = math.pi

# FUNCIONES


# Función "Hola mundo". (Ejercicio 1)
def imprimir_hola_mundo():
    return str("Hola mundo!")

# Función "Saludo personalizado". (Ejercicio 2)
def saludar_usuario(nombre):
    return str(f"Hola {nombre}!")


# Función "Datos personales". (Ejercicio 3)
def informacion_personal(nombre, apellido, edad, residencia):
    return str(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


#(Ejercicio 4)
# Función radio al cuadrado
def radio_al_cuadrado(r):
    return r ** 2

# Función diámetro (en base al radio)
def diametro(r):
    return r * 2

# Función área
def calcular_area_circulo(r):
    return pi * radio_al_cuadrado(r)

# Función perímetro
def calcular_perimetro_circulo(r):
    return pi * diametro(r)


# Función segundos a horas (Ejercicio 5)
def segundos_a_horas(seg):
    return seg / 3600


# Función múltiplos de un número (Ejercicio 6)
def tabla_multiplicar(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num * i}")


# Función de operaciones básicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinido"  # Manejo de la división por cero
    return (suma, resta, multiplicacion, division)



# Función de IMC (Ejercicio 8)
def calcular_imc(p, a):
    return (p / (a ** 2))


# Función conversión de grados (Ejercicio 9)
def celsius_a_fahrenheit(grados):
    return (1.8 * grados + 32)


# Función promedios
def calcular_promedio(a, b, c):
    return ((a + b + c) / 3)



# PROGRAMAS PRINCIPALES
'''
Consejo:
Antes de empezar, analiza cada problema y piensa cómo dividirlo en pasos más pequeños 
utilizando funciones. Al terminar, prueba cada función con diferentes entradas para verificar
que funciona correctamente.
'''



'''
1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. 
Llamar a esta función desde el programa principal.
'''
print("Ejercicio 1\n")

# Se imprime la frase "Hola mundo" mediante la función creada con ese fin.
print(imprimir_hola_mundo())
print()

'''
2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y 
devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), 
deberá de volver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando 
el nombre al usuario.
'''
print("Ejercicio 2\n")

# Se solicita el nombre del usuario y se lo almacena
nombre = input("Ingresa tu nombre por favor:\n")

# Se imprime el saludo utilizando la función.
print(saludar_usuario(nombre))
print()


'''
3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que 
reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en 
[residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
'''
print("Ejercicio 3\n")

# Se solicitan los datos al usuario
a = input("Ingresa tu nombre por favor: ")
b = input("Ahora ingresa tu apellido: ")
c = input("Continuemos con tu edad: ")
d = input("Finalmente, ingresa tu lugar de residencia: ")

# Se imprime el resultado
print(informacion_personal(a, b, c, d))
print()


'''
4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro 
y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio 
como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y 
llamar ambas funciones para mostrar los resultados.
'''
print("Ejercicio 4\n")

# Se solicita el ingreso de datos al usuario
rad = float(input("Ingresa el radio de un círculo por favor: "))

# Se devuelve el resultado aplicando las funciones
print(f"De acuerdo al valor ingresado el área del círculo es de {calcular_area_circulo(rad)}\nMientras que su perímetro es {calcular_perimetro_circulo(rad)}")
print()


'''
5. Crear una función llamada segundos_a_horas(segundos) que recibauna cantidad de 
segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al 
usuario los segundos y mostrar el resultado usando esta función.
'''
print("Ejercicio 5\n")

# Se solicitan los segundos al usuario
segundos = int(input("Ingrsa una cantidad en segundos, el programa lo convertirá a horas: "))

# Se imprime el resultado
print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos)} horas.")
print()


'''
6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima 
la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.
'''
print("Ejercicio 6\n")

# Se solicita el número que será multiplicado al usuario
num = int(input("Ingresa el número del cual deseas saber su tabla de muliplicar: "))

# Se imprime el resultado utilizando la función
tabla_multiplicar(num)
print()


'''
7. Crear una función llamada operaciones_basicas(a, b) que recibados números como parámetros 
y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
Mostrar los resultados de forma clara.
'''
print("Ejercicio 7\n")

# Se solicitan los números al usuario
print("Ingresa dos números distintos a cero. El programa te mostrará los resultados de suma, resta, división y multiplicación entre ellos.")
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segudo número: "))
print()

# Se imprimen los resulados
resultados = operaciones_basicas(num1, num2)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")
print()

'''
8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y 
la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los 
datos y llamar a la función para mostrar el resultado con dos decimales.
'''
print("Ejercicio 8\n")

# Se solicita el peso al usuario
peso = float(input("Ingresa tu peso: "))
# Se solicita la altura del usuario
altura = float(input("Ingresa tu altura: "))

# Se muestra el resultado utilizando la función.
print(f"Tu índice de masa corporal (IMC) es de: {calcular_imc(peso, altura)}")
print()


'''
9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.
'''
print("Ejercicio 9\n")

# Se solicita la temperatura en grados Celsius al usuario.
print("Ingresa una temperatura en grados Celsius, el programa lo convertirá a grados Fahrenheit.")
gradosC = float(input("Ingresa la temperura: "))

# Se imprime el resultado haciendo uso de la función.
print(f"{gradosC}° Celsius equivale a {celsius_a_fahrenheit(gradosC)}° Fahrenheit")
print()


'''
10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como 
parámetros y devuelva el promedio de ellos. Solicitar los números al usuario 
y mostrar el resultado usando esta función.
'''
print("Ejercicio 10\n")

# Se solicitan los números al usuario
print("Ingresa tres números. El programa te devolverá el promedio de ellos.")
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el último número: "))

# Se imprime el resultado haciendo uso de la función.
print(f"El promedio de los números ingresados es: {calcular_promedio(num1, num2, num3)}")