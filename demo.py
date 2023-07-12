class Manufacterer:
    name = ""
    location = ""
    brands = []

    # parameterized constructor
    def __init__(self, name, loc):
        self.name = name
        self.location = loc
        self.brands = []

    def add_brand(self, brand):
        self.brands.append(brand)

    def get_brands(self):
        print("This are the Brands for", self.name , ":", self.brands, "\n")


class Car:
    brand = ""
    model = ""
    year = 0

    # parameterized constructor
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    

    def get_details(self):
        print("Below are the specifications")
        print("\n Brand: ", self.brand, "\n Model: ", self.model, "\n Year: ", self.year, "\n")


car1 = Car("Tata", "Nexon", 2023)
car2 = Car("Mahindra", "XUV700", 2022)

# creating object of the class Car
car1.get_details()
car2.get_details()

# creating object of the class Manufacterer
man1 = Manufacterer("ABC Motors", "Ahmedabad")

man2 = Manufacterer("XY Motors", "Mumbai")

# perform Addition on man1
man1.add_brand("Tata")

# perform Addition on man2
man2.add_brand("Mahindra")

# display result of man1
man1.get_brands()

# display result of man2
man2.get_brands()
