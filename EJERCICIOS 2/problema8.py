def calcular_factorial(num):
    resultado = 1
    for i in range(1, num + 1):  
        resultado *= i
    return resultado 
numero = int(input("Ingresa un número para calcular su factorial: "))
print(f"El factorial de {numero} es: {calcular_factorial(numero)}")