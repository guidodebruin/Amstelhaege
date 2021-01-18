from House import House

class Maison(House):
    
    def __init__(self):
        self.length = 10
        self.width = 12
        self.id = id
        self.freespace = 6
        self.price = 610000
        self.percentage = 0.06
        self.corner_lowerleft = self.return_lowerleft()
