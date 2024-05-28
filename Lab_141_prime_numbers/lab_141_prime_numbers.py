'''
INSTRUCTIONS / ENUNCIADO:
Write a Python script to display all the prime numbers between 1 to 250.
Store the results in a results.txt file.
Test the script. Verify that it produced the expected results in the results.txt file.

what is a prime number  ? 
A prime number is a natural number greater than 1 that can only 
be divided by 1 and the number itself without leaving a remainder.
So 2 is the smallest prime number and the only even prime number. 
The number 1 is not considered a prime number.

# Check if num is less than or equal to 1:
    # if num <= 1: return False
    # Numbers less than or equal to 1 are not prime.

# Check if n is exactly 2: 
    # if num == 2: return True
    # 2 is the smallest and the only even prime number.

# Check if num is even:
    #if num % 2 == 0: return False
    # Any other even number greater than 2 cannot be prime because it would be divisible by 2.

# Check odd numbers starting from 3 up to the square root of num:
    # for i in range(3, int(num**0.5) + 1, 2)
    # Starts from 3 and skips even numbers by stepping 2 (i.e., checks 3, 5, 7, etc.).
 '''
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def main():
    results_file = "Lab_141_results.txt"
    with open(results_file, 'w') as file:
        for number in range(1, 251):
            if is_prime(number):
                file.write(f"{number}\n")
    print(f"Prime numbers between 1 and 250 have been written to {results_file}")

if __name__ == "__main__":
    main()

'''
EXPLIC:
is_prime(num): 
Simplificado para hacer comprobaciones iniciales rápidas y luego solo probar divisores impares hasta la raíz cuadrada de num.

    Retorna False si n es menor o igual a 1.
    Retorna True si n es igual a 2 (el único número primo par).
    Retorna False si n es divisible por 2 (y no es 2).
    Solo prueba los divisores impares hasta la raíz cuadrada de n para eficiencia.

Looping with range(3, int(n**0.5) + 1, 2):

    This loop starts checking for factors from 3 onwards.
    The check for divisibility by 2 is handled separately before this loop 
    because it's more efficient to directly check even numbers in one step rather than within the loop.

main():
Única función principal que:

    Define el archivo Lab_141_results.txt.
    Usa un with open para manejar el archivo, asegurándose de que se cierre correctamente.
    Itera sobre el rango de 1 a 250.
    Escribe cada número primo en una nueva línea del archivo.
    Imprime un mensaje de confirmación.
'''
