"""
 A grading system for the students marks below 
 [23,4,5,6,64,90,67,98,45,23,67,98,45,23,67,78,89]

100- 90 for excelent
89 -70 for very good
69-60 for good
59-40 for poor
39-20 for very poor
19-0 for repeat
 """

def grade():
	marks= [23,4,5,6,64,90,67,98,45,23,67,98,45,23,67,78,89]
	for mark in marks:
		if mark <=100 and mark>=90:
			print(  f'{mark} - excelent ')

		elif mark <=89 and mark >=70:
			print(f'{mark} - very good')

		elif mark <=69 and mark >=60:
			print(f'{mark} - good')

		elif mark <=59 and mark >=40:
			print(f'{mark} -  poor')

		elif mark <=39 and mark >=20:
			print(f'{mark} - very poor')

		elif mark <=19 and mark >=0:
			print(f'{mark} - repeat')

#grade()


