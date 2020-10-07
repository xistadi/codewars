def solution(args):
	temp = []
	temp2 = []
	temp3 = 0
	answer = ""
	a = len(args)
	for i in range(a):
		if i == a - 1:
			if temp3 == 1:
				temp.append(args[i])
				answer += f"{str(temp[:1])} - {str(temp[-1:])}"
				return answer
			else:
				temp2.append(args[i])
				answer += f"{str(args[i])}"
				return answer
		else:
			if args[i] + 1 == args[i+1]:
				temp.append(args[i])
				temp3 = 1
			else:
				if temp3 == 1:
					temp.append(args[i])
					answer += f"{str(temp[:1])} - {str(temp[-1:])}" 
					temp3 = 0
					temp = []
				else: 
					temp2.append(args[i])
					answer += f"{str(args[i])}"