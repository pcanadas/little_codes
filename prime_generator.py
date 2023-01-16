def numPrime(x):
    '''
    Indica si un número es primo o no
    :return: True or False
    '''
    if x < 2:
        return False
    elif x == 2:
        return True
    for n in range(2, x):
        if x % n == 0:
            return False
    return True

def primeRange(a, b):
    '''
    Indica los números primos entre un rango de números
    :param a: Inicio del rango
    :param b: Fin del rango
    '''
    for z in range(a, b):
        if numPrime(z) == True:
            yield z

num1 = int(input("Introduzca el primer número del rango: "))
num2 = int(input("Introduzca el último número del rango: "))

print("Los números primos comprendidos en el rango indicado son: ", list(primeRange(num1, num2)))