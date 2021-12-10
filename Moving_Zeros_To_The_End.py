def move_array(arr):
    l = [i for i in arr if isinstance(i,bool) or i !=0]
    return l + [0]*(len(arr)-len(l))



----------------------------------------------------------------------


def move_zeros(array):
    list = []
    list0 = []
    for x in array:
        if x != 0:
            list.append(x)
        else:
            list0.append(x)
            
    final_list = list + list0
    
    return final_list