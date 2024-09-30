def divisores_propios(z):
    divisores = []
    for i in range(1, z):  
        if z % i == 0:  
            divisores.append(i)
    return divisores
def es_numero_perfecto(z):
    divisores = divisores_propios(z)
    suma_divisores = sum(divisores)  
    return suma_divisores == z  


def encontrar_numeros_perfectos():
    for num in range(1, 1000):  
        if es_numero_perfecto(num):
            print(f"{num} es un número perfecto")

encontrar_numeros_perfectos()