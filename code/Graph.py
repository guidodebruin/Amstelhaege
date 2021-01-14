import csv
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from shapely.geometry import box

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
            rect = patches.Rectangle((data[1][0], data[1][1]),(data[2][0]-data[1][0]),(data[2][1]-data[1][1]),facecolor='b')
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
                rect = patches.Rectangle((house.corner_lowerleft[0], house.corner_lowerleft[1]),house.width, house.length,facecolor='r')
                self.houses.append(house)
                # self.houses.append(rect)
                
                # Add the patch to the Axes
                ax.add_patch(rect)

            # Save the graph
            plt.savefig('../plots/init_graph.png')

    def overlap(self, houses):

        overlap = []
        water_boxes = []
        for data in self.water:
            water_box = box(data[1][0], data[1][1], data[2][0], data[2][1])
            water_boxes.append(water_box)

        # UITEINDELIJK DIT MET DE 4 CORNERS IPV LOWERLEFT PLUS WIDTH IS VEEL NETTER EN MOOIER
        for house in houses:
            box1 = box(house.corner_lowerleft[0], house.corner_lowerleft[1], (house.corner_lowerleft[0]+house.width), (house.corner_lowerleft[1]+house.length))
            for house2 in houses:
                box2 = box(house2.corner_lowerleft[0], house2.corner_lowerleft[1], (house2.corner_lowerleft[0]+house2.width), (house2.corner_lowerleft[1]+house2.length))
                # IPV .CRONER_LOWERLEFT MET IDS OF STRUCTURE WERKEN OM ZEKER TE WETEN WELK HUIS
                if house.corner_lowerleft is not house2.corner_lowerleft and box1.intersects(box2) and house not in overlap:
                    overlap.append(house)
            for water_box in water_boxes:
                if box1.intersects(water_box) and house not in overlap:
                    overlap.append(house)
                
        return overlap

    def all_houses_set(self):
        pass

    def move_house(self):
        pass

    def delete_house(self):
        pass

    def swap_house(self):
        pass


