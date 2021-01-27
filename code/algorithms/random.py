######################################################################
# - random.py
# - Contains the random algorithm
# 
# - Programeer theorie 2021
# 
# - Manuka Khan, Guido de Bruin, Allan Duah
#
######################################################################

import copy
import matplotlib.pyplot as plt
# import pickle

from code.classes.graph import Graph

class Random:

    def __init__(self, loops, houses, area):
        self.loops = loops
        self.houses = houses
        self.area = area
        coordinates = []


    def looper(self):
        """
            In a loop of n times, decided by the number of loops, random states will be generated.
        """
        best_value = 0
        best_state = {}

        for loop in range(self.loops):
            # randomly assign the invalid placed houses until a valid state is reached
            self.area.randomly_assign_houses(self.houses)

            # calculate final houseprice
            self.area.houseprices(self.houses)

            # get final houseprice
            final_networth = self.area.get_networth(self.houses)

            if best_value < final_networth:
                best_value = final_networth
                best_state = {}
                for house in self.houses:
                    best_state[house.id] = house.corner_lowerleft

            # reset the graph
            self.area.area_reset(self.houses)
            self.area.price_reset(self.houses)

        # final outcome
        for key in best_state:
            for house in self.houses:
                if key == house.id:
                    house.corner_lowerleft = best_state[key]

        # calculate final houseprice
        self.area.houseprices(self.houses)

        # get final houseprice
        final_networth = self.area.get_networth(self.houses)
        print(final_networth)

        self.area.load_houses(self.houses)
        self.area.write_output(self.houses)