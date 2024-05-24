'''
V = π * r2 * h

Donde:
V es el volumen del cilindro.
π es la constante pi (aproximadamente 3.14159).
r es el radio de la base del cilindro.
h es la altura del cilindro.
'''

# pi = 3.1416

import math

# Definir la función estándar para calcular el volumen de un cilindro
def volumen_cilindro(radio, altura):
    return math.pi * radio**2 * altura

# Ejemplo de uso
radio = 2
altura = 5
pi = 3.1416
volumen = volumen_cilindro(radio, altura)
print(f"El volumen del cilindro es: {volumen}")

#################################################

# Definir la función lambda para calcular el volumen de un cilindro
vol_cilindro_lambda = lambda radio, altura: math.pi * radio**2 * altura

# Ejemplo de uso
radio = 5
altura = 10
vol_lambda = vol_cilindro_lambda(radio, altura)
print(f"El volumen del cilindro con lambda es: {vol_lambda}")

###############################################################
# V = π * r2 * h
# con pi
# Definir la función estándar para calcular el volumen de un cilindro
def volumen_cilindro(r, h):
    return pi * r**2 * h

# Ejemplo de uso
r = 5
h = 10
pi = 3.1416
volumen = volumen_cilindro(r, h)
print(f"El volumen del cilindro es: {volumen}")

#####################################################################
# Definir la función lambda para calcular el volumen de un cilindro
vol_cilindro_lambda = lambda r, h, pi : pi* r**2 * h

# Ejemplo de uso
r = 5
h = 10
vol = vol_cilindro_lambda(r, h, pi)
print(f"El volumen del cilindro con lambda es: {vol_lambda}")

###########################################

numeros = (1,2,3,4,5)

def cubico(number):
    return number**3     # devuelve al cubo
result = map(cubico, numeros)
resultLambda = map(lambda x: x**3, numeros)

print(list(result))
print(list(resultLambda))

################################################
# filtrar números mayores que 5
num = [1,2,3,4,5,6,7,8,9]
result = filter(lambda x: x>5, num)
print(list(result))

################################################

from functools import reduce

# bucles, donde la primera vuelta es x=1 y y=2
# acumulados del anterior
num = [1,2,3,4,5,6,7,8,9]
result = reduce(lambda x, y : x*2+y*2, num)  
print(result)

# 
num = [1,2,3,4,5,6,7,8,9]
result = reduce(lambda x, y : x+y, num, 4)  
print(result)

################################################
num = [1,2,3,4,5,6,7,8,9]
result = reduce(lambda x, y : x*2+y, num, 3)  
print(result)

################################################

def even_or_odd(number):
    if number %2 == 0: 
        print("even")
    else:
        print("odd")
        
even_or_odd(419)

pass
################################################

list=[1, 3, 4, 18, 23, 35, 100]

def even_or_odd(number):
    for number in list:
        if number %2 == 0:
            print("even")
        else:
            print("odd")
even_or_odd(list)
################################################

numbers = [1, 3, 4, 18, 23, 35, 100]

def even_or_odd(number_list):
    for number in number_list:
        if number % 2 == 0:
            print(f"{number} : even")
        else:
            print(f"{number} : odd")

even_or_odd(numbers)

################################################

def even_or_odd(number):
    if number % 2 == 0:
        return f"{number} : even"
    else:
        return f"{number} : odd"

# User input
user_input = int(input("Enter a number: "))
print(even_or_odd(user_input))


################################################

def placeholder_function():
    pass

class PlaceholderClass:
    pass

for i in range(10):
    pass

