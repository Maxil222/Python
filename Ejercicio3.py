print("ingrese número de respuestas correctas")
RC = int(input("Correctas: "))
print("ingrese número de respuestas incorrectas")
RI = int(input("Incorrectas: "))
print("ingrese número de respuestas en blanco")
RB = int(input("Respuesta en blanco: "))

PRC = RC*3
PRI = RI*-1
PRB = RB*0

PF = PRC + PRI + PRB 

print("El puntaje es: ",PF)