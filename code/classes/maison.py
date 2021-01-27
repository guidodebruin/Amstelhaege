"""
    maison.py
    This is the class for the Maison housetype.

    Programmeertheorie 2021
    Manuka Khan, Guido de Bruin, Allan Duah
""" 

from code.classes.House import House

class Maison(House):
    """
        Describes characteristics of a maison.
    """ 
    def __init__(self):
        self.length = 10
        self.width = 12
        self.id = id(self)
        self.freespace = 6
        self.price = 610000
        self.percentage = 6
        self.corner_lowerleft = [0,0]
