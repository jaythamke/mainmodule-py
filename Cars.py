import sys
sys.path.append("submods/gst_calculator")
import gst_calculator as gst_calc

class Car:

    car_rates = {"bmw": 50000, "tesla": 65000, "audi": 40000, "opel":30000, "toyota": 35000, "mercedes": 45000}

    def __init__(self, brand: str, manufacture_year: int):
        self.brand = brand.lower()
        self.year = manufacture_year

    @property
    def Price(self):
        if self.brand in Car.car_rates:
            if self.year < 2016:
                return float(Car.car_rates[self.brand])
            else:
                return gst_calc.Calculate_GST(Car.car_rates[self.brand], 3.5) 

        return -125

if __name__ == "__main__":
    # car exists
    bmw = Car("BMW", 2020)
    print(bmw.Price)

    # car does not exist
    print(Car("omni", 2013).Price)

    # car exists before 2016
    bmw = Car("Tesla", 2015)
    print(bmw.Price)
