import random


class Randomize():
    def place_house(self, coordinates):
        pass

    def return_corner2(self): 
        # Get random coordinate for the width       
        x_coordinate = random.randint(0, 180)
        print("Random integer: ", x_coordinate)

        # Get random coordinate for the depth
        y_coordinate = random.randint(0, 160)
        print("Random integer: ", y_coordinate)

        corner_2 = []
        corner_2.append(x_coordinate, y_coordinate)

        return corner_2

    def return_other_corners(self, coordinates):
        pass
        
        
        # Singlehouse (x,y)
        # lowerleft coordinates = (0, -8)
        # upperright coordinates = (+8, 0)
        # lowerright coordinates = (+8, -8)

        # Bungalow (x,y)
        # get random upperleft coordinates
        # lowerleft coordinates = (0, -7)
        # upperright coordinates = (+11, 0)
        # lowerright coordinates = (+11, -7)

        # Maison (x,y)
        # get random upperleft coordinates
        # lowerleft coordinates = (-10, 0)
        # upperright coordinates = (0, 12)
        # lowerright coordinates = (-10, 12)


        
        
        
        
        
        
        
        
        
#         # Assuming:
# myList = []
# co1 = (12.3,20.2) # and so on..
# valuesToCheck = [co1,co2,co3,co4,co5,co6,co7,co8,co9]

# # In each step:
# # Adding 2 coordinates
# myList.append((x1,y1))
# myList.append((x2,y2))
# # Searching 9 specific coordinates among all
# for coordinate in valuesToCheck:
#     if coordinate in myList:
#         print "Hit!"
#         break
        
        


