def nb_year(p0, percent, aug, p):
    count = p0
    year = 0
    percent = percent/100
    n = p - p0
    for i in range(n):
        if count < p: 
            count += percent*count + aug
            count = int(count)
            year += 1
        if count >= p:
            break
    return year
