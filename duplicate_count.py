def duplicate_count(text):
	sometxt = text.upper()
	someanswer = ""
	for l in set(sometxt):
		someanswer += l
	answer = 0
	for l in someanswer:
		if text.upper().count(l.upper()) > 1:
			answer += 1
	return answer
