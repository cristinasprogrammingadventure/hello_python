
# Abre el archivo .md y lee su contenido
with open('C:/Users/Buba/Desktop/hello_python/Lab2_109/readme_lab109.md', 'r') as file:
    markdown_content = file.read()

# Imprime el contenido del archivo Markdown
print(markdown_content)

#-------------------------------------------------------------------------------

'''Ejercicio 1: números y operaciones báscas de Python'''
'''Adición y Sustracción'''

# Definimos una Adición con números enteros, o de tipo 'integer'
add=(2+2)
print(add)

# sumamos y restamos 2 números enteros como si se tratase de una calculadora, sin definir previamente una variable.
2+2
4-2
# ---> TypeError: 'int' object is not iterable 
# ---> vemos que en VS (al contrario de Jupyter) no se ejecutan estas líneas, sino sólo las que tienen una función asociada

# vamos a usar una funcón de impresión en pantalla para sumar números
print(2 + 2)
print(4 + 2)

"""Multiplicación y División"""

print(2 * 2)
print(4 / 2)

#-------------------------------------------------------------------------------

'''Ejercicio 2: Tipo de dato entero

Para obtener más información sobre los tipos de datos, utilizará algunas funciones integradas. 
Una *función* es un fragmento de código reutilizable con un nombre. Utiliza una función mediante las siguientes acciones:

- llamarla por su nombre
- incluir una lista de una o más entradas llamadas *argumentos*, que se encuentran entre paréntesis

Python tiene varias funciones integradas que puede utilizar para escribir programas más útiles.
Un conjunto de funciones se denomina *biblioteca*. 
El conjunto de funciones integradas de Python se denomina *Biblioteca estándar de Python*.
'''

# usamos la función interna print para ver el texto con los típos de datos en pantalla
print("Python has three numeric types: int, float, and complex")

# Asignar un valor entero a la variable myValue
myValue = 1

# Imprimir el valor de la variable en la consola
print(myValue)

# Imprimir el tipo de dato de la variable
print(type(myValue))

# Convertir el valor y el tipo de dato a cadena y combinarlos en un solo mensaje
print(str(myValue) + " es del tipo de dato " + str(type(myValue)))

#-------------------------------------------------------------------------------

"""Ejercicio 3: Tipo de dato flotante

El tipo de dato entero solo almacena números enteros. 
Si desea almacenar un número con decimales necesita un nuevo tipo de dato denominado flotante.
"""

# Asignar un valor flotante a la variable myValue
myValue = 3.14

# Imprimir el valor de la variable en la consola
print(myValue)

# Imprimir el tipo de dato de la variable
print(type(myValue))

# Convertir el valor y el tipo de dato a cadena y combinarlos en un solo mensaje
print(str(myValue) + " es del tipo de dato " + str(type(myValue)))

#-------------------------------------------------------------------------------

"""Ejercicio 4: Tipo de dato complejo

En la matemática avanzada, un número imaginario es un número complejo, el cual se puede escribir como un número real que se multiplica por la unidad imaginaria i. El tipo de dato complejo es complicado porque tiene que representar una letra y un número, como 5j.
Vuelva al archivo en Python e escriba el siguiente código:
myValue=5j
"""

myValue=5j

# Escriba el valor de la variable con la función `print()`:
print(myValue)

# Obtenga el tipo de dato en la variable con la función `type()`:
print(type(myValue))

#Para combinar números y texto, utilice la función integrada `str()`:
print(str(myValue) + " is of the data type " + str(type(myValue)))

# Escriba el valor de la variable con la función print():
print(myValue)

# Obtenga el tipo de dato en la variable con la función type():
print(type(myValue))

# Para combinar números y texto, utilice la función integrada str():
print(str(myValue) + " is of the data type " + str(type(myValue)))



#---------------------------------------------------------------------------------

"""Ejercicio 5: Tipo de dato booleano

El tipo de datos bool (booleano) comprende los nombres permanentes *True* (Verdadero) y *False* (Falso), 
que se representan mediante los numerales *1* y *0*, donde *1 = Verdadero* y *0 = Falso*. 
El tipo de dato booleano se implementa como un subconjunto de los enteros y no se considera un tipo de dato real. Sin embargo, en algunos lenguajes de programación, se implementa como un tipo de dato diferente. 
Estos ejercicios denominan al tipo booleano de Python un *tipo de dato simulado*.
"""
7


