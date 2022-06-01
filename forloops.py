
# break - completely break out of a loop (stops it)
# continue - moves on to the next iteration(skips/ignores to the next)

# BREAK STATEMENT IN LOOP
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print('found it')
        break
    print(num)

# printed out 1 and 2 as it didn't meet the contional but when it hit 3 and met the conditional it printed 'found it' and broke out of the for loop.

# CONTINUE STATEMENT IN LOOP
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print('found it')
        continue
    print(num)
# as soon as it hit continue it carried on to the next

# LOOP IN A LOOP, NESTED LOOP
nums = [1, 2, 3, 4, 5]
for num in nums:
    for letter in 'abc':
        print(num, letter)

# looped through first value and then looped through every value in inner loop and then went back to second value of outer loop
# gave us every value

# RANGE FUNCTION
for i in range(1,11):
    print(i)

# x = 0
# while True:
# if x == 5:
#     break
# print(x)
# x += 1

# i = 0
# order in simplicity
# writtern foen clearly and reptititive
# look  example 