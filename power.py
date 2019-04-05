def power(a,n):
	b = a
	while(n !=1):
		a = a*b

		n -= 1

	return a

print(power(4,4))
