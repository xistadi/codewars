def digital_root(n):
	x = str(n)
	sum = 0
	while len(x) > 1:
		for temp in x:
			sum += int(temp)
		x = str(sum)
		sum = 0
	else: return int(x)