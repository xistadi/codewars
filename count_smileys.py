def count_smileys(arr):
	countsmileyfaces = 0
	for i in arr:
		for b in range(len(i)-1):
			if i[b] == ";" or i[b] == ":":
				if i[b+1] == "-" or i[b+1] == "~":
					if i[b+2] == "D" or i[b+2] == ")":
						countsmileyfaces += 1
				elif i[b+1] == "D" or i[b+1] == ")":
					countsmileyfaces += 1
	return countsmileyfaces
