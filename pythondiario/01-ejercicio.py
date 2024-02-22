"""Tanda de ejercicios de Pythondiario"""

"""/
1 - Definir una función max() que tome como argumento dos números y devuelva /
el mayor de ellos. (Es cierto que python tiene una función max() incorporada, /
pero hacerla nosotros mismos es un muy buen ejercicio./
"""


# def mi_max(a, b):
#     """/
#     Retornar el mayor entre 2 números./
#     """
#     if a > b:
#         return a
#     return b


# while True:
#     a = input("Escriba un número: ")
#     b = input("escriba otro número: ")
#     print(
#         f"Entre {a}, {b} y {c} el mayor es {mi_max(int(a), int(b))}\n")


"""/
2 - Definir una función max_de_tres(), que tome tres números como argumentos y/
 devuelva el mayor /de ellos./
"""


# def max_de_tres(a, b, c):
#     """Retornar el mayor entre 3 número."""
#     if a > b:
#         if a > c:
#             return a
#         return c
#     elif b > c:
#         return b
#     return c


# while True:
#     a = input("Escriba un número: ")
#     b = input("escriba otro número: ")
#     c = input("escriba un tercer número: ")
#     print(
#         f"Entre {a}, {b} y {c} el mayor es {max_de_tres(int(a), int(b), int(c))}\n")


"""/
3 - Definir una función que calcule la longitud de una lista o una cadena /
dada. (Es cierto que python tiene la función len() incorporada, pero /
escribirla por nosotros mismos resulta un muy buen ejercicio./
"""


# def len_lista(lista):
#     """Calcular longitud de una lista."""
#     cont = 0
#     for _ in lista:
#         cont += 1
#     return cont


# lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 21, 2345, "hola"]
# print(f"La lista: {lista} mide {len_lista(lista)}")


"""/
4 - Escribir una función que tome un carácter y devuelva True si es una /
vocal, de lo contrario devuelve False./
"""


# def es_vocal(char):
#     """Si es vocal -> True"""
#     if char.lower() in "aeiou":
#         return True
#     return False


# for char in "Hola mundo":
#     if es_vocal(char):
#         print(f"El caracter '{char}' es vocal.")
#     else:
#         print(f"El caracter '{char}' NO es vocal.")

"""/
5 - Escribir una función sum() y una función multip() que sumen y /
multipliquen respectivamente todos los números de una lista. Por ejemplo: /
sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24./
"""


# def sum(lista):
#     """Sumar elementos de la lista"""
#     suma = 0
#     for num in lista:
#         suma += num
#     return suma


# def multip(lista):
#     """Multiplicar elementos de la lista"""
#     producto = 1
#     for num in lista:
#         producto *= num
#     return producto


# lista = [1, 2, 3, 4]
# print(f"La suma de {lista} es {sum(lista)}")
# print(f"El producto de {lista} es {multip(lista)}")

"""/
6 - Definir una función inversa() que calcule la inversión de una cadena. /
Por ejemplo la cadena "estoy probando" debería devolver la cadena /
"odnaborp yotse"/
"""


# def inversa(lista):
#     """Invertir una lista"""
#     invertida = list()
#     for elem in lista:
#         invertida.insert(0, elem)
#     return invertida


# # l1 = "Hola mundo"
# # l2 = "Chanchito feliz"
# l1 = [1, 2, 3]
# l2 = ["Hola", "mundo"]
# l3 = "Chanchito feliz"
# print(l1, inversa(l1))
# print(l2, inversa(l2))
# print(l3, inversa(l3), str(inversa(l3)))

# Para convertir una lista de caracteres en un str usar: ''.join(lista)

"""/
7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, /
palabras que tienen el mismo aspecto escritas invertidas), ejemplo: /
es_palindromo ("radar") tendría que devolver True./
"""


# def sin_blancos(texto):
#     """Quitar los espacios en blanco."""
#     # nuevo_texto = ""
#     # for char in texto:
#     #     if char != " ":
#     #         nuevo_texto += char
#     nuevo_texto = ''.join([char for char in texto if char != " "])
#     return nuevo_texto


# def reverse(texto):
#     """Dar la vuelta a un texto."""
#     al_reves = ""
#     for char in texto:
#         al_reves = char + al_reves
#     return al_reves


# def es_palindromo(texto):
#     """Sí o no es palíndromo."""
#     texto = sin_blancos(texto)
#     texto_al_reves = reverse(texto)
#     return texto.lower() == texto_al_reves.lower()


# print(es_palindromo("Amo la paloma"))
# print(es_palindromo("Hola mundo"))

"""/
8 - Definir una función superposicion() que tome dos listas y devuelva True /
si tienen al menos 1 miembro en común o devuelva False de lo contrario. /
Escribir la función usando el bucle for anidado./
"""


# def superposición(lista1, lista2):
#     """Comprobar si tienen algún elemento en común."""
#     for elem1 in lista1:
#         for elem2 in lista2:
#             if elem1 == elem2:
#                 return True
#     return False


# lista1 = [1, 2, 3, 4, 5]
# lista2 = [6, 7, 8, 9, 0]
# lista3 = [11, 12, 13, 14, 1, 15, 8]
# print(superposición(lista1, lista2))
# print(superposición(lista1, lista3))
# print(superposición(lista3, lista2))

"""/
9 - Definir una función generar_n_caracteres() que tome un entero n y /
devuelva el caracter multiplicado por n. Por ejemplo: /
generar_n_caracteres(5, "x") debería devolver "xxxxx"./
"""


def generar_n_caracteres(n, char):
    return n * char


# print(generar_n_caracteres(2, "-"))
# print(generar_n_caracteres(20, "*"))
# print(generar_n_caracteres(7, "A"))

"""/
10 - Definir un histograma procedimiento() que tome una lista de números /
enteros e imprima un histograma en la pantalla. Ejemplo: /
procedimiento([4, 9, 7]) debería imprimir lo siguiente:
****
*********
*******/
"""


def procedimiento(lista_ints):
    for num in lista_ints:
        print(generar_n_caracteres(num, "*"))


procedimiento([4, 9, 7])
