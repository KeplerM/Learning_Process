from car import Car

class UberVan(Car):
    typeCarAccepted = []
    seatsMaterial = []

    def __init__(self, License, Driver, typeCarAccepted, seatMaterial):
        super().__init__(License, Driver)
        self.typeCarAccepted = typeCarAccepted
        self.seatsMaterial = seatMaterial