class Car:

    car_rates = {"bmw": 50000, "tesla": 65000, "audi": 40000, "opel":30000, "toyota": 35000, "mercedes": 45000}

    def __init__(self, brand: str, manufacture_year: int):
        self.brand = brand.lower()
        self.year = manufacture_year

    @property
    def Price(self):
        if self.brand in Car.car_rates:
                return Car.car_rates[self.brand]

        return -125

if __name__ == "__main__":
    #  car exists
    bmw = Car("BMW", 2020)
    print(bmw.Price)

    #  car does not exist
    print(Car("omni", 2013).Price)
