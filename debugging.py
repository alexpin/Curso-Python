def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    while True:
        try:
            num = int(input("Ingresa un numero: "))
            if num < 0:
                raise ValueError
            print(divisors(num))
            print("Terminó el programa")
            break 
        except ValueError:
            print('Debes ingresar un numero entero positivo')


if __name__ == '__main__':
    run()
