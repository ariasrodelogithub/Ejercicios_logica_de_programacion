from unidecode import unidecode

def process_sentence(sentence: str) -> str:
    clean_sentence = unidecode(sentence).lower().replace(".", "").replace("!", "").replace(",", "")
    return clean_sentence

def convert_to_list(sentence: str) -> list:
    return sentence.split()

def count_duplicate_words(word_list: list) -> dict:
    dict_words = {}
    for word in word_list:
        if word in dict_words:
            dict_words[word] +=1
        else:
            dict_words[word] = 1

    return dict_words

frase = "¡Persiste, resiste, avanza! En cada desafío, descubre tu fortaleza. No te detengas, sigue adelante. Rompe barreras, supera límites. Tú eres tu mejor competencia. La vida te reta, tú decides cómo responder. ¡Ama, sueña, logra! La fuerza está en tu interior. Cree en ti, porque eres capaz de más de lo que imaginas. ¡Adelante, conquista tus sueños, sé imparable!"

processed_sentence = process_sentence(frase)
word_list = convert_to_list(processed_sentence)
word_count = count_duplicate_words(word_list)
print(word_count)
