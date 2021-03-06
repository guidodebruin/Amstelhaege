"""
    - main.py
    - main.py is used to run the algorithms
    - Programeer theorie 2021
    - Manuka Khan, Guido de Bruin, Allan Duah
"""
import sys

from code.classes.singlehouse import Singlehouse
from code.classes.bungalow import Bungalow
from code.classes.maison import Maison
from code.classes.graph import Graph

from code.algorithms.random import Random
from code.algorithms.moving_hillclimber import Moving_Hillclimber
from code.algorithms.annealing import Simulated_Annealing


# request user for area number and number of houses
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
    area = Graph(sys.argv[1])

# create house objects
all_houses = area.save_houses(int(sys.argv[2]))

print("Choose the algorithm with which you want to perform the calculation")
print("Algorithmes available: Random = 1, Hill Climber = 2, Simulated Annealing = 3")
chosen_algorithm = input("Please choose your algorithm by entering the corresponding number: ")

while chosen_algorithm not in ["1", "2", "3"]:
    print("Algorithmes available: Random = 1, Hill Climber = 2, Simulated Annealing = 3")
    chosen_algorithm = input("Please choose your algorithm by entering the corresponding number: ")


# the user has chosen the random algorithm
if chosen_algorithm == "1":
    loop = input("How many random states do you want to generate: ")
    while not loop.isdigit():
       loop = input("Insert number of runs: ")

    random = Random(int(loop), all_houses, area)
    best_randomstate = random.looper()
    algorithm_type = "random"
    random.load_and_write_output(best_randomstate, algorithm_type)


# the user has chosen the moving hill climber
elif chosen_algorithm == "2":
    # ask for random state number
    loop = input("How many random states do you want to generate: ")
    while not loop.isdigit():
       loop = input("Insert number of runs: ")
    total_change = input("How many changes do you want to make? ")
    # ask for number of changes to make on the best random state
    while not total_change.isdigit():
        total_change = input("Insert number of changes: ")

    # get a best random state
    random = Random(int(loop), all_houses, area)
    best_randomstate = random.looper()

    # move houses in best random state
    moving_hillclimber = Moving_Hillclimber(int(total_change), best_randomstate, area)
    moving_hillclimber.move_houses()


# the user has chosen the simulated annealing
elif chosen_algorithm == "3":
    # ask for random state number
    loop = input("How many random states do you want to generate: ")
    while not loop.isdigit():
       loop = input("Insert number of runs: ")
    # ask for number of changes
    changes = input("how many changes per random state do you want to make: ")
    while not changes.isdigit():
        changes = input("Insert number of changes: ")

    # get a best random state
    random = Random(int(loop), all_houses, area)
    best_randomstate = random.looper()
    
    # use the best random state for the simulated annealing
    simulated_annealing = Simulated_Annealing(int(changes), best_randomstate, area)
    simulated_annealing.simulate()