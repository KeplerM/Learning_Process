from car import Car
from account import Account

if __name__=="__main__":
    print("Hola Mundo")

    car = Car("AMS234", Account("Andres Herrera", "ANDA876"))
    print(vars(car))
    print(vars(car.Driver))

    car2 = Car("QWE567", Account("Martha", "MDAN456"))
    print(vars(car2))
    print(vars(car2.Driver))