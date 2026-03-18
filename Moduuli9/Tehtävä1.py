class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def __repr__(self):
        return  f"License plate: {self.license_plate}\n" \
                f"Maximum speed: {self.maximum_speed}\n" \
                f"Current speed: {self.current_speed}\n" \
                f"Travelled distance: {self.travelled_distance}\n" \

car = Car("ABC-123","142 km/h")

print(car)
