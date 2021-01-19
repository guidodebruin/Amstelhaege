import random
from graph import Graph

class Hillclimber():

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
        directions = ["up", "down", "left", "right"]

        random_direction = random.choice(direction)

        return random_direction

    def return_new_coordinates(self, random_direction):

        if random_direction == "up":
            # The y-coordinate goes up by 1
            random_house_coordinates = random_house.corner_lowerleft[random_house.corner_lowerleft[0], house.corner_lowerleft[1] + 1]

        elif random_direction == "down":
            # The y-coordinate goes down by 1
            random_house_coordinates = random_house.corner_lowerleft[random_house.corner_lowerleft[0], house.corner_lowerleft[1] - 1]

        elif random_direction == "left":
            # The x-coordinate goes down by 1
            random_house_coordinates = random_house.corner_lowerleft[random_house.corner_lowerleft[0] - 1, house.corner_lowerleft[1]]

        elif random_direction == "right": 
            # The x-coordinate goes up by 1
            random_house_coordinates = random_house.corner_lowerleft[random_house.corner_lowerleft[0] + 1, house.corner_lowerleft[1]]

        return random_house_coordinates


    def assign_random_direction(self, all_houses, random_direction):
        """
            Assigns a new valid place for a house in a certain direction.
        """
        # Get a random house from all houses
        moving_house = self.random_house(all_houses)

        # Change the coordinates of the randomly selected house
        moving_house.corner_lowerleft = moving_house.return_new_coordinates(random_direction)

        # Check if the newly assigned coordinates are valid, if not assign new coordinates
        while self.invalid(moving_house, all_houses) or self.overlap(moving_house, all_houses):
            random_direction = moving_house.random_direction(moving_house)
            moving_house.corner_lowerleft = moving_house.return_new_coordinates(random_direction)

        return moving_house


    def compare_price(self, all_houses, old_price):

        """
         Returns random a random direction
        """
        new_price = get_networth(all_houses)
        if new_price > old_price:
            return True
        
        return False
     
    def undo_housemove(self, random_direction):

        """
         Cancels the adjustment
        """
        if random_direction == "up":
            # The y-coordinate goes down by 1
            random_house_coordinates = random_house.corner_lowerleft[random_house.corner_lowerleft[0], house.corner_lowerleft[1] - 1]

        elif random_direction == "down":
            # The y-coordinate goes up by 1
            random_house_coordinates = random_house.corner_lowerleft[random_house.corner_lowerleft[0], house.corner_lowerleft[1] + 1]

        elif random_direction == "left":
            # The x-coordinate goes up by 1
            random_house_coordinates = random_house.corner_lowerleft[random_house.corner_lowerleft[0] + 1, house.corner_lowerleft[1]]

        elif random_direction == "right":
            # The x-coordinate goes down by 1
            random_house_coordinates = random_house.corner_lowerleft[random_house.corner_lowerleft[0] - 1, house.corner_lowerleft[1]]

        # Change the coordinates of the randomly selected house
        moving_house.corner_lowerleft = random_house_coordinates

        return moving_house
        



    
