def fob(var):

	for i in range (1, (var + 1)):
		if i % 5 == 0 and i % 3 == 0:
			print (i, "FizzBuzz")
		elif i % 3 == 0:
			print (i, "Fizz")
		elif i % 5 == 0:
			print (i, "Buzz")
		else:
			print (i)
