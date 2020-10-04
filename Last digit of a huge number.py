def last_digit(lst):
    if len(lst) == 0:
        return 1
    answer = 0
    leng = len(lst)-1
    while leng > 0:
        answer = lst[leng-1] ** lst[leng]
        lst[leng-1] = answer
        leng -= 1
    return(last_digitoutput(answer))