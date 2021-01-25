import random
import math
import copy
import matplotlib.pyplot as plt

from code.classes.graph import Graph
from code.algorithms.moving_hillclimber import Moving_Hillclimber


class Simulated_Annealing(Moving_Hillclimber):

    def __init__(self, changes, houses, area):
        self.changes = changes
        self.houses = houses
        self.area = area


    def simulate(self):
        """
            Generates a random state.
            Tries to find to most optimal house coordinates in this random state.
        """

        # Simulated Annealing Parameters
        temp = 1
        final_temp = 0.1    
        alpha = 0.99

        # save the final prices to plot
        y_axes = []

        # create a random state
        current_state = self.area.randomly_assign_houses(self.houses)

        # temporary best state
        solution = {}
        for house in self.houses:
            solution[house.id] = house.corner_lowerleft

        # calculate the total price of the current solution
        solution_totalprice = self.area.get_networth(self.houses)

        while temp > final_temp:

            for change in range(self.changes):
                # make n changes to the positions of random houses
                given_direction = self.random_direction()
                moving_house = self.random_house(self.houses)
                self.assign_random_direction(given_direction, moving_house)

            # calculate the new final house prices
            self.area.houseprices(self.houses)
            new_totalprice = self.area.get_networth(self.houses)

            # calculate the cost difference
            cost_diff = new_totalprice - solution_totalprice

            # keep new state if better than current solution
            if solution_totalprice < new_totalprice:
                solution_totalprice = new_totalprice
                solution = {}
                for house in self.houses:
                    solution[house.id] = house.corner_lowerleft
            elif random.uniform(0, 1) < math.exp(cost_diff / temp):
                print("gelukt")
                solution_totalprice = new_totalprice
                solution = {}
                for house in self.houses:
                    solution[house.id] = house.corner_lowerleft  
            # state cannot be accepted
            else:
                new_totalprice = solution_totalprice
                for key in solution:
                    for house in self.houses:
                        if key == house.id:
                            house.corner_lowerleft = solution[key]

            # change the temp
            temp *= alpha

            # reset the house prices
            self.area.price_reset(self.houses)

            # plot the total price of the solutions
            y_axes.append(solution_totalprice)
            plt.subplot(131)
            plt.plot(y_axes)
            plt.savefig('plots/simulated_annealing.png')

        # final outcome
        for key in solution:
            for house in self.houses:
                if key == house.id:
                    house.corner_lowerleft = solution[key]

        # calculate final houseprice
        self.area.houseprices(self.houses)

        # get final houseprice
        final_networth = self.area.get_networth(self.houses)
        
        self.area.load_houses(self.houses)
        self.area.write_output(self.houses)
        print(solution_totalprice)