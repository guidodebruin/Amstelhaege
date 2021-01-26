from code.classes.House import House


class Maison(House):
    
    def __init__(self):
        self.length = 10
        self.width = 12
        self.id = id(self)
        self.freespace = 6
        self.price = 610000
        self.percentage = 6
        self.corner_lowerleft = [0,0]
