def series_sum(n):
    if n == 0:
        return '0.00'
    else:
        sum = 0
        for i in range(n):
            sum += 1 / (1 + (i * 3))
        return "{:.2f}".format(sum)
