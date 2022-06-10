def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors



def run():
    #while True:
        try:        
            num = int(input("Ingrese un numero: "))
            if num < 0:
                raise ValueError("No se puede ingresar un número negativo")
            print(divisors(num))
            print("Termino mi programa")

        except ValueError as ve:
            print(ve)
            return False    

if __name__ == '__main__':
    run()
