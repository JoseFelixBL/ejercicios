"""/
Ejercicio 2 de pythondiario./
"""

"""/
Ejercicio 1
La función max() del ejercicio 1 (primera parte) y la función max_de_tres() /
del ejercicio 2 (primera parte), solo van a funcionar para 2 o 3 números. /
Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. /
Escribir una función max_in_list() que tome una lista de números y devuelva /
el más grande.
"""


# def max_in_list(lista):
#     """Devolver el más grande."""
#     max = lista[0]
#     for num in lista[1:]:
#         if num > max:
#             max = num
#     return max


# lista = [1, 2, 456, 2, 789, 2, 2356, 56, -1234545]
# print(lista, max_in_list(lista))

"""/
Ejercicio 2
Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.
"""


# def mas_larga(lista_pal):
#     """Devolver palabra más larga."""
#     pal_larga = ""
#     for pal in lista_pal:
#         if len(pal) > len(pal_larga):
#             pal_larga = pal
#     return pal_larga


# lista_pal = ["Chanchito", "Feliz", "espialidoso", "palíndrome"]
# print(lista_pal, mas_larga(lista_pal))

"""/
Ejercicio 3
Escribir una función filtrar_palabras() que tome una lista de palabras /
y un entero n, y devuelva las palabras que tengan más de n caracteres.
"""


# def filtrar_palabras(lista_pal, n):
#     """Devolver las más largas que n caracteres."""
#     return [pal for pal in lista_pal if len(pal) > n]


# lista_pal = ["Chanchito", "Feliz", "espialidoso", "palíndrome"]
# print(lista_pal, filtrar_palabras(lista_pal, 1))
# print(lista_pal, filtrar_palabras(lista_pal, 5))
# print(lista_pal, filtrar_palabras(lista_pal, 9))

"""/
Ejercicio 4
Escribir un programa que le diga al usuario que ingrese una cadena. /
El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
"""


# def num_upper(cadena):
#     """Cuantas mayúsculas hay."""
#     num_mayus = 0
#     for char in cadena:
#         if char.isupper():
#             num_mayus += 1
#     return num_mayus


# print(num_upper("Hola Mundo"))
# cadena = """/
# Ejercicio 4
# Escribir un programa que le diga al usuario que ingrese una cadena. /
# El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
# """
# print(num_upper(cadena))


"""/
Ejercicio 5
Construir un pequeño programa que convierta números binarios en enteros.
"""


# def bin_a_int(binario):
#     """Pasar de binario a entero"""
#     entero = 0
#     binario = str(binario)
#     exp = 0
#     # Los binarios tienen la forma 8 = '1b1000', hay que eliminar los 2 de izq.
#     for bit in binario[-1:1:-1]:
#         entero += int(bit) * (2**exp)
#         exp += 1
#     return entero


# # n = 8
# # binario = bin(n)
# # print(n, binario, bin_a_int(binario))
# print(bin_a_int(bin(1)))
# print(bin_a_int(bin(2)))
# print(bin_a_int(bin(3)))
# print(bin_a_int(bin(4)))
# print(bin_a_int(bin(8)))
# print(bin_a_int(bin(25)))

"""/
Ejercicio 6
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla.
"""


# def edad(y_nacimiento, y_actual):
#     """Calcular edad en este año."""
#     return y_actual - y_nacimiento


# y_actual = int(input("Ingrese el año actual: "))
# print()
# personas = []
# for _ in range(3):
#     nombre = input("Ingrese el nombre: ")
#     y_nac = int(input("Ingrese su año de nacimiento: "))
#     personas.append((nombre, y_nac))
#     print()


# for nombre, y_nac in personas:
#     print(f"Este año {nombre} cumplirá {edad(y_nac, y_actual)} años.")


"""/
Ejercicio 7
Definir una tupla con 10 edades de personas.
Imprimir la cantidad de personas con edades superiores a 20.
Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.
"""

# print("Ingrese las edades de tantas personas como quiera.")
# print("Para terminar marque '0'.")

# edades = []
# edad = int(input("Edad: "))
# while edad:
#     edades.append(edad)
#     edad = int(input("Edad: "))
# tupla_edades = tuple(edades)
# mayores_20 = 0
# for edad in tupla_edades:
#     if edad > 20:
#         mayores_20 += 1

# print(f"La cantidad de personas mayores de 20 años son {mayores_20}.")

"""/
Ejercicio 8
Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)
"""
# print("Ingrese tantos nombres como quiera.")
# print("Termine con <enter>")

# nombre = input("Nombre: ")
# nombres = []
# while nombre:
#     nombres.append(nombre)
#     nombre = input("Nombre: ")

# por_a = 0
# for nombre in nombres:
#     if nombre[0].lower() == "a":
#         por_a += 1

# print(f"La cantidad de  nombres que eomienzan por 'a' es: {por_a}")

"""/
Ejercicio 9
Crear una función contar_vocales(), que reciba una palabra y cuente /
cuantas letras "a" tiene, cuantas letras "e" tiene y así hasta completar /
todas las vocales.
Se puede hacer que el usuario sea quien elija la palabra.
"""


# def contar_vocales(cadena):
#     """Contar vocales"""
#     num_vocales = dict()
#     for vocal in "aeiou":
#         num_vocales[vocal] = 0

#     for char in cadena:
#         if char.lower() in "aeiou":
#             num_vocales[char.lower()] += 1
#     return num_vocales


# cadena = input("Escribe algo: ")
# vocales = contar_vocales(cadena)
# print("El número de las vocales encontradas son: ")
# for vocal in "aeiou":
#     print(f"\t'{vocal}': {vocales[vocal]}")

"""/
Ejercicio 10
Escriba una función es_bisiesto() que determine si un año determinado /
es un año bisiesto.
    Todos los años bisiestos son divisibles entre 4.
    Aquellos años que son divisibles entre 4, pero no entre 100, son bisiestos.
    Los años que son divisibles entre 100, pero no entre 400, no son bisiestos.
    Sin embargo, los años divisibles entre 100 y entre 400 sí que son bisiestos.
"""


def es_bisiesto(year):
    """Calcular si es bisiesto."""
    if ((year % 4 == 0) and (year % 100 != 0)) or ((year % 100 == 0) and (year % 400 == 0)):
        return True
    return False


while True:
    year = input("Escriba un año: ")
    if year:
        if es_bisiesto(int(year)):
            print(f"El año {year} es bisiesto.")
        else:
            print(f"El año {year} NO es bisiesto.")
    else:
        break
