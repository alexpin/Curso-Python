from __future__ import division


def make_division_by(n):
    """ This closure returns a function thar retruns the division of
    an x number by n
    """
    def division(int):
        assert n > 0, "El valor ingresado debe ser mayor a cero"
        return int / n
    return division

def run():

    division_by_3 = make_division_by(3)
    print(division_by_3(18))

    division_by_5 = make_division_by(5)
    print(division_by_5(100))

    division_by_18 = make_division_by(18)
    print(division_by_18(54))

if __name__ == '__main__':
    run()
