import csv

with open('archivo\\datos.csv') as archivo:
    print(csv.reader(archivo))
    reader = csv.reader(archivo)
    for row in reader:
        print(row)