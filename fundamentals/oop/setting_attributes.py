class Shoe:

    def __init__(self, brand, shoe_type, price):
        self.brand = brand
        self.type = shoe_type
        self.price = price
        self.in_stock = True
    
    def on_sale_by_percent(self, percent):
        self.price = self.price * (1 - percent)
        
    def on_sale_by_dollar(self, dollar_amount):
        self.price = self.price - dollar_amount
        
    def tax_calculation(self, tax):
        self.price = self.price * (1 + tax)


skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
work_shoe = Shoe("Timberland", "Boots", 150.00)

work_shoe.in_stock = 'False'


# skater_shoe.on_sale_by_percent(0.2)
# work_shoe.on_sale_by_percent(0.3)
# dress_shoe.on_sale_by_percent(0.1)

skater_shoe.on_sale_by_dollar(50)
work_shoe.on_sale_by_dollar(20)
dress_shoe.on_sale_by_dollar(10)

# skater_shoe.tax_calculation(0.2)
# work_shoe.tax_calculation(0.3)
# dress_shoe.tax_calculation(0.1)

print(skater_shoe.type)
print(skater_shoe.price)
print(dress_shoe.price)
print(dress_shoe.type)
print(work_shoe.type)
print(work_shoe.price)
print(work_shoe.in_stock)
