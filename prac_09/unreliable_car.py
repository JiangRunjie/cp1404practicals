from prac_09.car import Car
import random


class UnreliableCar(Car):
    reliability = random.uniform(0, 100)

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()}"

    def drive(self, distance):
        car_reliability = random.randint(0, 100)
        if car_reliability < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        print(f"distance = {self.distance}km, distance driven = {distance_driven}km")


my_taxi = ['Prius', 100, 1.23]
instance = UnreliableCar(my_taxi[0], my_taxi[1], my_taxi[2])
print(instance)
