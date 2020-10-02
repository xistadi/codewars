def solve_runes(runes):
    der = dict()
    for i in range(10):
        b = runes.replace("?", str(i))
    for a in b:
        der[i] = a
    print (der)







solve_runes("-5?*-1=5?")