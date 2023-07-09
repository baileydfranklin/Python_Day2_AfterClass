# Write a Python function called max_num()to find the maximum of three numbers.
def max_value(num1, num2, num3):
    max_value = max(num1, num2, num3) # Built in Python Function
    return max_value

print(max_value(10, 20, 30))

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(listOfNumbers):
    result = 1
    for num in listOfNumbers:
        result *= num
    return result

my_list = [1, 3, 5, 7, 9, 11]
result = mult_list(my_list)
print(result)

# Write a Python function called rev_string() to reverse a string.
def rev_string(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string

    return reversed_string

my_string = "Hello World!"
result = rev_string(my_string)
print(result)

# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
def num_within(num, range1, range2):
    if range1 <= num <= range2:
        return True
    else:
        return False
    
example1 = num_within(3, 1, 10)
print(example1)

example2 = num_within(13, 1, 10)
print(example2)

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.

# *** no idea...