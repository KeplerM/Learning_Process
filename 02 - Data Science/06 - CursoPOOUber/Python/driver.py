import imp
from account import Account

class Driver(Account):
    def __init__(self, ID, Name, Document, Email, Password):
        super().__init__(Name, Document, Email, Password)
