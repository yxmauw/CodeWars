def persistence(n):
    n = [int(i) for i in str(n)]
    if len(n) <= 1:
        return 0
    
    counter = 0
    
    while len(n) > 1:
        result = 1
        for x in n:
            result *= x
        result = [int(i) for i in str(result)]
        counter += 1
        n = result
    return counter
