PI = 3.1416
print("ingrese Radio y Alto: ")
RADIO = float(input("Radio: "))
print("ingrese el valor de Alto")
ALTO = float(input("Alto: "))

VOL = PI * RADIO ** 2 * ALTO
ARE = 2 * PI *RADIO*(RADIO+ALTO)

print("\nSalida")

print("VOLumen: ",VOL)
print("Area: ",ARE)
