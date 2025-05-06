# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError
    if n == 0:
        return 1
    recurs = n * factorial(n - 1)
    return recurs



# reverse
def reverse(text):
    if len(text) < 1:
        return ""

    if len(text) == 1:
        return text[0]
        
    return reverse(text[1:]) + text[0]



# bunny
def bunny(count):
    if count == 0:
        return 0
    recurs = 2 + bunny(count - 1)
    
    return recurs



# is_nested_parens
def check_val(first, last):
    if first == "(":
        if last == ")":
            return True
    return False

def is_nested_parens(parens):
    if len(parens) < 1:
        return True

    if len(parens) % 2 == 1:
        return False
    
    if len(parens) == 2:
        return check_val(parens[0], parens[-1])
        
    check = check_val(parens[0], parens[-1])
    parens = parens[1:-1]
    
    return is_nested_parens(parens)


