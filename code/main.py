from Graph import Plattegrond
from singlehouse import Singlehouse
from bungalow import Bungalow
from maison import Maison
import matplotlib.pyplot as plt
import csv

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

singlehouse_list = []
bungalow_list = []
maison_list = []

for singlehouse in range(int(total_singlehouses)):
    singlehouse = Singlehouse()
    singlehouse_list.append(singlehouse)
    print(singlehouse.price)

for bungalow in range(int(total_bungalows)):
    bungalow = Bungalow()
    bungalow_list.append(bungalow)
    print(bungalow.price)

for maison in range(int(total_maisons)):
    maison = Maison()
    maison_list.append(maison)
    print(maison.price)


# writing output file
with open('output.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "corner_1", "corner_2", "corner_3", "corner_4", "type"])
    for singlehouse in singlehouse_list:
        writer.writerow([singlehouse.id, singlehouse.corner_1, singlehouse.corner_2, singlehouse.corner_3, singlehouse.corner_4, singlehouse.type])
    for bungalow in bungalow_list:
        writer.writerow([bungalow.id, bungalow.corner_1, bungalow.corner_2, bungalow.corner_3, bungalow.corner_4, bungalow.type])
    for single_maison in maison_list:
        writer.writerow([maison.id, maison.corner_1, maison.corner_2, maison.corner_3, maison.corner_4, maison.type])


