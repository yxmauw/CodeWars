def longest_consec(strarr, k):
    n = len(strarr)
    if k <= 0 or n == 0 or k > n:
        return ''
    longest_length = 0
    index = 0
    for i in range(n - k + 1):
        length = sum([len(s) for s in strarr[i:i+k]])
        if length > longest_length:
            longest_length = length
            index = i
    return ''.join(strarr[index:index+k])
