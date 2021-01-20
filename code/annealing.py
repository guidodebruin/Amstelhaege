from graph import Graph

class Simulated_Annealing:

    def __init__(self, loops, changes, houses, area):
        self.loops = loops
        self.changes = changes
        self.houses = houses
        self.area = area

    def simulate(self):
        """"
            Repeatedly generates random states.
            Tries to find to most optimal house coordinates in each random state.
        """"
        # create a random state

        # move a random house in this state

        # check if better or worse than current state
        # if better -> keep this state
        # if worse -> check if state can be accepted with formula
            # accepted -> repeat process
            # not accepted -> go back to last state and repeat process

        # find best position of houses in this random state
            # if better than other random states -> deepcopy

        # get new random state and repeat process
        pass