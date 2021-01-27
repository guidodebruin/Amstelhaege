######################################################################
# - singlehouse.py
# - Singlehouse class, describes the characteristics of the housetype
# 
# - Programeer theorie 2021
# 
# - Manuka Khan, Guido de Bruin, Allan Duah
#
######################################################################

from code.classes.House import House


class Singlehouse(House):
   def __init__(self):
      self.length = 8
      self.width = 8
      self.id = id(self)
      self.freespace = 2
      self.price = 285000
      self.percentage = 3
      self.corner_lowerleft = [0,0]
