'''
Realiza una función que devuelva el área de un rectángulo a partir de su base y su altura.
La función se llamará area_rectangulo().
La base y la altura se pedirán al usuario por teclado
'''

def area_rectangulo(base, altura): # Definimos la función
    area = base * altura
    return area

base = int(input("Indique la base del rectángulo: ")) #Solicitamos la base al usuario
altura = int(input("Indique la altura del rectángulo: ")) #Solicitamos la altura al usuario
area = area_rectangulo(base, altura) # Guardamos en una variable la devolución de la función
print("El área del rectángulo es: ", area) # Imprimimos el resultado