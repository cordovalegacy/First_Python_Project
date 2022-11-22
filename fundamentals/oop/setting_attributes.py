class Shoe:

    def __init__(self, brand, shoe_type, price):
        self.brand = brand
        self.type = shoe_type
        self.price = price
        self.in_stock = True


skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
work_shoe = Shoe("Timberland", "Boots", "150.00")

work_shoe.in_stock = 'False'

print(skater_shoe.type)
print(dress_shoe.type)
print(work_shoe.type)
print(work_shoe)
print(work_shoe.in_stock)
