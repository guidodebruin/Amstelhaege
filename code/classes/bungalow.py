######################################################################
# - bungalow.py
# - Bungalow class, describes the characteristics of the housetype
# 
# - Programeer theorie 2021
# 
# - Manuka Khan, Guido de Bruin, Allan Duah
#
######################################################################

from code.classes.House import House

class Bungalow(House):
    """
            Describes characteristics of a bungalow.
    """    
    def __init__(self):
        self.length = 7
        self.width = 11
        self.id = id(self) 
        self.freespace = 3
        self.price = 399000
        self.percentage = 4
        self.corner_lowerleft = [0,0]   
    