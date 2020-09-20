def number(bus_stops):
	summa1 = 0
	for firsttemp in bus_stops:
		summa = firsttemp[0] - firsttemp[1]
		summa1 += summa
	return summa1
