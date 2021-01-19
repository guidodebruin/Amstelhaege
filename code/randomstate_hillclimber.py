from graph import Graph

class Randomstate_Hillclimber:

    def __init__(self, loops):
        self.loops = loops


    def looper(self):
        """
            In a loop of n times, decided by the number of loops, random states will be generated.
        """
        for loop in range(self.loops):
            # go through algorithm