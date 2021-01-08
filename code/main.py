from graph import Plattegrond
import matplotlib.pyplot as plt

wijk = input("Voer wijk_nummer in: ")
while wijk not in ["wijk_1", "wijk_2", "wijk_3"] : 
    print("Kies tussen: wijk_1, wijk_2, wijk_3")
    wijk = input("Voer wijk_nummer in: ")

Plattegrond(wijk)

wijk = input("Voer de gewenste huizenvariant in: ")
while wijk not in ["20", "40", "60"] : 
    print("Kies tussen: 20, 40, 60")
    wijk = input("Voer de gewenste huizenvariant in: ")
