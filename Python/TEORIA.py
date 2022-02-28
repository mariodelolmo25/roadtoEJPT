# ----- TEMA 3. PARTE 1: Variables -----
# Diferentes tipos de varibles (y datos) que se reconocen con diferente formato.
entero = int(1)
float = float(0.5)
booleana = True
cadena = "En un lugar de la Mancha..."

lista = ["Madrid", "París", "Berlín"]
tupla = ("Madrid", "París", "Berlín")
rango = range(9)

diccionario = {
    "Nombre": "Fernando",
    "Apellidos": "Alonso",
    "Podios": "98"
}

# Asignación múltiple
x,y,z = "Juan", "Pedro", "Marta"
r=s=t=8

# Cambio de tipo de valor (Casting)
# -> int() | float() | str()
var1 = int(1)
var2 = (7.2)
var3 = str("de cuyo nombre no quiero acordarme.")

# Mostar el tipo de valor que tiene una variable
# -> type()
type(entero) # Devuelve "<class 'int'>"
type(float) # Devuelve "<class 'float'>"
type(booleana) # Devuelve "<class 'bool'>"
type(cadena) # Devuelve "<class 'str'>"

# Operadores Aritméticos
suma = x + y
resta = x - y
multiplicacion = x * y
división = x / y
modulo = x % y # El resto de la división

# Operadores de Asignación
x = 1 # Asignación
x += 1 #Suma
x -= 1 # Resta
x *= 2 # Multiplicación
x /= 2 # División
x %= 2 # Módulo

# Operadores de Comparación
x == y # Igual que
x != y # Distinto que
x > 5 # Mayor que
x < 5 # Menor que
x >= 5 # Mayor o igual que
x <= 5 # Menor o igual que

# Operadores Lógicos
x < 5 and x < 10 # Y si... -> and
x < 5 or x < 10 # O si... -> or
not(x == 5 or x == 10) # Invertir el resultado si es True -> not

# Estructuras de Control
    # Condicional: IF
if x == "gato": # Si se cumple (True) lo ejecuta
    print ("miau")
elif x == "perro": # Ejecuta si esta otra condición se cumple
    print ("guau")
else: # Ejecuta si no se cumple la condición del if ni elif
    print ("no miau ni guau")
  
    # Bucle: WHILE
        # Mientras que la condición se cumpla se ejecuta constantemente hasta que no lo sea.
while x > 10 and x < 20:
    print ("Se cumple un ciclo hasta 10")
    

    # Bucle: FOR
        # 
