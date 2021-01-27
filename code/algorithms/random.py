import copy
import matplotlib.pyplot as plt

from code.classes.graph import Graph

class Random:
    """
        The random algorithm create random states in a loop of X times.
        For every iteration the final networth is calculated.
        If a new final networth is better than te last one,
        the new one is saved as best state.
    """
    
    def __init__(self, loops, houses, area):
        self.loops = loops
        self.houses = houses
        self.area = area
        coordinates = []


    def looper(self):
        """
            In a loop of n times, decided by the number of loops, random states will be generated.
            The best state is saved and returned.
        """
        best_value = 0
        best_state = {}

        for loop in range(self.loops):
            # randomly assign the invalid placed houses until a valid state is reached
            self.area.randomly_assign_houses(self.houses)

            # calculate the value of each house
            self.area.houseprices(self.houses)

            # get total price
            final_networth = self.area.get_networth(self.houses)

            # check if the final networth is better than the current best value
            if best_value < final_networth:
                best_value = final_networth
                best_state = {}
                for house in self.houses:
                    best_state[house.id] = house.corner_lowerleft

            # reset the graph
            self.area.area_reset(self.houses)
            self.area.price_reset(self.houses)

        # reset the coordinates to their best state
        self.final_outcome(best_state)
        return(self.houses)


    def final_outcome(self, best_state):
        """
           Reset the best state coordinates to each house.
           This is returned as final outcome.
        """
        for key in best_state:
            for house in self.houses:
                if key == house.id:
                    house.corner_lowerleft = best_state[key]

        # calculate final houseprice
        self.area.houseprices(self.houses)


    def load_and_write_output(self, houses, algorithm_type):
        """
            Loads houses into the graph.
            Writes the final output for the best random state.
        """
        self.area.load_houses(houses)
        self.area.write_output(houses, algorithm_type)