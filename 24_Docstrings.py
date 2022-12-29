# docstrings are the strings that are writen right after the function defination and before function body.
# Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.

def square(n):
  #  print(n**2)
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)
    