# List Comprehension

# Ejemplo 1: Una lista de los cuadros del 1 al 5
cuadro_tradicional = []

for i in range(1, 6):
    cuadro_tradicional.append(i ** 2)
    
print(f'\nCuadro metodo tradicional: {cuadro_tradicional}\n')


# Usando list comprehension
cuadros = [i ** 2 for i in range(1, 6)]
print(f'\nCuadrados con list comprehension: {cuadros}\n')

# Ejemplo 2: Filtrar solo los numeros pares de la lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Metodo tradicional
pares_tradicional = []

for numero in numeros:
    if numero % 2 == 0:
        pares_tradicional.append(numero)
        
print(f'\nPares con el metodo tradicional: {pares_tradicional}\n')


# Usando list comprehension
pares = [
    numero for numero in numeros if numero % 2 == 0
]

print(f'\nPares con list comprehension: {pares}\n')


# Ejemplo 3: Crear una lista con el doble de cada numero si es mayor a 3
dobles = [n * 2 for n in numeros if n > 3]
print(f'\nDobles mayores a 3: {dobles}\n')


# Ejemplo 4: Convertir cada letra a mayuscula en una lista de caracteres

letras = ['a', 'b', 'c']

letras_mayus = [letra.upper() for letra in letras]
print(f'\nLetras en mayusculas: {letras_mayus}\n')


# Ejemplo 5: Una lista de tuplas del 1 al 5
tuplas = [(n, n ** 2) for n in range(1, 6)]

print(f'\nLista de las tuplas: {tuplas}\n')


# Ejemplo 6: Una lista con todos los elementos de una matriz 2D

matriz = [
    [1, 2, 3],
    [4,5,6],
    [7,8,9]
]

elementos = [elemento for fila in matriz for elemento in fila]

print(f'\nElementos de la matriz: {elementos}\n')



mi_lista = [i + 1 for i in range(10)]

print(f'\nMi lista con incremento con 1: {mi_lista}\n')

mi_lista = [i * 2 for i in range(10)]

print(f'\nMi lista multiplicada por 2: {mi_lista}\n')

mi_lista = [i * i for i in range(10)]

print(f'\nMi lista multiplicado por si mismo: {mi_lista}\n')


def suma_cinco(numero):
    return numero + 5

mi_lista = [suma_cinco(i) for i in range(10)]

print(f'\nMi lista con suma de 5: {mi_lista}\n')