def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    elif array1 == [] and array2 == []:
        return True
    elif array1 == [] and array2 != []:
        return False
    elif array1 != [] and array2 == []:
        return False
    else:
        array1 = [n**2 for n in array1]
        for n in array1:
            if n in array2:
                array2.remove(n)
        return True if len(array2) == 0 else False
