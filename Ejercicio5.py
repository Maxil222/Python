from os import NGROUPS_MAX


print("ingrese el numero de Megas: ")
Mg = float(input("MegaByte "))
print("ingrese el numero de Gigas: ")
Gb = float(input("GigaByte "))
Mg = Gb*1024
MD = Mg/1.44
print(MD)
print("se necesitan disquete: "(MD))
