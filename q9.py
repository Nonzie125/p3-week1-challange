class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Info: {self.year} {self.make} {self.model}")

# Example usage
my_car = Car("porsche", "Cayenne", 2021)
my_car.display_info()  # Output: Car Info: 2021 porsche Cayenne
