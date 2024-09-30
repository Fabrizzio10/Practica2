def convertir_fecha(fecha):
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    if '/' in fecha:
        partes = fecha.split('/') 
        if len(partes) != 3:  
            print("Inválido")
            return
        mes = int(partes[0])  
        dia = int(partes[1])  
        anio = int(partes[2])  
    else:
        partes = fecha.replace(',', '').split(' ') 
        if len(partes) != 3:  
            print("Inválido")
            return
        mes_texto = partes[0] 
        dia = int(partes[1])  
        anio = int(partes[2])  
        
        
        if mes_texto in meses:
            mes = meses.index(mes_texto) + 1  
        else:
            print("Mes inválido")
            return
    fecha = f"{anio}-{mes:02}-{dia:02}"
    return fecha


entrada_usuario = input("Ingresa una fecha en formato MM/DD/AAAA o 'Mes día, año': ")


fecha_convertida = convertir_fecha(entrada_usuario)
if fecha_convertida: 
    print(fecha_convertida)