def find_outlier(integers):
    listpair = []
    listimpair = []
    for x in integers:
        if (x % 2) == 0:
            listpair.append(x)
        else:
            listimpair.append(x)
   
    if len(listpair) == 1:
        return listpair[0]
    else:
        return listimpair[0]