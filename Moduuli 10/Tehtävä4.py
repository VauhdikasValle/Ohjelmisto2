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

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for auto in self.cars:
            muutos = random.randint(-10, 15)
            auto.accelerate(muutos)
            auto.drive(1)
    def race_finished(self):
        for auto in self.cars:
            if auto.travelled_distance >= self.distance:
                return True
        return False

    def print_status(self):
        print(f"{'Rekisteri':<10} | {'Huippu (km/h)':<15} | {'Nopeus':<10} | {'Matka (km)':<10}")
        print("-" * 60)
        for auto in self.cars:
            print(
                f"{auto.license_plate:<8} | {auto.maximum_speed:<8} | {auto.current_speed:<8} | {auto.travelled_distance:<10.1f} km")

autot = []
for i in range(1, 11):
    rekisteri = f"BMW-{i}"
    huippunopeus = random.randint(100, 200)
    uusi_auto = Car(rekisteri, huippunopeus)
    autot.append(uusi_auto)


