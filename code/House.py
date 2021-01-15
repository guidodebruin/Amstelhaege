import random

class House():
   
   def calc_freespace(self):
      pass
 
   def calc_price(self):
      pass

   def return_corner2(self): 
      """
         Returns random coordinates
      """
      return [random.randint(0, 160), random.randint(0,180)]

   def return_upperleft(self, house):
      corner_upperleft = [house.corner_lowerleft[0], house.corner_lowerleft[1] + house.length]
      return corner_upperleft
   
   def return_upperright(self, house):
      corner_upperright = [house.corner_lowerleft[0] + house.width, house.corner_lowerleft[1] + house.length]
      return corner_upperright
   
      
   def return_lowerright(self, house):
      corner_lowerright = [house.corner_lowerleft[0] + house.width, house.corner_lowerleft[1]]
      return corner_lowerright