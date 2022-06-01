# CONVERT STRING TO NUMBER
# method turning it from string to interger as method name passes paramenter and same paramter is then called with int
def string_converter(s):
   return int(s)

# calling on the function to test
string_converter(45)

# confirming that the 'type is an int
print(type(string_converter(45)))



# CONVERT NUMBER TO STRING

def number_converter(n):
   return str(n)

number_converter(234)

print(type(number_converter(243)))

# SHOWS EVEN NUMBERS AND ODD NUMBERS
def even_or_odd(number):
  if number % 2 == 0:
    return "Even"
  else:
    return "Odd"

# If number can be completely divisable by 2 with 0 remainder of 0 it is an even number, everything else is odd

# take the number of petals of each flower and return true if they are in love and false if they aren't.

def lovefunc( flower1, flower2 ):
    return (flower1+flower2)%2