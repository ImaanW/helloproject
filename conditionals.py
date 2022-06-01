# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
def bool_to_word(boolean):
    if bool(boolean) == 0:
        return "No"
    else:
        return "Yes"

# if value of boolean variable = 0 (which equals to false), return no otherwise its positive and return yes
#OR

def bool_to_word(bool):
    return "Yes" if bool else "No"