from taxi import Taxi


class Silver_Service_Taxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = fanciness * self.price_per_km

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall}"

    def get_fare(self):
        return super().get_fare() + self.flagfall


my_taxi = ['Prius', 100, 10]
instance = Silver_Service_Taxi(my_taxi[0], my_taxi[1], my_taxi[2])
print(instance)
