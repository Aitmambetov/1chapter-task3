"""@ Makers
Write a function last_letter that returns the last letter of a string.
Ex: last_letter('hello!') # --> !
"""



def last_letter(word):
    return word [-1]
#DO NOT remove lines below here, this is designed to test your code.
def test_last_letter():
    assert last_letter('hello!') == '!'
    assert last_letter('banana') == 'a'
    assert last_letter('8') == '8'
    assert last_letter('funnyguys') == 's'
    assert last_letter('101') == '1'
    print("YOUR CODE IS CORRECT!")

#test your code by un-commenting the line(s) below
test_last_letter()