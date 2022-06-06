def run():

    # my_dict = {}

    #{llaves, valores}

    # for i in range(1, 101):
    #     if i % 3 !=0:
    #         my_dict[i] = i**3
        
    # DICTIONARY COMPREHENSION


    my_dict={i: i**3 for i in range(1,101) if i % 3 !=0}
    
    print(my_dict)

    # Reto: crear, un dictionay comprehension, un diccionario cuyas llaves sean los 1000 primeros numeros naturales con sus raices cuadradas como valores.

    my_dict2={i: round(i**(1/2),2) for i in range(1, 1001)}
    print(my_dict2)

    # Lo redonde a dos cifras para que sea mas visible




if __name__ == '__main__':
    run()


