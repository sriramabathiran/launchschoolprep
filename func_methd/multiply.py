
# declare the function object, with two parameters as input, may be set a default value if input is not received?
def multiply(left, right):
#function body declaration 
    return left * right
#1 return the result that multiples the values pointed by the internal variables



# get the 1st input from the user, float 
left = float(input("Enter the first number: ")) # 3.1415
right = float(input("Enter the first number: "))

# get the 2nd input from the user, float

# use print function and make a functional call for multiply function and pass the two fload input
print(f'{left} * {right} = {multiply(left,right)}')

