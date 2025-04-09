# A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces


# Create a Function
def child(name, candyamnt):
    if candyamnt > 2:
        print(f"*kills* you can no longer have candy {name}")
    else: print(f'alright maybe you can have some candy {name}')

# child("George", 2)
# Function only activates when we call on it

# Using the return (make a mini calculator)
def sum(num1, num2):
    total = num1 + num2
    return total
"""num = sum(1,2)
print ('Sum =', num)"""
    


# A lambda function is  a small anonymous function.
sum = lambda num1, num2: num1 * num2
print(sum(3,4))

# The lambda eliminates the need to total AND return total. It process the calculation within itself in that ONE expression.

# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

