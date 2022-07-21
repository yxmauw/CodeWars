def expanded_form(num):
    num = str(num)
    digit_num = [i for i in num]
    
    if len(digit_num) == 1:
        return ''.join(digit_num)
    
    if len(digit_num) > 1:
        lst = []
        power = len(digit_num) - 1
        for j in range(len(digit_num)):
            new_num = int(digit_num[j]) * (10**power)
            power -= 1
            if new_num != 0:
                lst.append(new_num)            
        return ' + '.join(str(k) for k in lst)
