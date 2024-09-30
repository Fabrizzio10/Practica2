alumnos={}
numerodealumnos=int(input("Ingrese el número de alumnos del curso: "))
for _ in range(numerodealumnos):
    z=input("Ingrese el nombre del alumno: ")
    notas=[]
    for x in range(1,4):
        n=input(f"Ingrese la nota {x} del alumno:")
        notas.append(n)
    alumnos[z]=notas
for z,notas in alumnos.items():     
    print(z,notas)
    

        





