# STRING CONT BUT LISTS


# You get an array of numbers, return the sum of all of the positives ones.

# USING THE BUILT IN SUM FOR RETURNING POSTIVE

def positive_sum(arr):
    return sum(x for x in arr if x > 0)


# return the sum of x, for every  x(variable) in arr(the array), that is greater than zero
# here the built in function was used

print(positive_sum([-5000, 4000, 1000]))


# FOR RETURN NEGATIVE
def negative_sum(arr):
    return sum(x for x in arr if x < 0)


# here it says return the sum of x(variables in array) for every x in array, if x is less than zero
# this outputs the sum of negative numbers

print(negative_sum([-5000, 4000, 1000]))


# COUNT() return the total count of a given element in a string.
def count_sheep(x):
    return x.count(True)


# or


def count_sheeps1(sheep):
    return len([x for x in sheep if x])


# return the length of : the variable , for every variable in sheep if x (if x=bool=true)


# if an integer number is divisible by both integers a and b.
def is_divide_by(number, a, b):
    return number % a == 0 and number % b == 0


# Complete the square sum function so that it squares each number passed into it and then sums the results together.
def square_sum(numbers):
    return sum(number ** 2 for number in numbers)


# Now calculate the average of array and compare your score! Return True if you're better, else False!

def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)
