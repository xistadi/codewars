"""Задача на матем не решил забил хуй"""
def zeros(n):
	fact = 1
	for i in range(1, n + 1):
		fact *= i

	for i in len(fact):
		if (fact[-i:] % 10) == 0:


	return(fact)

zeros(7)