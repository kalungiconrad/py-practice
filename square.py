"""
a function which can generate a list where the values are square of numbers between 1 and 20(both included)
print the first five elements in a list
"""
def generator():

    square_list=[num**2 for num in range(1,20)]
    print(square_list[0:5])
    return square_list[0:5]

# generator()