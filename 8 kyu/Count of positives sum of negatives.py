def count_positives_sum_negatives(arr):
    if arr == [] or None:
        return []
    new_arr = []
    count = len([i for i in arr if i > 0])
    neg_sum = sum([i for i in arr if i < 0])
    new_arr.append(count)
    new_arr.append(neg_sum)
    return new_arr
