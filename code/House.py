import random

class House():

   def return_lowerleft(self): 
      """
         Returns random coordinates
      """
      return [random.randint(0, 160), random.randint(0,180)]


   def return_upperleft(self, house):
      """
         Returns coordinates for the upperleft corner based on coordinates of the lowerleft corner
      """
      corner_upperleft = [house.corner_lowerleft[0], house.corner_lowerleft[1] + house.length]
      return corner_upperleft
   

   def return_upperright(self, house):
      """
         Returns coordinates for the upperright corner based on coordinates of the lowerleft corner
      """
      corner_upperright = [house.corner_lowerleft[0] + house.width, house.corner_lowerleft[1] + house.length]
      return corner_upperright
   
      
   def return_lowerright(self, house):
      """
         Returns coordinates for the lowerright corner based on coordinates of the lowerleft corner
      """
      corner_lowerright = [house.corner_lowerleft[0] + house.width, house.corner_lowerleft[1]]
      return corner_lowerright