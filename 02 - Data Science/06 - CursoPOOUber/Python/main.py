from car import Car

if __name__=="__main__":
    print("Hola Mundo")
    car = Car()
    car.License = "AMS234"
    car.Driver = "Andres Herrera"
    print(vars(car))

    car2 = Car()
    car2.License = "QWE567"
    car2.Driver = "Martha"
    print(vars(car2))