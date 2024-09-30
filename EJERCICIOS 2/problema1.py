#Problema 1
# Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
# en el rango de 1500 y 2700 (ambos incluidos)
# Lista para almacenar los números que cumplen la condición
lista_números=[]
for número in range(1500,2700):
    if int(número)%5==0 and int(número)%7==0:
     lista_números.append(número)
print(lista_números)