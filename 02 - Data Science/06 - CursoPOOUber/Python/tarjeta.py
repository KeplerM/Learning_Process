from payment import Payment

class tarjeta(Payment):
    Number = str
    codevv = str
    date = str

    def __init__(self, ID, Number, codevv, date):
        super().__init__(ID)
        self.Number=Number
        self.codevv = codevv
        self.date = date

