from multiprocessing.sharedctypes import Value


def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"fristname": "Alexander", "lastname": "Pino"}

    super_list = [
        {"fristname": "Alexander", "lastname": "Pino"},
        {"fristname": "Miguel", "lastname": "Torres"},
        {"fristname": "Pepe", "lastname": "Rodelo"},
        {"fristname": "Susana", "lastname": "Miranda"},
        {"fristname": "Jose", "lastname": "Pino"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for i in super_list:
        print(i["fristname"], i["lastname"])

    for values in super_list:
        for key, value in values.items():
            print(key, "_", value)


if __name__ == '__main__':
    run()