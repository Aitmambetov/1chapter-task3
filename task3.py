
"""
Write a function is_odd that takes
in a number and returns True if it is odd, otherwise false.
BONUS CHALLENGE:
Write the function solution in 1 line of code without using if statements.
"""

def is_odd(number):
    if number % 2 == 1:
        return True
    else: 
        return False 
#DO NOT remove lines below here, this is designed to test your code.
def test_is_odd():
    assert is_odd(2) == False
    assert is_odd(3) == True
    assert is_odd(8) == False
    assert is_odd(100) == False
    assert is_odd(101) == True
    print("YOUR CODE IS CORRECT!")
#test your code by un-commenting the line(s) below
test_is_odd()