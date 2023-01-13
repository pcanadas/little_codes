'''
Realizar un programa que realice las siguientes tareas:

Paso 1) solicitar al usuario una contraseña y guardarla en una variable
Paso 2) pedir al usuario introducir la contraseña para loguearse
        si la contraseña es correcta mostramos "Login correcto"
        si la contraseña no es correcta se le tendrá que mostrar un mensaje de "Login fallido. Intento 1",
        donde 1 será una variable contador que irá incrementandose hasta llegar a 5.
        En ese punto reiniciamos el programa y volveremos al Paso 1
'''
def password():
    password = input("Ingrese una contraseña: ") # Solicitamos una contraseña
    return password

def login(word):
    reinicioLogin = "no" # Creamos variable de reinicio
    contador = 1 # Creamos la variable contador
    while contador <= 5: # Establecemos que queremos que se repita la pregunta 5 veces como máximo
        password_login = input("Introduzca su contraseña para loguearse: ") #Solicitamos su contraseña al usuario
        if word != password_login:
            print("Login fallido. Intento", contador)  # Indicamos que la contraseña no es correcta
            contador += 1  # Aumentamos contador
        else:
            print("Login correcto") # Indicamos al usuario que el login es correcto
            break            # Finalizamos la iteración
    if contador == 6: # Establecemos cuando debe reiniciarse la pregunta de la contraseña
        reinicioLogin = "si"
    return reinicioLogin

reinicio = "si"
while reinicio == "si":  # Ejecutamos nuestro programa
    word = password()
    reinicio = login(word)