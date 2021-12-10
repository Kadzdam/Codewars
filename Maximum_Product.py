from decimal import Decimal 


def adjacent_element_product(array):
    var = Decimal('-Infinity')
    for i in range(len(array)-1):
        res = array[i] * array[i+1]
        if res > var:
            var = res
    return var 