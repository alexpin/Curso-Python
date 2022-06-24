def run():
    #my_dic = {}

    #for i in range(1, 101):
    #    if i % 3 != 0:
    #        my_dic[i] = i**3
    my_dic = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print(my_dic)

    challenge_two = {i: round(i**0.5, 2) for i in range(1, 1001)}
    # redondea a dos cifras i y calcula su raiz cuadrada
    # Las llaves son los naturales del uno al 100 y los valores sun raices cuadradas.
    print(challenge_two)

if __name__ == '__main__':
    run()
