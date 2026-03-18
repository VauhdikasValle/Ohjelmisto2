import random

class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def drive(self, tunnit):
        self.travelled_distance += self.current_speed * tunnit

    def accelerate(self, change):
        uusi_nopeus = self.current_speed + change
        if uusi_nopeus > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif uusi_nopeus < 0:
            self.current_speed = 0
        else:
            self.current_speed = uusi_nopeus

def race(cars):
    while True:
        for auto in cars:
            change = random.randint(-10, 15)
            auto.accelerate(change)
            auto.drive(1)
            if auto.travelled_distance >= 10000:
                return cars
autot = []
for i in range(1, 11):
    rekisteri = f"BMW-{i}"
    huippunopeus = random.randint(100, 200)
    uusi_auto = Car(rekisteri, huippunopeus)
    autot.append(uusi_auto)
