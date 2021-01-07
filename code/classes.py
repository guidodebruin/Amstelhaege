import csv

class Plattegrond():
    def __init__(self, wijk):
        """
            Maakt de plattegrond
        """
        self.water = []

        # road room structures
        self.load_water(f"../wijken/{wijk}.csv")
        print(self.water)

    def load_water(self, filename):
        """
            Laadt het water dat bij een specifieke wijk hoort
        """
        with open(filename, "r") as csv_file:
            next(csv_file)
            reader = csv.reader(csv_file)

            for row in reader:
                self.water.append(row)
            csv_file.close()