class Car(Vehicle):
    def __init__(self, color, has_winter_tires=False):
        super().__init__(color)
        self.has_winter_tires = has_winter_tires

    def __str__(self):
        return f"{super().__str__()}\nHas winter tires: {self.has_winter_tires}"
