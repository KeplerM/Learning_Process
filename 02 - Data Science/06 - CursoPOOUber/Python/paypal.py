import email
from payment import Payment

class paypal(Payment):
    email = str
    
    def __init__(self, ID, email):
        super().__init__(ID)
        self.email=email

        