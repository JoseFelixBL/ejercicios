"""Ejercicios de Head First Python - Chapter 4"""


def search4vowels(phrase: str) -> set:
    """Return any vowels found in a supplied phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase.lower()))


def search_4_letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return any letters found in a supplied phrase."""
    return set(letters.lower()).intersection(set(phrase.lower()))


# mi_phrase = input("Introduzca una frase: ")
# mis_letters = input("Introduzca los caracteres que quiere buscar: ")

# print(search4vowels(mi_phrase))
# print(search_4_letters(mi_phrase, mis_letters))
# print(help(search4vowels))
# print(help(search_4_letters))
