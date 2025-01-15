# def remainders_3(numbers):
#     return any([number %3 for number in numbers])

# numbers_1 = [0,1,2,3,4,5,6]
# numbers_2 = [1,2,5,5]
# numbers_3 = [0,3,6]
# numbers_4 = []

# print(remainders_3(numbers_1))
# print(remainders_3(numbers_2))
# print(remainders_3(numbers_3))
# print(remainders_3(numbers_4))

def remainders_5(numbers):
    return all([number % 5 for number in numbers])

numbers_1 = [0,1,2,3,4,5,6,7,8,9,10]
numbers_2 = [1,2,3,4,6,7,8,9]
numbers_3 = [0,5,10]
numbers_4 = []

print(remainders_5(numbers_1))
print(remainders_5(numbers_2))
print(remainders_5(numbers_3))
print(remainders_5(numbers_4))







