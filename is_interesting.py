def is_interesting(number, awesome_phrases):
	if number + 1 in awesome_phrases or number + 2 in awesome_phrases:
		return 1

	if number in awesome_phrases:
		return 2

	if num_interesting(number):
		return 2

	if num_interesting(number + 1) or num_interesting(number + 2):
		return 1

	return 0


def num_interesting(number):	

	if number % 100 == number:
		return False

	string = str(number)

	if string[1:] == (len(string) - 1) * "0": #all zeros
		return True

	if len(set(string)) == 1:#same numbers
		return True

	if string[::-1] == string:#palidrome
		return True

	if string in "1234567890":#increasing
		return True

	if string in "9876543210":#decreasing
			return True

"""	b = []
	a = []
	answer1 = 0
	answer2 = 0
	for i in str(number):
		b.append(int(i))
	for i in range(1, len(b)):#all zeros
		if b[i] == 0: answer1 += 1
		answer2 += 1
	if answer1 == answer2: return True

	answer1 = 0
	answer2 = 0
	for i in range(len(b) - 1):#same number
		if b[i] == b[i+1]: answer1 += 1
		answer2 += 1
	if answer1 == answer2: return True
	
	for i in range (1, len(b) + 1): # incementing
		a.append(i)
	if a == b: return True

	a = []
	for i in range (1, len(b) + 1): # decrementing
		a.append(i)
	if a[::-1] == b: return True

	if b == b[::-1]: return True #palindrome"""