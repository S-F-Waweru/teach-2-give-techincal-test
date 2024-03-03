'''	
	Question 2: Fibonacci Sequence
	Write a program to generate the Fibonacci sequence up to 100.
'''

n = 100

last_term = 0
second_last_term = 1

count = 0

while count <= n:
	if count == 0:
		print(0)
	new_term = last_term + second_last_term

	if new_term > n:
		break;

	print(new_term)
	second_last_term = last_term
	last_term = new_term
	count +=1