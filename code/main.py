import sys

from graph import Graph
from singlehouse import Singlehouse
from bungalow import Bungalow
from maison import Maison
from moving_hillclimber import Moving_Hillclimber
from randomstate_hillclimber import Randomstate_Hillclimber
from annealing import Simulated_Annealing


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


# ---------------------- Random --------------------

# Just comment out the below lines when Random algorithm is not needed 
# when using this algorithm comment out everything below the -----

# loop = input("How many random states do you want to generate: ")

# while not loop.isdigit():
#    loop = input("Insert number of runs: ")
# loops = int(loop)
# randomstate_hillclimber = Randomstate_Hillclimber(loops, all_houses, area)
# randomstate_hillclimber.looper()

# -------------------------------------------------------------------


# ---------------------- Moving Hillclimber -------------------------

# Just comment out the below lines when the moving hillclimber is not needed 
# When using this algorithm comment out the random state hillclimber and everything below the -----

# total_change = input("How many changes do you want to make? ")
# while not total_change.isdigit():
#     total_change = int(input("Insert number of changes: "))
# total_changes = int(total_change)

# moving_hillclimber = Moving_Hillclimber(total_changes, all_houses, area)
# moving_hillclimber.move_houses()
    
# -------------------------------------------------------------------------



# ---------------------- Simulated Annealing --------------------

# Just comment out the below lines when simulated annealing is not needed 
# when using this algorithm comment out everything below the -----

# changes = input("how many changes per random state do you want to make: ")
# while not changes.isdigit():
#    changes = input("Insert number of changes: ")

# changes = int(changes)
# simulated_annealing = Simulated_Annealing(changes, all_houses, area)
# simulated_annealing.simulate()

# -------------------------------------------------------------------
