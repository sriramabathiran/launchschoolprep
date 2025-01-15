def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

#14

#multiply - line 1, 9
#left - line 1, 2 
#right - line 1,2
#get_num - line 4,7,8
#prompt - line 4, 5
#first_number - line 7, ,9 , 10
#second_number - line 8,9, 10
#product - line 9, 10
#float - 5
#input - 5
#print  - 10


#15
#local - left, right, prompt
#builtin - float, input, print
#global - first_number, second_number, product, multiply,get_num

#16

#function_names

#multiply - dfeined on line 1, called on line 9
#get_num - defined on line 4, called on line 7 and 8
#float - built in function called on line 5
#input - built in function called  on line 5
#print - built in function called  on line 10

#parameter
#left and right --> are parameters on line 1 and the local variable on line 2
#prompt --> are paramteres on line 3 and it will be a local variable on Line 4.