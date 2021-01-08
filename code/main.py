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


total_houses = input("Voer de gewenste huizenvariant in: ")
while total_houses not in ["20", "40", "60"] : 
    print("Kies tussen: 20, 40, 60")
    total_houses = input("Voer de gewenste huizenvariant in: ")

# Determine the total number of houses for every variation
total_singlehouses = 0.6 * int(total_houses)
total_bungalows = 0.25 * int(total_houses)
total_maisons = 0.15 * int(total_houses)

for singlehouse in range(int(total_singlehouses)):
    singlehouse = Singlehouse()
    print(singlehouse.price)

for bungalow in range(int(total_bungalows)):
    bungalow = Bungalow()
    print(bungalow.price)

for maison in range(int(total_maisons)):
    maison = Maison()
    print(maison.price)




