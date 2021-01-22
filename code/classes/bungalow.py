from code.classes.House import House

class Bungalow(House):
    
    def __init__(self):
        self.length = 7
        self.width = 11
        self.id = id(self) 
        self.freespace = 3
        self.price = 399000
        self.percentage = 0.04
        self.corner_lowerleft = [0,0]   
    