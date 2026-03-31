class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def floor_up(self):
        self.current_floor += 1

    def go_to_floor(self, floor):
        if floor < self.bottom_floor or floor > self.top_floor:
            return

        if self.current_floor < floor:
            for i in range(floor - self.current_floor):
                self.floor_up()
                print(f"Current floor: {self.current_floor}")
        elif self.current_floor > floor:
            for i in range(self.current_floor - floor):
                self.floor_down()
                print(f"Current floor: {self.current_floor}")
        else:
            print(f"Current floor: {self.current_floor}")
            return

    def floor_down(self):
        self.current_floor -= 1


class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []

        for i in range(number_of_elevators):
            new_elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(new_elevator)

    def fire_alarm(self):
        for hissi in self.elevators:
            hissi.go_to_floor(self.bottom_floor)
            pass


    def run_elevator(self, elevator_number, destination_floor):
        hissi = self.elevators[elevator_number]
        hissi.go_to_floor(destination_floor)



