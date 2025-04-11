'''
1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 
'''

print("1)\n")
# Ciclo for de 0 a 10 imprimiendo el valor de "i" en cada iteración
for i in range(101):
    print(i)
print()


'''
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
dígitos que contiene.
'''

print("2)")
# Se solicita un número al usuario
num = int(input("Ingresa un número entero que no sea cero por favor:\n"))

# Se inicializa el contador
cont = 0

# Se valida el ingreso
if num != 0:
    # Proceso
    while num != 0:
        cont += 1
        num = num // 10
    # Se imprime el resultado
    print(f"El número ingresado tiene {cont} dígitos")
else:
    print("El número ingresado no puede ser cero.")
print()


'''
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
dados por el usuario, excluyendo esos dos valores. 
'''

print("3)")

# Se solicitan números al usuario
num1 = int(input("Ingrese un número entero por favor:\n"))
num2 = int(input("Ingrese otro número entero por favor:\n"))

# Aseguramos que el 1° número sea siempre menor que el 2°
if num1 > num2:
    aux = num1
    num1 = num2
    num2 = aux

# Se inicializa un contador y acumulador
cont = num1 + 1
acu = 0

# Proceso
while cont < num2:
    acu = acu + cont
    cont += 1
print("La suma de los numeros intermedios de los ingresados es: ", acu)
print()



'''
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
un 0. 
'''

print("4)")
# Se solicita el ingreso de los números al usuario
num = int(input("Ingrese los números enteros que desea sumar, para finaliaz ingrese un cero:\n"))

# Se inicializa un acumulador
acu = 0

# Proceso
while num != 0:
    acu += num
    num = int(input())
# Se imprime el resultado
print("La suma total de los números ingesados es de:",acu)
print()


'''
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 
'''

print("5)")
# Se importa la librería random de Python
import random

# Se genera un número aleatorio
num_secreto = random.randrange(0,9)

# Se inicializa un contador
cont = 1

# Se pide al usuario que ingrese un número
num = int(input("Adivina el número secreto ingresando un número del 0 al 9:\n"))

# Proceso
while num != num_secreto:
    cont +=1
    num = int(input("No adivinaste el número aún, intenta de nuevo:\n"))

# Resultado/egreso
if cont == 1:
    print("Felicidades! adivinaste el número en tu primer intento!!")
else:
    print(f"Muy bien, adivinaste el número en {cont} intentos.")
print()


'''
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
entre 0 y 100, en orden decreciente. 
'''

print("6)\n")

# Ciclo for decreciente
for i in range(100,-1,-1):
    if i % 2 == 0:
        print(i)
print()


'''
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
número entero positivo indicado por el usuario. 
'''

print("7)\n")

# Se solicita un número al usuario
num = int(input("Ingrese un número entero positivo por favor:\n"))

# Se inicializa un contador y un acumulador
cont = 1
acu = 0

# Se valida el ingreso
if num > 0:

# Proceso
    while cont <= num:
        acu = acu + cont
        cont += 1
    print("La suma de todos los numeros consecutivos desde 0 hasta el número ingresado es de:", acu)
else: 
    print("Debe ingresar un número positivo.")
print()


'''
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
'''

print("8)\n")

# Se informa la metodología del programa.
print("Debes ingresar 100 números enteros para dar fin al programa y ver su resultado.")
print("Ingresa el primer número:")
# Se inicializan los conatdores
cont_pos = 0
cont_neg = 0
cont_par = 0
cont_impar = 0
cont_neutro = 0

# Proceso
for i in range(100):
    # Se solicitan los números al usuario
    num = int(input())
    # Se discriminan los ingresos de ceros
    if num == 0:
        cont_neutro += 1

    # Se evalúan los positivos y negativos (o neutros)
    else:
        if num > 0:
            cont_pos += 1
        else:
            cont_neg += 1
            
        # Se evalúan los pares e impares
        if num % 2 == 0:
            cont_par += 1
        else:
            cont_impar += 1
# Se imprimen los resultados
print(f"Se ingresaron {cont_pos} números positivos,",end=" ")
print(cont_neg, "números negativos,",end=" ")
print(cont_par, "números pares,")
print(f"y {cont_impar} números impares.")
if cont_neutro == 1:
    print("También se ingresó un número neutro.")
elif cont_neutro >= 2:
    print(f"También se ingresaron {cont_neutro} números neutros.")
print()


'''
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
poder procesar 100 números cambiando solo un valor).
'''

print("9)\n")

print("Ingresa cien números enteros, el programa te informara la media de los mismos.")
print("Ingresa el primer número:")

# Se inicializa el acumulador y se fija cantidad de ingresos
acu = 0
CANTIDAD = 100

for i in range(100):
    # Se solicitan los números al usuario
    num = int(input())
    # Se acumulan los ingresos
    acu += num

# Proceso
media = float(acu / CANTIDAD)
print(acu)

# Se imprime el resultado
print("La media de los valores ingresados es de:", media)
print()


'''
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 
'''
print("10)\n")

# Se informa el proceso y se solicita un número al usuario
num = int(input("Ingrese un número entero distinto de cero, el programa invertirá el orden de los dígitos.\n"))

# Se inicializa la variable de almaceamiento del número inverso
num_invertido = '' 

# Se ejecuta un proceso en caso de que el número ingresado sea negativo
num_neg = False

if num < 0:
    num = num - (num * 2)
    num_neg = True

if num != 0:
    while num != 0:
        # Se extrae el último dígito y se lo asigna a una variable
        digito = num % 10
        # Se actualiza el número
        num = num // 10
        num_invertido = num_invertido + str(digito)
else:
    print("Ingresa un número distinto de cero.")

# Se muestra el resultado
if num_neg == False:
    print(f"El número ingresado resulta en el número {num_invertido} al invertirlo.")
else:
    print(f"El número ingresado resulta en el número -{num_invertido} al invertirlo.")