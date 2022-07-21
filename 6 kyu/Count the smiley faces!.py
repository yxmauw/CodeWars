def count_smileys(arr):
    if arr == []:
        return 0
    
    counter = 0
    
    for item in arr:
        if item == ':)' or item == ':D' \
        or item == ';)' or item == ';D' \
        or item == ':-)' or item == ':-D' \
        or item == ':~)' or item == ':~D' \
        or item == ';-)' or item == ';-D' \
        or item == ';~)' or item == ';~D':
            counter += 1
    return counter
