def primo(z):
    if z < 2:
        return False
    for i in range(2, int(z**0.5) + 1):
        if z % i == 0:
            return False
    return True

def suma():
    suma = 0
    for numero in range(2, 100):
        if primo(numero):
            suma += numero
    return suma

resultado = suma()
print(resultado)