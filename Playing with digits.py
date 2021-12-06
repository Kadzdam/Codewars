def dig_pow(n,p):
    num=str(n)
    var = 0
    liste = [int(i) for i in num]
    for x,t in enumerate(liste,start=p):
        var+=t**x
    if var%n == 0:
        res = var // n
        return res
    else:
        return -1