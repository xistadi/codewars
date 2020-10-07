def solution(args):
    temp = []
    temp3 = 0
    answer = ""
    a = len(args)
    for i in range(a):
        if i == a - 1:
            if temp3 > 1:
                temp.append(args[i])
                answer += f"{''.join(str(x) for x in temp[:1])}-{''.join(str(x) for x in temp[-1:])}"
                return answer
            elif temp3 == 1:
                answer += f"{args[i-1]},{args[i]}"
                return answer
            else:
                answer += f"{str(args[i])}"
                return answer
        else:
            if args[i] + 1 == args[i+1]:
                temp.append(args[i])
                temp3 += 1
            else:
                if temp3 > 1:
                    temp.append(args[i])
                    answer += f"{''.join(str(x) for x in temp[:1])}-{''.join(str(x) for x in temp[-1:])}," 
                    temp3 = 0
                    temp = []
                elif temp3 == 1:
                    answer += f"{args[i-1]},{args[i]},"
                    temp3 = 0
                    temp = []
                else: 
                    answer += f"{str(args[i])},"

solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])