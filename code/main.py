import sys

from graph import Graph
from singlehouse import Singlehouse
from bungalow import Bungalow
from maison import Maison


# Request user for area number and number of houses
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

# randomly relocate the invalid placed houses until a valid state is reached
area.randomly_assign_houses(all_houses)

# sent house info to graph
area.load_houses(all_houses)

# Calculate final houseprice
area.houseprices(all_houses)

# Writing output file
area.write_output(all_houses)       