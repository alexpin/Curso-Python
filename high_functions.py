def run():
# Uso de filter
    my_list1 = [1,4,5,6,9,13,19,21]
    odd = list(filter(lambda x: x%2 !=0, my_list1))
    print(odd)


# Uso de map
    my_list = [1, 2, 3, 4, 5]
    squares2 = list(map(lambda x: x**2, my_list))
    print(squares2)

#Uso de reduce
    from functools import reduce
    my_list3 = [2,2,2,2,2]
    all_multiplied = reduce(lambda a, b: a*b, my_list3)
    print(all_multiplied)

if __name__ == '__main__':
    run()