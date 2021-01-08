import csv
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

class Plattegrond():
    def __init__(self, wijk):
        """
            Maakt de plattegrond
        """
        self.water = []
        self.breedte = 180
        self.diepte = 160
        self.houses = []

        # laad water in
        self.load_water(f"../wijken/{wijk}.csv")
        print(self.water)

        # roep plattegrond aan
        self.load_plattegrond()


    def load_water(self, filename):
        """
            Laadt het water dat bij een specifieke wijk hoort
        """
        with open(filename, "r") as csv_file:
            next(csv_file)
            reader = csv.reader(csv_file)

            for counter, row in enumerate(reader):
                self.water.append([])
                for elem in row:
                    if elem[0].isnumeric():
                        coords = list(map(float,elem.split(','))) 
                        self.water[counter].append(coords)
                    else:
                        self.water[counter].append(elem)

            csv_file.close()

    def load_plattegrond(self):
        """
            Roept de plattegrond voor een wijk aan
        """
        plt.xlabel("breedte")
        plt.ylabel("diepte")
        plt.axis([0, self.breedte, 0, self.diepte])
        
        # maak wijk groen
        ax = plt.gca()
        ax.set_facecolor("green")
        
        for data in self.water:
            # Create a Rectangle patch
            rect = patches.Rectangle((data[1][0], data[1][1]),data[2][1],data[2][0],facecolor='b')
            # Add the patch to the Axes
            ax.add_patch(rect)

        plt.savefig('../plots/init_plattegrond.png')
        
        def load_houses(self):
            pass

