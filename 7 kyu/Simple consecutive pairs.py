def pairs(ar):
    if len(ar) % 2 == 1:
        ar = ar[0:-1]
    count = 0
    for i in range(0, len(ar), 2):
        frst_num = ar[i]
        sec_num = ar[i+1]
        if frst_num - sec_num == 1 or sec_num - frst_num == 1:
            count += 1
    return count
