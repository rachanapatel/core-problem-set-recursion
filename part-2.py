# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if len(array) < 1:
        return False
    if query == array[0]:
        return True
    array = array[1:]
    return search(array, query)


# is_palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True

    if len(text) == 2:
        return text[0] == text[-1]
        
    if text[0] == text[-1]:
        text = text[1:-1]
        return is_palindrome(text)
    return False


# digit_match
def recursive_count(apples, oranges, count):
    if len(apples) == 0 or len(oranges) == 0:
        return count
    if apples[-1] == oranges [-1]:
        count += 1
    return recursive_count(apples[0:-1], oranges[0:-1], count)

def digit_match(apples, oranges):
    apples = str(apples)
    oranges = str(oranges)
    match_count = recursive_count(apples, oranges, 0)
    return match_count


x = digit_match(1072503891, 62530841)
print('ans', x)

