def first_non_repeating_letter(string):
    if len(string) > 0:
        for l in string:
            answer = ""
            if string.upper().count(l.upper()) == 1:
                answer += l
                break

        if len(answer) > 0:
            return answer
        else: return ""
    else: return ""