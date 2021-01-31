def permutations(string):
    # все вожможные порядок букв из строки
    result = set([string])
    if len(string) == 2:
        result.add(string[1] + string[0])

    elif len(string) > 2:
        for i, c in enumerate(string):
            for s in permutations(string[:i] + string[i + 1:]):
                result.add(c + s)
    return list(result)

print(permutations('aabbccc'))