from graph import Graph

class hillclimber():

    def random_house(self, houses):
      """
         Returns random a random house object
      """
        random_house = random.choice(houses)
        return random_house
    
    
    def random_direction(self, moving_house, all_houses):
      """
         Returns random a random direction
      """
        directions = ["up", "down", "left", "right"]
        random_house = moving_house

        random_direction = random.choice(direction)
        if random_direction = "up":
                
            # The y-coordinate goes up by 1
            random_house.corner_lowerleft = random_house.corner_lowerleft[random_house.corner_lowerleft[0], house.corner_lowerleft[1] + 1]

        elif random_direction = "down":
                
            # The y-coordinate goes down by 1
            random_house.corner_lowerleft = random_house.corner_lowerleft[random_house.corner_lowerleft[0], house.corner_lowerleft[1] - 1]

        elif random_direction = "left":
                
            # The x-coordinate goes down by 1
            random_house.corner_lowerleft = random_house.corner_lowerleft[random_house.corner_lowerleft[0] - 1, house.corner_lowerleft[1]]

        else random_direction = "left":
                
            # The x-coordinate goes up by 1
            random_house.corner_lowerleft = random_house.corner_lowerleft[random_house.corner_lowerleft[0] + 1, house.corner_lowerleft[1]]

        return random_house


    def assign_random_direction(self, moving_house, all_houses):
    """
         
    """
        moving_house.corner_lowerleft = moving_house.random_direction()
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
     



    