from House import House

class Bungalow(House):
    
    def __init__(self):
        self.length = 7
        self.width = 11
        self.id = id
        self.free = 3
        self.price = 399000
        # self.corner_1 = [0,0]
        self.corner_lowerleft = self.return_corner2()
        # self.corner_3 = [0,0]
        # self.corner_4 = [0,0]      
    