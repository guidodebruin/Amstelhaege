import sys

# from code.classes.House import House
from code.classes.singlehouse import Singlehouse
from code.classes.bungalow import Bungalow
from code.classes.maison import Maison
from code.classes.graph import Graph

from code.algorithms.randomstate_hillclimber import Randomstate_Hillclimber
from code.algorithms.moving_hillclimber import Moving_Hillclimber
from code.algorithms.annealing import Simulated_Annealing



#application/app2/some_folder/some_file.py

# sys.path.append('amstelhaege/code/classes/singlehouse.py/')
# sys.path.append('amstelhaege/code/classes/graph.py/')


# from code.classes.singlehouse import Singlehouse
# from code.classes.bungalow import Bungalow
# from code.classes.maison import Maison
# from code.classes.graph import Graph
# from code.algorithms.annealing import Simulated_Annealing
# from code.algorithms import moving_hillclimber
# from code.algorithms import randomstate_hillclimber
# from moving_hillclimber import Moving_Hillclimber
# from randomstate_hillclimber import Randomstate_Hillclimber
# from annealing import Simulated_Annealing


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

print("Choose the algorithm with which you want to perform the calculation")
print("Algorithmes available: Randomstate = 1, Hill Climber = 2, Simulated Annealing = 3")
chosen_algorithm = input("Please choose your algorithm by entering the corresponding number: ")

while chosen_algorithm not in ["1", "2", "3"]:
    print("Algorithmes available: Randomstate = 1, Hill Climber = 2, Simulated Annealing = 3")
    chosen_algorithm = input("Please choose your algorithm by entering the corresponding number: ")

# The user has chosen the random algorithm
if chosen_algorithm == "1":
    loop = input("How many random states do you want to generate: ")
 
    while not loop.isdigit():
       loop = input("Insert number of runs: ")
    loops = int(loop)
    randomstate_hillclimber = Randomstate_Hillclimber(loops, all_houses, area)
    randomstate_hillclimber.looper()

# The user has chosen the moving hill climber
elif chosen_algorithm == "2":
    total_change = input("How many changes do you want to make? ")
    while not total_change.isdigit():
        total_change = input("Insert number of changes: ")
    total_changes = int(total_change)

    moving_hillclimber = Moving_Hillclimber(total_changes, all_houses, area)
    moving_hillclimber.move_houses()

# The user has chosen the simulated annealing
elif chosen_algorithm == "3":
    changes = input("how many changes per random state do you want to make: ")
    while not changes.isdigit():
        changes = input("Insert number of changes: ")
    changes = int(changes)
    
    simulated_annealing = Simulated_Annealing(changes, all_houses, area)
    simulated_annealing.simulate()




