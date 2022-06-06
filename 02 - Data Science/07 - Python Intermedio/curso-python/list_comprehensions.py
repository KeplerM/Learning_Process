def run():

    # squares = []
    # for i in range(1, 101):
    #     if i % 3 !=0:
    #         squares.append(i**2)
    

    # AHORA lIST COMPREHENSION 

    squares = [i**2 for i in range(1, 101) if i % 3 !=0]

    # Reto: con un List Comprehension, crear una lista de todos los multiplos de 4 que a la vez tambien son multiplos de 6 y de 9, hasta 5 dígitos (10000)

    squares2 = [i for i in range (1, 10001) if i % 36 ==0]   

    # se usa el 36 porque es el numero multiplo de 4, 6 y 9 al mismo tiempo. 
    # 
    print(squares)
    print(squares2)



if __name__ == '__main__':
    run()