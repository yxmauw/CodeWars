from functools import reduce

def grow(arr):
    mul_num = reduce(lambda x, y: x * y, arr)
    return mul_num
