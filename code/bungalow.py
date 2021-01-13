import random

class Bungalow():

   def __init__(self):
       self.length = 7
       self.width = 11
       self.id = id
       self.free = 3
       self.price = 399000
       self.corner_1 = [0,0]
       self.corner_2 = self.return_corner2()
       self.corner_3 = [0,0]
       self.corner_4 = [0,0]      
 
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