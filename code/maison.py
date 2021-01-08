class Maison():
 
   def __init__(self, length, width, type, id, free, price, latitude, longitude):
       self.length = 10
       self.width = 12
       self.id = id
       self.free = 6
       self.price = 610000
       self.lat = latitude
       self.long = longitude
 
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