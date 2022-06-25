def run():
   # squares = [] # Crea una lista vacia
   # for i in range(1, 101):
   #     if i % 3 !=0: # Si el resto de la division es distinto de cero
   #         squares.append(i**2) # Agrega a la lista squares el contenido de i elevandolo al cuadrado  
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    print(squares)

    challenge = [i for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0 ]
    print(challenge)

  

if __name__ == '__main__':
    run()

