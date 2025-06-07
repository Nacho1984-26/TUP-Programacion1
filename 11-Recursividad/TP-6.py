'''
1- Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
función para calcular y mostrar en pantalla el factorial de todos los números enteros 
entre 1 y el número que indique el usuario 
'''

print("Ejercicio 1\n")

# Se crea la función recursiva que calcula el factorial de un número.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Se solicita un número al usuario  el cual funionará como rango.
num = int(input("Ingresa un número entero: "))

# Se crea el bucle que irá entregando los factoriales desde 1 hasta el número ingresado por el usuario.
for i in range(1, num+1):
    print(f"El factorial de {i} es: {factorial(i)}") # Se imprimen los factoriales.


'''
2- Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique. 
'''

print("Ejercicio 2\n")

# Se solicita la posición al usuario hasta donde quiere que se ejecute la serie de Fibonacci
n = int(input("Ingrese hasta que posición de la serie Fibonacci quiere ver: "))

# Se crea la función de Fibonacci aplicando su método
def fibonacci(n): 
    if n == 0: 
        return 0 
    elif n == 1: 
        return 1 
    else: 
        return fibonacci(n - 1) + fibonacci(n - 2)

# Se crea un bucle for para imprimir la sucesión de Fibonacci desde el comienzo hasta la posición indicada por el usuario.
for i in range(n + 1):
    print(fibonacci(i)) # Se imprime el valor de cada posición hasta llegar la posición requerida.



'''
3- Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general. 
'''

print("Ejercicio 3\n")

def potencia_recursiva(base, exponente):
    # Caso base: cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1
    # Se multiplica la base por el resultado de la potencia con un exponente reducido
    return base * potencia_recursiva(base, exponente - 1)

# Prueba de la función con un algoritmo general
print("Ingrese el número del cuál quiere saber su potencia:")
base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))

resultado = potencia_recursiva(base, exponente)
print(f"{base}^{exponente} = {resultado}")



'''
4- Crear una función recursiva en Python que reciba un número entero positivo en base decimal 
y devuelva su representación en binario como una cadena de texto. 
'''

print("\nEjercicio 4\n")

binario = [] # Creamos la lista "binario" que almacenará cada dígito binario

# Función que transforma decimal a binario
def binario_recursivo(nume):
    if nume == 0:
        return
    else:
        binario_recursivo(nume // 2)  # Llamamos recursivamente antes de agregar el residuo
        binario.append(nume % 2)  # Agregamos el bit correspondiente

# Solicitamos el número que queremos convertir a binario
nume = int(input("Ingresa el número entero positivo que quieras transformar a binario: "))
binario_recursivo(nume) # Llamado de la fución

# Convertimos la lista a una cadena e imprimimos el resultado
#print(f"El número {n} en decimal es:", "".join(map(str, binario))" en binario.")  

print("".join(map(str, binario)))

'''
5- Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de 
texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es. 
Requisitos: 
La solución debe ser recursiva. 
No se debe usar [::-1] ni la función reversed(). 
'''

print("\nEjercicio 5\n")

def es_palindromo(palabra):
    # Caso base: Si la palabra tiene 0 o 1 caracteres, es un palíndromo
    if len(palabra) <= 1:
        return True
    # Verificamos si el primer y último carácter son iguales
    if palabra[0] != palabra[-1]:
        return False
    # Llamamos recursivamente con la palabra sin el primer y último carácter
    return es_palindromo(palabra[1:-1])

# Ejemplo de uso
palabra = input("Ingresa una palabra sin espacios ni tildes, el programa te dirá si es palíndromo o no: ")
print(es_palindromo(palabra))



'''
6- Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
número entero positivo y devuelva la suma de todos sus dígitos. 
Restricciones: 
No se puede convertir el número a string. 
Usá operaciones matemáticas (%, //) y recursión. 
Ejemplos: 
suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
suma_digitos(9)      → 9 
suma_digitos(305)    → 8   (3 + 0 + 5)
'''

print("Ejercicio 6\n")

def suma_digitos(n):
    if n < 10:   # Caso base (si el numero es menor a 10 significa que es sólo un dígito)
        return n
    else:
        # Se extrae el últim dígito y se suma con el anterior mediante la recursión
        return (n % 10) + suma_digitos(n // 10) 

n = int(input("Ingrese el número del cuál quiere obtener la suma de sus dígitos: "))
print(f"La suma de los dígitos de {n} nos da como resultado: {suma_digitos(n)}.")



'''
7-  Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
último nivel con un solo bloque. 
 
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
pirámide. 
Ejemplos: 
contar_bloques(1)   → 1         (1) 
contar_bloques(2)   → 3         (2 + 1) 
contar_bloques(4)   → 10        (4 + 3 + 2 + 1)
'''

print("\nEjercicio 7\n")

def contar_bloques(num):
    if num < 1: # Condición base: no puede haber menos de un bloque
        return num
    else:
         # Se suma recursivamente la cantidad inicial mas la cantidad inicial (actualizada) menos 1
         return num + contar_bloques(num - 1) 

# Se solicita el valor inicial para la prueba
num = int(input("Ingrese la cantidad de bloques del nivel más bajo: "))
print(f"En base a los {num} bloques iniciales, se necesitaran {contar_bloques(num)} en total para completar la pirámide.")



'''
8- Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
aparece ese dígito dentro del número. 
      Ejemplos: 
contar_digito(12233421, 2)   → 3   
contar_digito(5555, 5)       → 4   
contar_digito(123456, 7)     → 0  
'''

print("\nEjercicio 8\n")

def contar_digito(numero, digito):
    if numero == 0: # Condisión base
        return 0
    else:       # operador ternario................más, el resultado de las recursiones
       return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

# Se solicitan los valores iniciales para la prueba
numero = int(input("Ingrese un número entero positivo a analizar: "))
digito = int(input("Ingrese el dígito a analizar: "))
# Se imprime el resultado
print(f"El dígito {digito} se repite {contar_digito(numero, digito)} veces dentro del número {numero} ")