def generate_hashtag(s):
	if s == "":
		return False
	else:
		answer = "#"
		for i in s.title():
			if i.isalpha():
				answer += i
		if len(answer) > 140:
			return False
		return answer