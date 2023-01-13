'''
Realiza una función que devuelva el área de un círculo a partir de un radio.
La función se llamará area_circulo().
El radio se pedirá al usuario por teclado
'''

def area_circulo(radio): # Definimos la función
    pi = 3.14159
    area = (radio ** 2) * pi
    return area

radio = int(input("Indique el radio del círculo: ")) # Solicitamos el radio al usuario
area = area_circulo(radio) # Introducimos en una variable el return de la función
print("El área del círculo es: ", area) # Imprimimos el resultado