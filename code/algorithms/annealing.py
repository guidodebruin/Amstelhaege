"""
    annealing.py
    Contains the simulated annealing algorithm

    Programmeertheorie 2021
    Manuka Khan, Guido de Bruin, Allan Duah
""" 

import random
import math
import copy

from code.classes.graph import Graph
from code.algorithms.moving_hillclimber import Moving_Hillclimber


class Simulated_Annealing(Moving_Hillclimber):
    """
        The simulated annealing algorithm works by first using
        the random algorithm to get the best random state.
        Then changes are made to this state.
        If the changes give the graph a higher value the changes are kept.
        if the changes do not give the graph a higer value,
        an acceptance rate is used to check if the changes can lead to a new optimum.
        The algorithm stops when the temperature is below the minimum temperature.
    """

    def __init__(self, changes, best_randomstate, area):
        self.changes = changes
        self.houses = best_randomstate
        self.area = area


    def simulate(self):
        """
            Tries to find to most optimal house coordinates in this random state.
        """
        # simulated annealing parameters
        temp = 100000
        final_temp = 0.1    
        alpha = 0.99

        solution = copy.deepcopy(self.houses)
        solution_totalprice = self.area.get_networth(self.houses)

        while temp > final_temp:

            for change in range(self.changes):
                    
                # make n changes to the positions of random houses
                given_direction = self.random_direction()
                moving_house = random.choice(self.houses)
                self.assign_random_direction(given_direction, moving_house)

            # calculate the new final house prices
            self.area.price_reset(self.houses)
            self.area.houseprices(self.houses)
            new_totalprice = self.area.get_networth(self.houses)
                
            # calculate the total price of the current solution
            self.area.price_reset(solution)
            self.area.houseprices(solution)
            solution_totalprice = self.area.get_networth(solution)

            # calculate the cost difference
            cost_diff = new_totalprice - solution_totalprice

            # if better keep this state
            if solution_totalprice < new_totalprice:
                solution_totalprice = new_totalprice
                solution = copy.deepcopy(self.houses)
            # if worse check if this state can be accepted
            elif random.uniform(0, 1) < math.exp(cost_diff / temp):
                solution_totalprice = new_totalprice
                solution = copy.deepcopy(self.houses)
            # if state cannot be accepted
            else:
                self.houses = solution

            # change the temp
            temp *= alpha
        
        self.area.load_houses(solution)
        self.area.write_output(solution, "annealing")