'''
	Question 6: Count Vowels
	Write a program that counts the number of vowels in a sentence.
'''

sentence = input("Enter a sentence :\n")
count = 0

for word in sentence.split():
	count+=1


print(count)
