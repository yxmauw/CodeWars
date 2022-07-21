import string

def rot13(message):
    alphalower_lst = list(string.ascii_lowercase)
    alphaupper_lst = list(string.ascii_uppercase)
    digit_lst = list(string.digits)
    whitespace_lst = list(string.whitespace)
    special_lst = list(string.punctuation)
    
    dict = {}
    
    for i in range(0, 13):
        dict[alphalower_lst[i]] = alphalower_lst[i+13]
        dict[alphaupper_lst[i]] = alphaupper_lst[i+13]
    for i in range(13, 26):
        dict[alphalower_lst[i]] = alphalower_lst[i-13]
        dict[alphaupper_lst[i]] = alphaupper_lst[i-13]
    for i in range(0, 10):
        dict[digit_lst[i]] = digit_lst[i]
    for i in range(0, 6):
        dict[whitespace_lst[i]] = whitespace_lst[i]
    for i in range(0, 32):
        dict[special_lst[i]] = special_lst[i]
        
    new_message = ''.join([dict[char] for char in message])
    return new_message
