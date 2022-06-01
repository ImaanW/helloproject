N = 24
numbers = range(1, N + 1)
for i in numbers:
    if (i % 2 == 0 and i % 3 == 0 and i % 5 == 0):
        print('CodilityTestCoders')
    elif (i % 2 == 0 and i % 3 == 0):
        print('CodilityTest')
    elif (i % 2 == 0 and i % 5 == 0):
        print('CodilityCoders')
    elif (i % 3 == 0 and i % 5 == 0):
        print('TestCoders')
    elif (i % 2 == 0):
        print('Codility')
    elif (i % 3 == 0):
        print('Test')
    elif (i % 5 == 0):
        print('Coders')
    else:
        print(i)
# ensure you have the complex first,
# ensure you have all combinations
# plus one as the N (meaning 24) when using range function it goes up to value, not including
# uses and as you have to tell python what to do, repeat code and be clear
# AND means both are true
# elif - an this , and this
# Else - if not true, excecute this

factorial = 1

for i in range(1, 5):
    if i < 5:
        print(i)
    elif i + 1:
        print(i + 1)

# ITERATION FOR LOOP/IF CONDITIONALS
n = 4
for i in range(1, n + 1):
    if i < 5:
        print('*' * i)
# MINUS
for i in range(n, 0, -1):
    for j in range(n - i):
        print(' ')
        for j in range(2 * i - 1):
            print('*')
            print



