from code.classes.House import House


class Singlehouse(House):
   """
            Describes characteristics of a singlehouse.
   """ 
   def __init__(self):
      self.length = 8
      self.width = 8
      self.id = id(self)
      self.freespace = 2
      self.price = 285000
      self.percentage = 3
      self.corner_lowerleft = [0,0]
