def solution(string,markers):
    #solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
    #output "apples, pears\ngrapes\nbananas"
    answer = ""
    b = []
    b = string.split("\n")
    for one_string in b:
        temp = 1
        counter_spaces = 1
        for letter in one_string:
            if letter == " ":
                counter_spaces += 1
            if letter in markers:
                temp = one_string.count(letter)
                if counter_spaces > 1:
                    answer = answer.rstrip()
                    break
                break
            answer += letter
        answer += "\n" * temp
    answer = answer[:len(answer)-1]
    return answer
print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))