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
        Moves houses in a random direction and then calculates the new final price of the map.
        """ 
        current_changes = 0

        # randomly assign the invalid placed houses until a valid state is reached
        # self.area.randomly_assign_houses(self.houses)

        best_state = {}
        for house in self.houses:
            best_state[house.id] = house.corner_lowerleft
 
        # calculate total value of the graph
        best_value = self.area.get_networth(self.houses)


        while current_changes < self.changes:

            # find house with the least freespace
            moving_house = self.return_smallest_freespace()

            # return a random direction and a random house
            given_direction = self.random_direction()
            
            # get a random house from all houses
            # moving_house = random.choice(self.houses)

            # assign this house to the given direction
            self.assign_random_direction(given_direction, moving_house)

            # reset the house prices to their original price before calculating their new price increase
            self.area.price_reset(self.houses)

            # calculate final houseprices and total graph value
            self.area.houseprices(self.houses)

            total_price = self.area.get_networth(self.houses)

            if total_price > best_value:
                best_value = total_price
                solution = {}
                current_changes += 1
                for house in self.houses:
                    solution[house.id] = house.corner_lowerleft
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
      

    def random_direction(self):
        """
         Returns random coordinates for a random direction.
        """
        direction = ["up", "down", "left", "right"]

        return random.choice(direction)


    def return_new_coordinates(self, random_direction, random_house):
        """
         Returns the new coordinates for the picked direction.
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
         Cancels the adjustment.
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
         Returns the house object with the smallest freespace.
        """

        smallest_freespace = 180
        for house in self.houses:
            freespace = self.area.closest_house(house, self.houses)[1]
            if freespace < smallest_freespace and self.check_moveability(house):
                smallest_freespace = freespace
                house_smallest_freespace = house

        return house_smallest_freespace


    def check_moveability(self, house):
        """
            Checks if a house can be moved in at least one direction.
        """
        directions = ["up", "down", "left", "right"]

        for direction in directions:
            house.corner_lowerleft = self.return_new_coordinates(direction,house)
            # check if a house can be moved
            if self.area.invalid(house, self.houses) == False and self.area.overlap(house, self.houses) == False:
                house.corner_lowerleft = self.undo_housemove(direction, house)
                return True
            house.corner_lowerleft = self.undo_housemove(direction, house)

        # house cannot be moved
        return False
