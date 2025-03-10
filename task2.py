class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

# Example usage:
my_bus = Bus(name="My Bus", max_speed=80, mileage=10)
default_capacity = 50
print(my_bus.seating_capacity(default_capacity))
