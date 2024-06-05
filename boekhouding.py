import csv
from helper import som
from presentatie import presenteer

inkomsten = {
    "Aardbeien-ijs": 1000,
    "Vanille-ijs": 2000,
    "Chocolade-ijs": 1500,
    "Waterijsjes": 750
    }

totaal_inkomsten = som(inkomsten)

presenteer(inkomsten, totaal_inkomsten)

with open('boekhouding.csv', 'w', newline="") as csvfile:
    for item,bedrag in inkomsten.items():
        writer = csv.writer(csvfile, delimiter = ";")
        writer.writerow([item,bedrag])