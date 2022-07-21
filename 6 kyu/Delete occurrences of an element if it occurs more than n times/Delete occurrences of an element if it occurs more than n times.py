def delete_nth(order,max_e):
    if order == [] or max_e < 1:
        return []
    
    order_count = {x:0 for x in order}
    new_order = []
    
    for item in order:
        if order_count[item] < max_e:
            order_count[item] += 1
            new_order.append(item)
    return new_order
