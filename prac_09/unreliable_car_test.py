import random
from prac_09.car import Car

class Unreliable_car(Car):
    reliability = random.uniform(0, 100)

    def __init__(self, name, fuel, reliability):
        self.name = name
        self.fuel = fuel
        self.reliability = reliability
        self.distance = 0
        self.distance_driven = 0

    def dirve(self, reliability):
        Car_reliability = 50
        if reliability >= Car_reliability:
            distance = 0
        else:
            distance = random.random(0,100)
        self.distance += distance
        return self.distance

    def distance_driven(self, distance,):
        self.distance_driven += distance
        return self.distance_driven

    def __str__(self):
        return f"{self.name}, fuel= {self.fuel}, distance= {self.distance}km, distance driven= {self.distance_driven}km"


my_taxi = ['Prius', 100, 1.23]
instance = Unreliable_car(my_taxi[0], my_taxi[1], my_taxi[2])
print(instance)