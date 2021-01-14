from House import House

class Maison(House):
    
    def __init__(self):
        self.length = 10
        self.width = 12
        self.id = id
        self.free = 6
        self.price = 610000
        # self.corner_1 = [75,105]
        self.corner_lowerleft = self.return_corner2()
        # self.corner_3 = [83,97]
        # self.corner_4 = [83,105]
