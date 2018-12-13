"""
a program that accepts sequence of lines as input and prints the lines 
after making all characters in the sentence capitalised. 

"""

def Upper_case():
	string = input("enter sentence:")
	if type(string) is str:
		return string.upper()
	else:
		print('invalid input: please enter a string')
		return print(Upper_case())



print(Upper_case())