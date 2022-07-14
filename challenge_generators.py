import time

def fibo_gen_max(max_number: int):
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            if aux >= max_number:
                raise StopIteration
            n1, n2 = n2, aux
            counter +=1
            yield aux



if __name__ == '__main__':
    fibonacci = fibo_gen_max(1000)
    for element in fibonacci:
        print(element)
        time.sleep(0.05)
