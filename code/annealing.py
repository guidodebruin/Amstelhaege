import random
import copy
import math

from graph import Graph
from moving_hillclimber import Moving_Hillclimber


class Simulated_Annealing(Moving_Hillclimber):

    def __init__(self, loops, changes, houses, area):
        self.loops = loops
        self.changes = changes
        self.houses = houses
        self.area = area


    def simulate(self):
        """
            Repeatedly generates random states.
            Tries to find to most optimal house coordinates in each random state.
        """
        best_value = 0

        # Simulated Annealing Parameters
        temp = 90
        final_temp = 0.1    
        alpha = 0.01

        # create a random state
        current_state = self.area.randomly_assign_houses(self.houses)
        solution = copy.deepcopy(self.houses)

        while temp > final_temp:
            # loop n x door het aantal veranderingen dat je per state wil aanbrengen
            for loop in range(self.loops):

                # move a random house in this state
                for change in range(self.changes):
                    
                    given_direction = self.random_direction()
                    moving_house = self.random_house(self.houses)
                    self.assign_random_direction(given_direction, moving_house)

                # check if the total price is better or worse than current state price
                new_totalprice = self.area.get_networth(self.houses)
                
                # calculate its final price
                current_totalprice = self.area.get_networth(solution)

                # if better -> keep this state
                if current_totalprice < new_totalprice:
                    current_totalprice = new_totalprice
                    local_best_state = copy.deepcopy(self.houses)
                # if worse -> check if this state can be accepted
                else:
                    # use the simulated annealing formula
                    # if random.uniform(0, 1) < math.exp(cost_diff / current_temp):
                    pass

                # if worse -> check if state can be accepted with formula
                    # accepted -> repeat process
                    # not accepted -> go back to last state and repeat process

                # find best position of houses in this random state
                    # if better than other random states -> deepcopy

                # get new random state and repeat process