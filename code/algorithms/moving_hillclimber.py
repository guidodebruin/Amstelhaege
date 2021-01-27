######################################################################
# - moving_hillcimber.py
# - Contains the hill climber algorithm
# 
# - Programeer theorie 2021
# 
# - Manuka Khan, Guido de Bruin, Allan Duah
#
######################################################################

import random
import copy
import math
import matplotlib.pyplot as plt

from code.classes.graph import Graph


class Moving_Hillclimber:

    def __init__(self, changes, best_randomstate, area):
        self.changes = changes
        self.houses = best_randomstate
        self.area = area


    def move_houses(self):
        """
            Moves house to a different place and then calculates the new finalprice of the map.
        """ 
        current_changes = 0

        best_state = {}
        for house in self.houses:
            best_state[house.id] = house.corner_lowerleft

        # calculate total value per house
        self.area.houseprices(self.houses) 

        # calculate total value of the graph
        best_value = self.area.get_networth(self.houses)

        while current_changes < self.changes:

            # find house with the least freespace
            # moving_house = self.return_smallest_freespace(self.houses)

            # return a random direction and a random house
            given_direction = self.random_direction()
            moving_house = self.random_house(self.houses)

            # assign this house to the given direction
            self.assign_random_direction(given_direction, moving_house)

            # reset the houses prices to their original price before calculating their new price increase
            self.area.price_reset(self.houses)

            # calculate final houseprices and total graph value
            self.area.houseprices(self.houses)
            total_price = self.area.get_networth(self.houses)

            if total_price > best_value:
                best_value = total_price
                solution = {}
                for house in self.houses:
                    solution[house.id] = house.corner_lowerleft
                current_changes += 1
            else:
                moving_house.corner_lowerleft = self.undo_housemove(given_direction, moving_house)

        # reset the houses prices to their original price before calculating their new price increase
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

        self.area.load_houses(self.houses)
        self.area.write_output(self.houses)
                

    def random_house(self, houses):
        """
        Randomly returns a house object
        """
        random_house = random.choice(houses)
        return random_house
      

    def random_direction(self):
        """
         Returns random coordinates for a random direction
        """
        direction = ["up", "down", "left", "right"]

        random_direction = random.choice(direction)

        return random_direction


    def return_new_coordinates(self, random_direction, random_house):
        """
         Returns the new coordinates for the picked direction
        """
        if random_direction == "up":
            # the y-coordinate goes up by 1
            random_house_coordinates = [random_house.corner_lowerleft[0], random_house.corner_lowerleft[1] + 2]    

        elif random_direction == "down":
            # the y-coordinate goes down by 1
            random_house_coordinates = [random_house.corner_lowerleft[0], random_house.corner_lowerleft[1] - 2]

        elif random_direction == "left":
            # the x-coordinate goes down by 1
            random_house_coordinates = [random_house.corner_lowerleft[0] - 2, random_house.corner_lowerleft[1]]

        elif random_direction == "right": 
            # the x-coordinate goes up by 1
            random_house_coordinates = [random_house.corner_lowerleft[0] + 2, random_house.corner_lowerleft[1]]

        return random_house_coordinates


    def assign_random_direction(self, random_direction, moving_house):
        """
            Assigns a new valid place for a house in a certain direction.
        """
        # change the coordinates of the randomly selected house
        moving_house.corner_lowerleft = self.return_new_coordinates(random_direction, moving_house)

        # check if the newly assigned coordinates are valid, if not assign new coordinates
        if self.area.invalid(moving_house, self.houses) or self.area.overlap(moving_house, self.houses):
            # return house to original position
            moving_house.corner_lowerleft = self.undo_housemove(random_direction, moving_house)

        return moving_house
     

    def undo_housemove(self, random_direction, random_house):
        """
         Cancels the adjustment
        """
        if random_direction == "up":
            # the y-coordinate goes down by 1
            random_house_coordinates = [random_house.corner_lowerleft[0], random_house.corner_lowerleft[1] - 2]

        elif random_direction == "down":
            # the y-coordinate goes up by 1
            random_house_coordinates = [random_house.corner_lowerleft[0], random_house.corner_lowerleft[1] + 2]

        elif random_direction == "left":
            # the x-coordinate goes up by 1
            random_house_coordinates = [random_house.corner_lowerleft[0] + 2, random_house.corner_lowerleft[1]]

        elif random_direction == "right":
            # the x-coordinate goes down by 1
            random_house_coordinates = [random_house.corner_lowerleft[0] - 2, random_house.corner_lowerleft[1]]

        return random_house_coordinates

    def return_smallest_freespace(self):

        """
         Returns the house object with the smallest freespace
        """

        for house in self.houses:
            freespace = self.area.closest_house(house, self.houses)[1]
        

            