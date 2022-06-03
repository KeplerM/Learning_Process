from account import Account

class User(Account):
    def __init__(self, ID, Name, Document, Email, Password):
        super().__init__(Name, ID, Document, Email, Password)

        