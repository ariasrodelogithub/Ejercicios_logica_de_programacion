
#  * Reto #1
#  * ¿ES UN ANAGRAMA?
#  * Fecha publicación enunciado: 03/01/22
#  * Fecha publicación resolución: 10/01/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
#  * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
#  * NO hace falta comprobar que ambas palabras existan.
#  * Dos palabras exactamente iguales no son anagrama.
#  *

def are_anagrams(word1: str, word2: str) -> bool:
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    
    if word1 != word2:
        return "".join(sorted(word1)) == word2
            
    return False   


data = are_anagrams("roma", "amor")
print(data)