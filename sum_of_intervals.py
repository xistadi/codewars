def sum_of_intervals(intervals):
	a = []
	for i in intervals:
		for b in range(i[0], i[1]):
			a.append(b)
	return len(list(set(a)))