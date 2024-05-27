class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage



class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity):
        super().__init__(name, max_speed, mileage)
        self.capacity = capacity
    def announce_capacity(self):
        print(f"this bus can carry up to {self.capacity} passengers.")

my_bus = Bus(name="Volvo", max_speed=80, mileage=10, capacity=50)
my_bus.announce_capacity()
