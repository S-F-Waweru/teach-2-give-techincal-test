'''
	Question 4: Capitalize Words
	Write a program that accepts a string as input, capitalizes the first letter of each word in the
	string, and then returns the result string.
'''

words = input("Enter multiple word here: \n")

# getindividual words

char_words_array =[]
new_sentence_array = []

words_array = words.split()
for word in words_array:

	char_word = list(word)
	char_word[0] = (char_word[0].upper())

	new_word = ''.join(char_word)
	new_sentence_array.append(new_word)





new_sentence = ' '.join(new_sentence_array)
print(new_sentence)