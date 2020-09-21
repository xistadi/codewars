def unique_in_order(iterable):
    b = []
    temp = 0
    for i in iterable:
        if temp != i:
            b.append(i)
            temp = i
        else: temp = i
    return b