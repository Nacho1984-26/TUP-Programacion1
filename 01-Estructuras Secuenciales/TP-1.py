#   1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.  
print("Ejercicio N°1")
print("Hola Mundo!\n")

#   2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
#   el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
#   por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
#   realizar la impresión por pantalla. 
print("Ejercicio N°2")
nombre = input("¿Cuál es tu nombre? ")
print(f"Hola {nombre}!")
print()

#   3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
#   imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
#   “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
#   años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
#   la impresión por pantalla.
print("Ejercicio N°3")
nombre = input("Ingresa tu nombre por favor: ")
apellido = input(f"Hola {nombre}!. Ahora ingresa tu apellido: ")
edad = input("Exelente!. Continuemos con tu edad. Cuántos años tienes?: ")
residencia = input("Perfecto. Y ya para terminar... A donde vives?: ")
print(f"Con los datos ingresados podemos afirmar que eres {nombre} {apellido}, que tienes {edad} años de edad, y que vives en {residencia}.")
print()

#   4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
print("Ejercicio N°4")
pi = 3.1416
pi = float(pi)
radio = input("Ingresa el radio del círculo del cual quieres saber su área: ")
radio = float(radio)
diametro = radio * 2
print(f"El área del círculo es {pi * (radio * radio)}")
print(f"Mientras que el perímetro del mismo cículo es {pi * diametro}")
print()

#   5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale. 
print("Ejercicio N°5")
segundos = input("Igresa una cantidad determinada de segundos. El programa lo tranformará a horas: ")
segundos = float(segundos)
horas = (segundos / 60) / 60
print(f"{segundos} equivale a {horas} horas.")
print()

#   6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
#   multiplicar de dicho número.
print("Ejercicio N°6")
numero = input("Ingresa un número del cuál quieras saber sus múltiplos: ") 
numero = int(numero)
print(numero, "* 1 = ", numero * 1)
print(numero, "* 2 = ", numero * 2)
print(numero, "* 3 = ", numero * 3)
print(numero, "* 4 = ", numero * 4)
print(numero, "* 5 = ", numero * 5)
print(numero, "* 6 = ", numero * 6)
print(numero, "* 7 = ", numero * 7)
print(numero, "* 8 = ", numero * 8)
print(numero, "* 9 = ", numero * 9)
print(numero, "* 10 = ", numero * 10)
print()

#   7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
#   pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 
print("Ejercicio N°7")
print("Ingresa un número entero que no sea cero:")
num1 = input()
num1 = int(num1)
print("Ingresa otro número:")
num2 = input()
num2 = int(num2)
print(f"Suma: {num1} + {num2} = {num1 + num2}")
print(f"Resta: {num1} - {num2} = {num1 - num2}")
print(f"Multiplicación: {num1} * {num2} = {num1 * num2}")
print(f"División: {num1} ÷ {num2} = {num1 / num2}")
print()

#   8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
#   de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: 
print("Ejercicio N°8") 
peso = input("Ingresa tu peso: ")
peso = float(peso)
altura = input("Ingresa tu altura: ")
altura = float(altura)
print(f"El índice de tu masa corporal es de {(peso / (altura * altura))} ")
print()

#   9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 
# 𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9  𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠   + 32
#                           5
print("Ejercicio N°9")
print("Ingresa una temperatura en grados Celsius, el programa lo convertirá a grados Fahrenheit")
gradosC = input("Ingresa la temperura: ")
gradosC = float(gradosC)
print(f"{gradosC}° Celsius equivale a {(1.8 * gradosC + 32)}° Fahrenheit")
print()

#   10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de dichos números. 
print("Ejercicio N°10")
print("Ingresa tres números, el programa se encargará de entregarte el promedio de los mismos.")
n1 = input("Ingresa el primer número: ")
n2 = input("Ingresa el segundo número: ")
n3 = input("Ingresa el tercer número: ")
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
print(f"El promedio de los números ingresados es: {((n1 + n2 + n3) / 3)}")