def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
        
    num = input("Ingresa un numero: ")
            
    
    assert num.isnumeric() and int(num) > 0, "Debes ingresar un entero positivo"
    # isnumeric es un metodo que devuelbe true si el usuario ingresa un numero en caso contrario false
    # Es un metodo de las cadenas de carracteres por eso no se hace casting con int.
    print(divisors(int(num)))
    print("Terminó el programa")
                    

if __name__ == '__main__':
    run()