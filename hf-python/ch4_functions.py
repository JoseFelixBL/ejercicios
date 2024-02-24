"""Ejercicios de Head First Python"""


def search4vowels(phrase: str) -> set:
    """Return any vowels found in a supplied phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search_4_letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return any letters found in a supplied phrase."""
    return set(letters).intersection(set(phrase))


mi_phrase = input("Introduzca una frase: ")
mis_letters = input("Introduzca los caracteres que quiere buscar: ")

print(search4vowels(mi_phrase))
print(search_4_letters(mi_phrase, mis_letters))
print(help(search4vowels))
print(help(search_4_letters))
