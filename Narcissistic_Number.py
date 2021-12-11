import math

def narcissistic( value ):
    res = 0
    var = int(math.log10(value)+1)
    list_value = [int(i) for i in str(value)]
    for x in range(var):
        res += list_value[x] ** var
    if res == value:
        return True
    else:
        return False