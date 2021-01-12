import csv
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

class Graph():
    def __init__(self, area):
        """
            Necessities for the visual representation
        """
        self.water = []
        self.width = 180
        self.depth = 160
        self.houses = []

        # Load the water data
        self.load_water(f"../Areas/{area}.csv")

        # Create area graph
        self.load_graph()

    def load_water(self, filename):
        """
            Load the water that belongs to a specific neighborhood
        """

        # Read the file that contains the water data
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

    def load_graph(self):
        """
            Call up the map for the specific area
        """
        plt.xlabel("width")
        plt.ylabel("depth")
        plt.axis([0, self.width, 0, self.depth])
        
        # Display the neighborhood as green
        ax = plt.gca()
        ax.set_facecolor("green")
        
        for data in self.water:
            # Create a Rectangle patch in which water is displayed as blue
            rect = patches.Rectangle((data[1][0], data[1][1]),data[2][1],data[2][0],facecolor='b')
            
            # Add the patch to the Axes
            ax.add_patch(rect)

        # Save the graph
        plt.savefig('../plots/init_graph.png')
        
    def load_houses(self, houses):
            """
                Locate houses on the map
            """
            ax = plt.gca()

            for house in houses:
                rect = patches.Rectangle((house.corner_2[0], house.corner_2[1]),house.width, house.length,facecolor='r')
                
                # Add the patch to the Axes
                ax.add_patch(rect)

            # Save the graph
            plt.savefig('../plots/init_graph.png')

    def all_houses_set(self):
        pass

    def add_house(self):
        pass

    def move_house(self):
        pass

    def delete_house(self):
        pass

    def swap_house(self):
        pass


