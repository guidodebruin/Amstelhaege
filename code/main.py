from Graph import Graph
from singlehouse import Singlehouse
from bungalow import Bungalow
from maison import Maison
import matplotlib.pyplot as plt
import csv
import sys

# Request user for area number
if len(sys.argv) < 3:
    print("Choose a specific area_number and number of houses")
    sys.exit(1)
elif sys.argv[1] not in ["area_1", "area_2", "area_3"]:
    print("Choose between: area_1, area_2, area_3")
    sys.exit(1) 
elif sys.argv[2] not in ["20", "40", "60"]:
    print("Choose between: 20, 40, and 60")
    sys.exit(1)   
else:
    area = sys.argv[1]

area = Graph(area)   

# Determine the total number of houses for every variation
total_houses = int(sys.argv[2])
total_singlehouses = 0.6 * int(total_houses)
total_bungalows = 0.25 * int(total_houses)
total_maisons = 0.15 * int(total_houses)

all_houses = []


# roep random class aan


# Add the house objects to a list
for singlehouse in range(int(total_singlehouses)):
    singlehouse = Singlehouse()
    all_houses.append(singlehouse)
    print(singlehouse.price)

for bungalow in range(int(total_bungalows)):
    bungalow = Bungalow()
    all_houses.append(bungalow)
    print(bungalow.price)

for maison in range(int(total_maisons)):
    maison = Maison()
    all_houses.append(maison)
    print(maison.price)

# sent house info to graph
area.load_houses(all_houses) 

# Writing output file
with open('output.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "corner_1", "corner_2", "corner_3", "corner_4", "type"])
    for house in all_houses:
        writer.writerow([house.id, house.corner_1, house.corner_2, house.corner_3, house.corner_4])