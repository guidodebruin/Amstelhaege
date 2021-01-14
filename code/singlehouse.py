from House import House

class Singlehouse(House):
   def __init__(self):
      #   def __init__(self, length, width, type, id, free, price, latitude, longitude):
      self.length = 8
      self.width = 8
      self.id = id
      self.free = 2
      self.price = 285000
      self.corner_1 = [40,121]
      self.corner_2 = self.return_corner2()
      self.corner_3 = [32,129]
      self.corner_4 = [40,129]

   def return_corner1(self):
      coordinates = self.corner_2
      y_coordinate = coordinates[1]
      new_y_coordinate = y_coordinate + 8
      corner_2[1] = new_y_coordinate
      return corner_2

