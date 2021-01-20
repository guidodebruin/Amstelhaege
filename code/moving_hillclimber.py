import random
import copy

from graph import Graph

class Moving_Hillclimber:

    def __init__(self, changes, houses, area):
        self.changes = changes
        self.houses = houses
        self.area = area

    def move_houses(self):
        current_changes = 0
        best_value = 0
        while current_changes < self.changes:

            given_direction = self.random_direction()
            self.assign_random_direction(given_direction)

            # Obtain the total prices of all households
            total_price = self.area.get_networth(self.houses)

            if best_value < total_price:
                current_changes += 1
                best_value = total_price
                best_state = copy.deepcopy(self.houses)
            else:
                self.area.undo_housemove(given_direction)
                

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

        if random_direction == "up":
            # The y-coordinate goes up by 1
            random_house_coordinates = [random_house.corner_lowerleft[0], random_house.corner_lowerleft[1] + 1]
            

        elif random_direction == "down":
            # The y-coordinate goes down by 1
            random_house_coordinates = [random_house.corner_lowerleft[0], random_house.corner_lowerleft[1] - 1]

        elif random_direction == "left":
            # The x-coordinate goes down by 1
            random_house_coordinates = [random_house.corner_lowerleft[0] - 1, random_house.corner_lowerleft[1]]

        elif random_direction == "right": 
            # The x-coordinate goes up by 1
            random_house_coordinates = [random_house.corner_lowerleft[0] + 1, random_house.corner_lowerleft[1]]

        return random_house_coordinates


    def assign_random_direction(self, random_direction):
        """
            Assigns a new valid place for a house in a certain direction.
        """
        # Get a random house from all houses
        moving_house = self.random_house(self.houses)

        # Change the coordinates of the randomly selected house
        moving_house.corner_lowerleft = self.return_new_coordinates(random_direction, moving_house)

        # Check if the newly assigned coordinates are valid, if not assign new coordinates
        while self.area.invalid(moving_house, self.houses) or self.area.overlap(moving_house, self.houses):
            # random_direction = self.random_direction(moving_house)
            moving_house.corner_lowerleft = self.return_new_coordinates(random_direction, moving_house)

        return moving_house


    # def compare_price(self, all_houses, old_price):

    #     """
    #      Returns random a random direction
    #     """
    #     new_price = get_networth(all_houses)
    #     if new_price > old_price:
    #         return True
        
    #     return False
     
    def undo_housemove(self, random_direction):

        """
         Cancels the adjustment
        """
        if random_direction == "up":
            # The y-coordinate goes down by 1
            random_house_coordinates = [random_house.corner_lowerleft[0], house.corner_lowerleft[1] - 1]

        elif random_direction == "down":
            # The y-coordinate goes up by 1
            random_house_coordinates = [random_house.corner_lowerleft[0], house.corner_lowerleft[1] + 1]

        elif random_direction == "left":
            # The x-coordinate goes up by 1
            random_house_coordinates = [random_house.corner_lowerleft[0] + 1, house.corner_lowerleft[1]]

        elif random_direction == "right":
            # The x-coordinate goes down by 1
            random_house_coordinates = [random_house.corner_lowerleft[0] - 1, house.corner_lowerleft[1]]

        # Change the coordinates of the randomly selected house
        moving_house.corner_lowerleft = random_house_coordinates

        return moving_house
        



    
