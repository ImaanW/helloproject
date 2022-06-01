# COMPARISONS
# EQUAL: ==
# NOT EQUAL: !=
# GREATER THAN: >
# LESS THAN: <
# GREATER OR EQUAL: <=
# LESS OR EQUAL: >=
# OBJECT IDENTITY: IS (if values have the same id or same object in memeory


language = 'java'

if language == 'english':
    print('language is english')
elif language == 'java':
    print('language is java')
else:
    print('no match')

# BOOLEAN OPERATIONS
# AND - makes sure both have to be true
# OR - only one or the other needs to be true
# AND - twitched false to true

a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))
print(a is b)


# FALSE VALUES
# False
# None
# Zero of any numeric type
# Any empty sequence for example, '', (), []
# Any empty mapping, for example {}.

# everything else will evaulate to true