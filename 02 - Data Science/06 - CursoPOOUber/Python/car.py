from account import Account


class Car:
    ID        = int
    License   = str
    Driver    = Account("","")
    Passengen = int

    def __init__(self, License, Driver):
        self.License = License
        self.Driver  = Driver