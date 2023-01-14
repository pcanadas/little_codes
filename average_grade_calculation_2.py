'''
Se solicita notas al usuario hasta que no introduzca ninguna, momento en el cual el programa para
la introducción de notas y devuelve la media aritmética de las notas introducidas.
'''
def notas(): # Función que pide las notas al usuario
    notas = []
    while True:
        numero = input("Introduzca una nota: ") # Pedimos al usuario una nota
        notas.append(numero)
        if numero == "":
            notas.pop()
            print("Se ha completado la introducción de notas.")
            break
    return notas
def media(suma, divisor): # Función que realiza la media
    media = suma / divisor
    return media

notas = notas()
notas_float = [float(x) for x in notas]
print("La nota media es: ", media(sum(notas_float), len(notas)))