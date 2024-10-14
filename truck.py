class Truck(Vehicle):
    def __init__(self, color, has_trailer=False):
        super().__init__(color)
        self.has_trailer = has_trailer

    def __str__(self):
        return f"{super().__str__()}\nHas trailer: {self.has_trailer}"
