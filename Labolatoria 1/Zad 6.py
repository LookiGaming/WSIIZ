# Zad 6

# A)
#droga = float(input("Podaj przebytą drogę w km: "))
#spalanie = float(input("Podaj średnie spalanie (l/100 km): "))

#cena = 6.5

#zuzycie = droga*spalanie/100
#koszt = zuzycie*cena

#print("Przewidywane zużycie paliwa:", round(zuzycie, 2), "l")
#print("Szacowany koszt podróży:", round(koszt, 2), "zł")

# B)

#import random

#droga = random.randint(100, 1000)

#spalanie = float(input("Podaj średnie spalanie (l/100 km): "))
#cena = float(input("Podaj aktualną cenę paliwa za litr: "))

#zuzycie = droga*spalanie/100
#koszt = zuzycie*cena

#print("Wylosowana droga:", droga, "km")
#print("Przewidywane zużycie paliwa:", round(zuzycie, 2), "l")
#print("Szacowany koszt podróży:", round(koszt, 2), "zł")

# C)

import random

droga = random.randint(100, 1000)

spalanie = float(input("Podaj średnie spalanie (l/100 km): "))
cena = float(input("Podaj aktualną cenę paliwa za litr: "))

zuzycie = droga*spalanie/100
koszt = zuzycie*cena

print(f"Wylosowana droga: {droga} km")
print(f"Przewidywane zużycie paliwa: {zuzycie:.2f} l")
print(f"Szacowany koszt podróży: {koszt:.2f} zł")