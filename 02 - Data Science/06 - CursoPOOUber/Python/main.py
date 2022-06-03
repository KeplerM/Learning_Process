# from Python.uberX import UberX
from car import Car
from account import Account
from uberX import UberX
from uberPool import UberPool
from user import User

if __name__=="__main__":
    print("Hola Mundo")

    car = UberX("AMS234", Account("Andres Herrera", "ANDA876"), "Chevrolte", "Spark")
    print(vars(car))
    print(vars(car.Driver))

    car2 = UberPool("QWE567", Account("Martha", "MDAN456"), "Chevrolet", "Aveo" )
    print(vars(car2))
    print(vars(car2.Driver))

    user = User("Diego Martinez", "REA789", "diego@hotmail.com", "*****")
    print(vars(user))

    