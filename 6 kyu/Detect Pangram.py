import string

def is_pangram(s):
    s = s.lower()
    alphabet_list = list(string.ascii_lowercase)
    no_digit_list = [i for i in s if i.isalpha()]
    for x in no_digit_list:
        if x in alphabet_list:
            alphabet_list.remove(x)
    return True if len(alphabet_list) == 0 else False
