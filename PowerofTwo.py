'''
Question 3: Power of Two
Write a program that takes an integer as input and returns true if the input is a power of two.'''

Runnning = True

while Runnning:
	number = input("Enter an Integer: \n")
	try:
		lcm = int(number)
		while (lcm % 2) == 0:
			lcm = lcm / 2

		if lcm == 1:
			print(f"{number} => True")
			Runnning = False
		elif lcm != 1:
			print(f"{number} => False")
			Runnning = False
	except ValueError as e:
		print("Integer Expected")
		Runnning = True
		