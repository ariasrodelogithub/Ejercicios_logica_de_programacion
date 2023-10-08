
#  * Reto #0
#  * EL FAMOSO "FIZZ BUZZ"
#  * Fecha publicación enunciado: 27/12/21
#  * Fecha publicación resolución: 03/01/22
#  * Dificultad: FÁCIL
#  * Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
#  * - Múltiplos de 3 por la palabra "fizz".
#  * - Múltiplos de 5 por la palabra "buzz".
#  * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#  *

def fizz_buzz():
    for i in range(1, 101, 1):
        divisible_three = i % 3 == 0
        divisible_five = i % 5 == 0

        if divisible_three and divisible_five:
            print(i, "Fizz Buzz")

        elif divisible_three:
            print(f"{i} Fizz")

        elif divisible_five:
            print(f"{i} Buzz")
        
fizz_buzz()