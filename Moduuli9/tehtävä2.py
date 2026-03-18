class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        uusi_nopeus = self.current_speed + change
        if uusi_nopeus > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif uusi_nopeus < 0:
            self.current_speed = 0
        else:
            self.current_speed = uusi_nopeus



