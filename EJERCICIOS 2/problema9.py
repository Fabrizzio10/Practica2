def quitar_vocales(texto):
    vocales = "aeiouAEIOU"
    resultado = "" 

    for letra in texto:
        if letra not in vocales:  
            resultado += letra 

    return resultado  
cadena = input("Escribe algo: ")
texto_sin_vocales = quitar_vocales(cadena)
print(texto_sin_vocales)