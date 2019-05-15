import csv

with open("Sales Records.csv", "r") as csv_file_thing:
    reader = csv.reader(csv_file_thing)
    fruits_sales = 0
    clothes_sales = 0
    meat_sales = 0
    beverages_sales = 0
    office_supplies_sales = 0
    cosmetics_sales = 0
    snacks_sales = 0
    personal_care_sales = 0
    household_sales = 0
    vegetables_sales = 0
    baby_food_sales = 0
    cereal_sales = 0
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
        if item_type == "Office Supplies":
            office_supplies_sales += float(profits)
        if item_type == "Cosmetics":
            cosmetics_sales += float(profits)
        if item_type == "Snacks":
            snacks_sales += float(profits)
        if item_type == "Personal Care":
            personal_care_sales += float(profits)
        if item_type == "Household":
            household_sales += float(profits)
        if item_type == "Vegetables":
            vegetables_sales += float(profits)
        if item_type == "Baby Food":
            baby_food_sales += float(profits)
        if item_type == "Cereal":
            cereal_sales += float(profits)
    print("Fruits", fruits_sales)
    print("Clothes", clothes_sales)
    print("Meat", meat_sales)
    print("Beverages", beverages_sales)
    print("Office Supplies", office_supplies_sales)
    print("Cosmetics", cosmetics_sales)
    print("snacks", snacks_sales)
    print("Personal Care", personal_care_sales)
    print("Household", household_sales)
    print("Vegetables", vegetables_sales)
    print("Baby food", baby_food_sales)
    print("Cereal", cereal_sales)