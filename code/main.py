from graph import Plattegrond
from singlehouse import Singlehouse
from bungalow import Bungalow
from maison import Maison
import matplotlib.pyplot as plt

wijk = input("Voer wijk_nummer in: ")
while wijk not in ["wijk_1", "wijk_2", "wijk_3"] : 
    print("Kies tussen: wijk_1, wijk_2, wijk_3")
    wijk = input("Voer wijk_nummer in: ")

Plattegrond(wijk)


total_houses = int(input("Voer de gewenste huizenvariant in: "))
while total_houses not in ["20", "40", "60"] : 
    print("Kies tussen: 20, 40, 60")
    total_houses = int(input("Voer de gewenste huizenvariant in: "))

# Determine the total number of houses for every variation
total_singlehouses = 2 * total_houses
total_bungalows = 3 * total_houses
total_maisons = 4 * total_houses

print(total_bungalows)
print(total_singlehouses)
print(total_bungalows)
print(total_maisons)

for singlehouse in total_singlehouses:
    singlehouse = Singlehouse()
    print(singlehouse.price)




