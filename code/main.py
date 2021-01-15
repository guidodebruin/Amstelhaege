import random
import csv
import sys

from Graph import *
from singlehouse import Singlehouse
from bungalow import Bungalow
from maison import Maison

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

# Make the graph
area = Graph(area)   

# Determine the total number of houses for every variation
total_houses = int(sys.argv[2])
total_singlehouses = 0.6 * int(total_houses)
total_bungalows = 0.25 * int(total_houses)
total_maisons = 0.15 * int(total_houses)

all_houses = []

# Make the house objects and add to list
for singlehouse in range(int(total_singlehouses)):
    singlehouse = Singlehouse()
    all_houses.append(singlehouse)

for bungalow in range(int(total_bungalows)):
    bungalow = Bungalow()
    all_houses.append(bungalow)

for maison in range(int(total_maisons)):
    maison = Maison()
    all_houses.append(maison)

# Change overlapping coordinates
overlap = area.overlap(all_houses)
emptylist = []

while overlap != emptylist:
    for house in overlap:
        house.corner_lowerleft = house.return_corner2()
    overlap = area.overlap(all_houses)

# Closest distance tussen huizen vinden
for house in all_houses:
    output = area.closest_house(house, all_houses)

# print(overlap)

# sent house info to graph
area.load_houses(all_houses) 

# Writing output file
area.write_output(all_houses)


# Writing output file
# with open('output.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(["structure", "corner_1", "corner_2", "corner_3", "corner_4", "type"])
#     total_price = []
#     for house in all_houses:

#         if isinstance(house, Singlehouse):
#             x_coordinate = house.corner_lowerleft[0]
#             y_coordinate = house.corner_lowerleft[1]
#             new_x_coordinate = x_coordinate + 8
#             new_y_coordinate = y_coordinate + 8
#             corner_upperleft = [x_coordinate, new_y_coordinate]
#             corner_upperright = [new_x_coordinate, new_y_coordinate]
#             corner_lowerright = [new_x_coordinate, y_coordinate]
#             housetype = "SINGLEHOUSE"
#             total_price.append(house.price)
#             writer.writerow([house.id, corner_upperleft, house.corner_lowerleft, corner_upperright, corner_lowerright, housetype])

#         elif isinstance(house, Bungalow):
#             x_coordinate = house.corner_lowerleft[0]
#             y_coordinate = house.corner_lowerleft[1]
#             new_x_coordinate = x_coordinate + 11
#             new_y_coordinate = y_coordinate + 7
#             corner_upperleft = [x_coordinate, new_y_coordinate]
#             corner_upperright = [new_x_coordinate, new_y_coordinate]
#             corner_lowerright = [new_x_coordinate, y_coordinate]
#             housetype = "BUNGALOW"
#             total_price.append(house.price)
#             writer.writerow([house.id, corner_upperleft, house.corner_lowerleft, corner_upperright, corner_lowerright, housetype])
       
#         elif isinstance(house, Maison):
#             x_coordinate = house.corner_lowerleft[0]
#             y_coordinate = house.corner_lowerleft[1]
#             new_x_coordinate = x_coordinate + 12
#             new_y_coordinate = y_coordinate + 10
#             corner_upperleft = [x_coordinate, new_y_coordinate]
#             corner_upperright = [new_x_coordinate, new_y_coordinate]
#             corner_lowerright = [new_x_coordinate, y_coordinate]
#             housetype = "MAISON"
#             total_price.append(house.price)
#             writer.writerow([house.id, corner_upperleft, house.corner_lowerleft, corner_upperright, corner_lowerright, housetype])

#     writer.writerow(["networth", sum(total_price)])

        

        