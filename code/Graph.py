import csv
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from shapely.geometry import box, Point

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
                # Add the patch to the Axes
                ax.add_patch(rect)

            # Save the graph
            plt.savefig('../plots/init_graph.png')


    def overlap(self, houses):
        """
            Checks for overlapping houses with each other, water or the edges of the graph.
            The overlapping houses are returned in a list.
        """
        overlap = []

        # make shapely functional boxes
        water_boxes = []
        for data in self.water:
            water_box = box(data[1][0], data[1][1], data[2][0], data[2][1])
            water_boxes.append(water_box)
        graph_box = box(0,0,self.width, self.depth)

        # UITEINDELIJK DIT MET DE 4 CORNERS IPV LOWERLEFT PLUS WIDTH IS VEEL NETTER EN MOOIER
        for house in houses:
            box1 = box(house.corner_lowerleft[0], house.corner_lowerleft[1], (house.corner_lowerleft[0]+house.width), (house.corner_lowerleft[1]+house.length))
            
            # check for overlap between edges graph and houses and save in list
            if box1.overlaps(graph_box):
                overlap.append(house)

            for house2 in houses:
                box2 = box(house2.corner_lowerleft[0], house2.corner_lowerleft[1], (house2.corner_lowerleft[0]+house2.width), (house2.corner_lowerleft[1]+house2.length))
                # IPV .CORNER_LOWERLEFT MET IDS OF STRUCTURE WERKEN OM ZEKER TE WETEN WELK HUIS
                # check for intersections between different houses and save in list
                if house.corner_lowerleft is not house2.corner_lowerleft and box1.intersects(box2) and house not in overlap:
                    overlap.append(house)

            for water_box in water_boxes:
                # check for instersection between water areas and housese and save in list
                if box1.intersects(water_box) and house not in overlap:
                    overlap.append(house)
                
        return overlap

    def closest_house(self, house, houses):
        """
            Checks which house is most nearby another house
        """
        # save all the corners of the house
        house_point1 = house.corner_lowerleft
        house_point2 = [house_point1[0], house_point1[1] + house.length]
        house_point3 = [house_point1[0] + house.width, house_point1[1] + house.length]
        house_point4 = [house_point1[0] + house.width, house_point1[1]]
        house_pointlist = [house_point1, house_point2, house_point3, house_point4]

        # output list that returns a house and its distance/vrijstand
        output = []

        for neigh_house in houses:
            # UITEINDELIJK MET ID OF STRUCTURE EN NIET LOWERLEFT
            if neigh_house.corner_lowerleft is not house.corner_lowerleft:
                # Save all the corners of a neighbouring house
                neigh_point1 = neigh_house.corner_lowerleft
                neigh_point2 = [neigh_point1[0], neigh_point1[1] + neigh_house.length]
                neigh_point3 = [neigh_point1[0] + neigh_house.width, neigh_point1[1] + neigh_house.length]
                neigh_point4 = [neigh_point1[0] + neigh_house.width, neigh_point1[1]]
                neigh_pointlist = [neigh_point1, neigh_point2, neigh_point3, neigh_point4]
            
                # Compare the points of given house and its neighbours to find shortest distance
                for housepoint in house_pointlist:
                    for neighpoint in neigh_pointlist:
                        distance = Point(housepoint[0],housepoint[1]).distance(Point(neighpoint[0],neighpoint[1]))
                        if output == []:
                            output.append(neigh_house)
                            output.append(distance) 
                        elif distance < output[1]:
                            output = []
                            output.append(neigh_house)
                            output.append(distance)

        # format [huisobject, getal die distance aangeeft]
        return output


    def all_houses_set(self):
        pass

    def move_house(self):
        pass

    def delete_house(self):
        pass

    def swap_house(self):
        pass


