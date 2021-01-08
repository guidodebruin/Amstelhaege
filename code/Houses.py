class HouseType():
 
   def __init__(self, length, width, type, id, free, price, latitude, longitude):
       self.length = length
       self.width = width
       self.id = id
       self.free = free
       self.price = price
       self.lat = latitude
       self.long = longitude
 
   def __str__(self):
       return self.id
 
   def move(self):
       pass
 
   def delete(self):
       pass
 
   def add(self):
       pass
 
   def free(self):
       pass
 
   def calcprice(self):
       pass