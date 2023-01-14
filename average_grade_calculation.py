'''
Función para crear una lista con las notas que ingrese el usuario y mostrar la media aritmética
de los elementos de esa lista
'''
def notas(n): # Función que pide tantas notas como nos haya indicado el usuario
    notas = []
    for i in range(n):
        numero = float(input("Introduzca una nota: ")) # Pedimos al usuario un número
        notas.append(numero)
    return notas
def media(suma, divisor): # Función que realiza la media
    media = suma / divisor
    return media

n = int(input("Número de notas que va a introducir: "))
notas = notas(n)
print("La nota media es: ", media(sum(notas), len(notas)))
