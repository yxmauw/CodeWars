def sum_dig_pow(a, b):
    final_lst = [] 
    for i in range(a, b+1):
        if i < 10:
            final_lst.append(i)
        if i >= 10:
            digit_i = [int(i) for i in str(i)]
            
            lst = []
            power = 1
            
            for j in digit_i:
                power_j = j**power
                lst.append(power_j)
                power += 1
            if i == sum(lst):
                final_lst.append(i)
    return final_lst
