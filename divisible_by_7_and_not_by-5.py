"""

a programe which will find all such numbers which are divisible by 7
 but are not a multiple of 5,between 2000 and 3200(both included)
the numbers obtained should be printed in a comma - seperated sequence on a single line

"""

def finder():
	for num in range(2000, 3201, 7):
		if num%5!=0:
			print(f' {num}', end =',')


finder()