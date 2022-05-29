class Account:
    ID       = int
    Name     = str
    Document = str 
    Email    = str
    Password = str

    def __init__(self, Name, Document):
        self.Name     = Name
        self.Document = Document