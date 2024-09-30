Números_pares=[]
Números_impares=[]
Números_ingresados=[]
while True:
 print("¿Desea ingresar un número?:")
 z=input().lower() 
 if "si" in z:
  x=int(input("Ingrese su número:"))
  Números_ingresados.append(x)
  if x%2==0:
   Números_pares.append(x)
  if x%2==1:
   Números_impares.append(x)  
 elif "no" in z:
  break
print(Números_ingresados)
a=(len(Números_pares))
b=(len(Números_impares))
print("Cantidad de números pares:",str(a)) 
print("Cantidad de números impares:",str(b)) 
   
  
 


    