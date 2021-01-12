from graph import Graph
from singlehouse import Singlehouse
from bungalow import Bungalow
from maison import Maison
import matplotlib.pyplot as plt
import csv
import sys

# Request user for area number
# area = input("Enter the area number: ")
# while area not in ["area_1", "area_2", "area_3"] : 
#     print("Choose between: area_1, area_2, area_3")
#     area = input("Enter the area number: ")


if len(sys.argv) < 3:
    print("Choose a specific area_no.")
    sys.exit(1)
elif sys.argv[1] not in ["area_1", "area_2", "area_3"]:
    print("Choose between: area_1, area_2, area_3")
    sys.exit(1)  
elif sys.argv[2] not in ["20", "40", "60"]:
    print("Choose between: 20, 40, and 60")
    sys.exit(1)      

# Request user for the number of houses
# total_houses = input("Enter the number of houses: ")
# while total_houses not in ["20", "40", "60"] : 
#     print("Choose between: 20, 40, 60")
#     total_houses = input("Enter the number of houses: ")

# Determine the total number of houses for every variation
total_houses = int(sys.argv[2])
total_singlehouses = 0.6 * int(total_houses)
total_bungalows = 0.25 * int(total_houses)
total_maisons = 0.15 * int(total_houses)

singlehouse_list = []
bungalow_list = []
maison_list = []
all_houses = []

# Add the house objects to a list
for singlehouse in range(int(total_singlehouses)):
    singlehouse = Singlehouse()
    singlehouse_list.append(singlehouse)
    all_houses.append(singlehouse)
    print(singlehouse.price)

for bungalow in range(int(total_bungalows)):
    bungalow = Bungalow()
    bungalow_list.append(bungalow)
    all_houses.append(bungalow)
    print(bungalow.price)

for maison in range(int(total_maisons)):
    maison = Maison()
    maison_list.append(maison)
    all_houses.append(maison)
    print(maison.price)

# sent house info to graph
print(all_houses)

# Writing output file
with open('output.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "corner_1", "corner_2", "corner_3", "corner_4", "type"])
    for singlehouse in singlehouse_list:
        writer.writerow([singlehouse.id, singlehouse.corner_1, singlehouse.corner_2, singlehouse.corner_3, singlehouse.corner_4, singlehouse.type])
    for bungalow in bungalow_list:
        writer.writerow([bungalow.id, bungalow.corner_1, bungalow.corner_2, bungalow.corner_3, bungalow.corner_4, bungalow.type])
    for single_maison in maison_list:
        writer.writerow([maison.id, maison.corner_1, maison.corner_2, maison.corner_3, maison.corner_4, maison.type])


