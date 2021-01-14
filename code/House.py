import random

class House():
    def __init__(self):
       #   def __init__(self, length, width, type, id, free, price, latitude, longitude):
       self.length = 8
       self.width = 8
       self.id = id
       self.free = 2
       self.price = 285000
    #    self.corner_1 = [40,121]
       self.corner_lowerleft = self.return_corner2()
    #    self.corner_3 = [32,129]
    #    self.corner_4 = [40,129]
       
 
    def __str__(self):
       return self.id
 
    def move_house(self):
       pass
 
    def delete_house(self):
       pass
 
    def add_house(self):
       pass
 
    def calc_freespace(self):
       pass
 
    def calc_price(self):
       pass

    def return_corner2(self): 
        # Get random coordinate for the width       
        x_coordinate = random.randint(0, 180)

        # Get random coordinate for the depth
        y_coordinate = random.randint(0, 160)

        corner_2 = []
        corner_2.append(x_coordinate)
        corner_2.append(y_coordinate)

        return corner_2