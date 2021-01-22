import copy
import matplotlib.pyplot as plt

from code.classes.graph import Graph

class Randomstate_Hillclimber:

    def __init__(self, loops, houses, area):
        self.loops = loops
        self.houses = houses
        self.area = area


    def looper(self):
        """
            In a loop of n times, decided by the number of loops, random states will be generated.
        """
        best_value = 0
        best_state = []

        y_axes = []

        for loop in range(self.loops):
            # randomly assign the invalid placed houses until a valid state is reached
            self.area.randomly_assign_houses(self.houses)

            # calculate final houseprice
            self.area.houseprices(self.houses)

            # get final houseprice
            final_networth = self.area.get_networth(self.houses)

            if best_value < final_networth:
                best_value = final_networth
                best_state = copy.deepcopy(self.houses)

            # reset the graph
            self.area.area_reset(self.houses)
            self.area.price_reset(self.houses)

            # y_axes.append(best_value)
            # plt.subplot(131)
            # plt.plot(y_axes)
            # plt.savefig('../plots/simulated_annealing.png')

        # final outcome
        self.area.load_houses(best_state)
        self.area.write_output(best_state)
