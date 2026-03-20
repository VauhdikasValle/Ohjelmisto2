class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor

    def go_to_floor(self, floor):
        new_floor = self.current_floor + floor
        if new_floor






