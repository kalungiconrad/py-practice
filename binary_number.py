"""
A programe that accepts a sequence of comma seperated 4digit binary numbers as its input
and then check whether they are divisible by 5 or mot.
the numbers that are divisible by 5 are to be printed in a coma seperated sequence.

# """

def binary():
	try:

		my_list=[]
		digit_list =[]
		digit_list=int(input('enter  a sequence of comma seperated 4digit binary numbers:\n'))
		for digit in digit_list:
			if len(digit)==4:
				if digit%5==0:
					my_list.append(digit)
			else:
				print('enter a four binary digit sequence number')
				return binary()
					
		return print(my_list)
		

	except(ValueError):
		print('please enter a valid binary digit')

		







