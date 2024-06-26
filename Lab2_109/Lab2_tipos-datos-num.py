
# Abre el archivo .md y lee su contenido
with open('C:/Users/Buba/Desktop/hello_python/Lab2_109/readme_lab109.md', 'r') as file:
    markdown_content = file.read()

# Imprime el contenido del archivo Markdown
print(markdown_content)

'''Ejercicio 1: números y operaciones báscas de Python'''
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


'''Ejercicio 2: Presentar el tipo de dato entero'''

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


"""Ejercicio 3: Presentar el tipo de dato flotante"""

# Asignar un valor flotante a la variable myValue
myValue = 3.14

# Imprimir el valor de la variable en la consola
print(myValue)

# Imprimir el tipo de dato de la variable
print(type(myValue))

# Convertir el valor y el tipo de dato a cadena y combinarlos en un solo mensaje
print(str(myValue) + " es del tipo de dato " + str(type(myValue)))
