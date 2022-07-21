def accum(s):
    s = s.lower()
    new_s =''
    for count, letter in enumerate(s):
        new_s += letter.upper() + letter*count + '-'
    return new_s[:-1]
