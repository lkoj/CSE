import csv

with open("Sales Records.csv", "r") as csv_file_thing:
    reader = csv.reader(csv_file_thing)
    fruits_sales = 0
    clothes_sales = 0
    meat_sales = 0
    beverages_sales = 0
    for row in reader:
        profits = row[13]
        item_type = row[2]
        if item_type == "Fruits":
            fruits_sales += float(profits)
        if item_type == "Clothes":
            clothes_sales += float(profits)
        if item_type == "Meat":
            meat_sales += float(profits)
        if item_type == "Beverages":
            beverages_sales += float(profits)
    print("Fruits", fruits_sales)
    print("Clothes", clothes_sales)
    print("Meat", meat_sales)
    print()