import itertools

def Fibanocci_Thousand_Digits():
	DIGITS = 1000
	prev = 1
	cur = 0
	for i in itertools.count():
		# At this point, prev = fibonacci(i - 1) and cur = fibonacci(i)
		if len(str(cur)) > DIGITS:
			raise RuntimeError("Not found")
		elif len(str(cur)) == DIGITS:
			return str(i)
		
		prev, cur = cur, prev + cur


if __name__ == "__main__":
	print(Fibanocci_Thousand_Digits())

