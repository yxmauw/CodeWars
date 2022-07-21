def is_isogram(string):
    string = string.lower()
    string_lst = [letter for letter in string]
    dict = {letter:0 for letter in string}
    
    if string == '':
        return True
    
    for letter in string_lst:
        if letter in dict:
            dict[letter] += 1
    
    if len(set(dict.values())) == 1:
        print(set(dict.values()))
        return True
    else:
        return False
