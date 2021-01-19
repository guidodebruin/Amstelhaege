import random
from graph import Graph

class Hillclimber():

    def random_house(self, houses):
    """
        Randomly returns a house object
    """
        random_house = random.choice(houses)
        # moet random hiervoor import worden?
        return random_house
    
    
    def random_direction(self, random_house):
    """
         Returns random a random direction
    """
        directions = ["up", "down", "left", "right"]

        random_direction = random.choice(direction)

        if random_direction == "up":
            # The y-coordinate goes up by 1
            random_house_coordinates = random_house.corner_lowerleft[random_house.corner_lowerleft[0], house.corner_lowerleft[1] + 1]
        elif random_direction == "down":
            # The y-coordinate goes down by 1
            random_house_coordinates = random_house.corner_lowerleft[random_house.corner_lowerleft[0], house.corner_lowerleft[1] - 1]
        elif random_direction == "left":
            # The x-coordinate goes down by 1
            random_house_coordinates = random_house.corner_lowerleft[random_house.corner_lowerleft[0] - 1, house.corner_lowerleft[1]]
        else random_direction == "right": 
            # The x-coordinate goes up by 1
            random_house_coordinates = random_house.corner_lowerleft[random_house.corner_lowerleft[0] + 1, house.corner_lowerleft[1]]

        return random_house_coordinates


    def assign_random_direction(self, all_houses):
        """
            Assigns a new valid place for a house in a certain direction.
        """
        # get a random house from all houses
        moving_house = self.random_house(all_houses)

        # change the coordinates of the randomly selected house
        moving_house.corner_lowerleft = moving_house.random_direction(moving_house, all_houses)

        # check if the newly assigned coordinates are valid, if not assign new coordinates
        while self.invalid(moving_house, all_houses) or self.overlap(moving_house, all_houses):
            moving_house.corner_lowerleft = moving_house.random_direction()

        return moving_house


    def price_comparison(self, new_price, old_price):

    """
         Returns random a random direction
    """

        if new_price > old_price:
            return True
        
        return False
     
    def undo_housemove(self):
        
        pass



    
