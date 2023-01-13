'''
Realizar una función llamada imc().
Esta función nos proporcionará el estado nutricional de una persona.
Esto es; la clasificación de su índice de masa corporal (IMC), según la tabla proporcionada.
La función recibirá el peso (en kilos) y la talla de una persona (en metros con dos decimales),
datos a partir de los cuales se puede calcular el IMC cómo:

IMC = peso / (altura * altura)

Clasificación: IMC (Kg/m^2)

Bajo peso: < 18.50
Normal: [18.50, 25.00)
Sobrepeso: >= 25.00
Obesidad: >= 30.00
'''

def imc(peso, altura): # Definimos la funcion
    imc = peso / (altura * altura)  # Hacemos el cálculo según la fórmula facilitada
    if imc < 18.50:  # Establecemos la clasificación según los rangos que nos han dado
        clasificacion = "Bajo peso"
    elif imc >= 18.50 and imc < 25.00:
        clasificacion = "Normal"
    elif imc >= 25.00 and imc < 30.00:
        clasificacion = "Sobrepeso"
    else:
        clasificacion = "Obesidad"
    return clasificacion # Devolvemos el valor que nos da la funcion

peso = round(float(input("Introduzca su peso en kilos: ")),2) # Solicitamos el peso al usuario
altura = round(float(input("Introduzca su altura en metros: ")),2) # Solicitamos la altura al usuario
clasificacion = imc(peso, altura) # Asignamos a una variable la devolución de la función
print("Su estado nutricional es: ", clasificacion) # Imprimimos lo que nos solicita el problema