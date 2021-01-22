import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from singlehouse import Singlehouse
from bungalow import Bungalow
from maison import Maison
from House import House
from shapely.geometry import box, Point


class Graph():
    def __init__(self, area):
        """
            Necessities for the visual representation
        """
        self.water = []
        self.width = 180
        self.depth = 160

        # Load the water data
        self.load_water(f"../Areas/{area}.csv")

        # Create area graph
        self.load_graph()


    def load_water(self, filename):
        """
            Loads the water that belongs to a specific neighborhood
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
            Creates the map for the specific area
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
            # Add the patch to the Axes
            ax.add_patch(rect)

        # Save the graph
        plt.savefig('../plots/init_graph.png')


    def overlap(self, house, houses):
        """
            Checks for overlapping houses with each other, water or the edges of the graph.
            Returns True if a house overlaps.
        """
        # save the points of the structures in boxes to find intersection
        graph_box = box(0,0,self.width, self.depth)
        housebox1 = box(house.corner_lowerleft[0], house.corner_lowerleft[1], (house.return_upperright(house)[0]), (house.return_upperright(house)[1]))
        water_boxes = []
        for data in self.water:
            water_box = box(data[1][0], data[1][1], data[2][0], data[2][1])
            water_boxes.append(water_box)

        # check for overlap between edges graph and houses and save in list
        # if graph_box.overlaps(housebox1):
        #     return True

        # check if overlap with border of the map
        if self.check_borders(house):
            return True

        # check for intersection between water areas and houses and save in list
        for water_box in water_boxes:
            if housebox1.intersects(water_box):
                return True

        # check for intersections between different houses and save in list
        for house2 in houses:
            housebox2 = box(house2.corner_lowerleft[0], house2.corner_lowerleft[1], (house2.return_upperright(house2)[0]), (house2.return_upperright(house2)[1]))
            if house.id is not house2.id and housebox1.intersects(housebox2):
                return True
                
        return False


    def closest_house(self, house, houses):
        """
            Checks which house is most nearby another house
            The output list returns a house and its freespace
        """
        output = []

        # save all the corners of the house
        house_pointlist = [house.corner_lowerleft, house.return_upperleft(house), house.return_upperright(house), house.return_lowerright(house)]

        for neigh_house in houses:
            if neigh_house.id is not house.id:
                # save all the corners of a neighbouring house
                neigh_pointlist = [neigh_house.corner_lowerleft, neigh_house.return_upperleft(neigh_house), neigh_house.return_upperright(neigh_house), neigh_house.return_lowerright(neigh_house)]
            
                # compare the points of given house and its neighbours to find shortest distance
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

        return output


    def invalid(self, house, houses):
        """
            Checks if the freespace between houses is the same or larger than the minimum freespace required.
            Returns True if the freespace is invalid. 
        """
        nearest_neighbour = self.closest_house(house, houses)

        # Return houses with an invalid freespace distance
        if isinstance(house, Maison) and nearest_neighbour[1] < house.freespace:
            return True
        elif isinstance(house, Bungalow) and nearest_neighbour[1] < house.freespace:
            return True
        elif isinstance(house, Singlehouse) and  nearest_neighbour[1] < house.freespace:
            return True
    
        return False


    def randomly_assign_houses(self, houses):
        """
            Assigns coordinates to a single house. Checks if coordinate placement is valid.
            If not, new coordinates are assigned.
        """
        for house in houses:
            house.corner_lowerleft = house.random_lowerleft()
            while self.invalid(house, houses) or self.overlap(house, houses):
                house.corner_lowerleft = house.random_lowerleft()


    def houseprices(self, houses):
        """
            Calculates the final and total value of a house.
        """
        for house in houses:
            freespace = self.closest_house(house, houses)[1]
            extra_freespace = freespace - house.freespace
            price_increase = extra_freespace * house.percentage + 1
            house.price = round(house.price * price_increase)


    def all_houses_set(self):
        pass


    def delete_house(self):
        pass

    def swap_house(self):
        pass


    def write_output(self, all_houses):
        """
            Writes the final output in a csv file.
        """
        with open('output.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(["structure", "corner_1", "corner_2", "corner_3", "corner_4", "type"])
            singlehouse_counter = 0
            bungalow_counter = 0
            maison_counter = 0
            for house in all_houses:

                if isinstance(house, Singlehouse):
                    housetype = "EENGEZINSWONING"
                    singlehouse_counter += 1
                    structure = "singlehouse_" + str(singlehouse_counter)
                    writer.writerow([structure, ', '.join(map(str,house.return_upperleft(house))), ', '.join(map(str, house.corner_lowerleft)), ', '.join(map(str, house.return_upperright(house))), ', '.join(map(str, house.return_lowerright(house))), housetype])
                elif isinstance(house, Bungalow):
                    housetype = "BUNGALOW"
                    bungalow_counter += 1
                    structure = "bungalow_" + str(bungalow_counter) 
                    writer.writerow([structure, ', '.join(map(str,house.return_upperleft(house))), ', '.join(map(str, house.corner_lowerleft)), ', '.join(map(str, house.return_upperright(house))), ', '.join(map(str, house.return_lowerright(house))), housetype])
                elif isinstance(house, Maison):
                    housetype = "MAISON"
                    maison_counter += 1
                    structure = "maison_" + str(maison_counter)
                    writer.writerow([structure, ', '.join(map(str,house.return_upperleft(house))), ', '.join(map(str, house.corner_lowerleft)), ', '.join(map(str, house.return_upperright(house))), ', '.join(map(str, house.return_lowerright(house))), housetype])

            writer.writerow(["networth", self.get_networth(all_houses)])
    

    def get_networth(self, all_houses):
        """
            Returns the total networth
        """
        self.total_price = []
        for house in all_houses:
            self.total_price.append(house.price)
            net_worth = sum(self.total_price)
        return net_worth   


    def area_reset(self, houses):
        """
            Resets every house to its starting position
        """
        for house in houses:
            house.corner_lowerleft = [0,0]


    def price_reset(self, houses):
        """
            Resets every house price to its initial price
        """
        for house in houses:

            if isinstance(house, Maison):
                house.price = 610000
            elif isinstance(house, Bungalow):
                house.price = 399000
            elif isinstance(house, Singlehouse):
                house.price = 285000


    def check_borders(self, house):
        """
            Returns true if house placement is on top of a border of the graph
        """
        house_corners = [house.corner_lowerleft, house.return_upperleft(house), house.return_upperright(house), house.return_lowerright(house)]
        for corners in house_corners:
            for corner in corners:
                if corner < 0 or corner > 180 or corner > 160:
                    return True
        return False 

            
