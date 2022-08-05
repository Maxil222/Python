print("Ingrese número de partidos ganados")
PG = int(input("Partidos Ganados: "))
print("Ingrese número de partidos ganados")
PE = int(input("Partidos Empatados: "))
print("Ingrese número de partidos ganados")
PP = int(input("Partidos Perdidos: "))

PPG = PG*3
PPE = PE-1
PPP = PP*0

PT = PPG + PPE + PPP 
print("Puntaje Final: ",PT)