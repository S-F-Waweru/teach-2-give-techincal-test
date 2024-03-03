'''
	Question 5: Reverse Integer
	Write a program that takes an integer as input and returns an integer with reversed digit
	ordering.
	
'''


Running = True
while Running:
	input_number = input("Enter an integer: \n")

	try:
		# check if its a integer
		number = int(input_number)
		string_number = list(input_number)
		if string_number[0] == '-':
			string_number.pop(0)
			
			new_string_number = [''.join(string_number)[::-1]]
			new_string_number.insert(0, '-')
			final_number =''.join(new_string_number)
			print(int(final_number))

		else:
			print(''.join(string_number)[::-1])

		Running = False

	except ValueError as e:
		print("An integer number is required:")



