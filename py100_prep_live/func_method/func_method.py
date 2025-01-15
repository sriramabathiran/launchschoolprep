# def find_vowels(txt):
#     list1 = []
#     for l in txt.lower():
#         if l == 'a' or l == 'e' or l =='i'  or  l == 'o' or l == 'u':
#             for w in list1:
#                 if w == l:
#                     continue
#                 else:
#                     list1 += list1[l]

# print(find_vowels("aeiou"))
# print(find_vowels('inform bud at america'))


# """
# problem2:

# p:
# takes string data type as an arg and return a dictionary object 

# """

"""
Write a function find_vowels that takes a string as an argument and returns a list containing all of the vowels present in that string. The vowels should old appear once in the output list and should be alphabetized.

Examples and expected output:
1. User inputs: Simple Plan --> Output: ['a', 'e', 'i']
2. User inputs: Put thE Fork agAinst the wall nOw. --> Output: ['a', 'e', 'i', 'o', 'u']
"""


# VOWELS = ('a', 'e', 'i', 'o', 'u')

# def find_vowels(string):
#     vowel_list = []
#     for vowel in VOWELS:
#         if vowel in string:
#             vowel_list += vowel
#     return vowel_list

# my_input = input('Please input a string: ')
# my_input = my_input.lower()     # lowercase to avoid duplicates
# vowels = find_vowels(my_input)
# print(vowels)



# wirte a function to add two numbers that reruns sum of two numbers


# def sum(a,b):
#     return abs(a) + abs(b)

# print(sum(4,0))
# print(sum(5,-3))
# print(sum(-4,-2))


# write a function revers_string(s) takes a string and returns it reversed

def reverse_str(txt):
    length = len(txt)
    reversed_str = []
    for index in range(length - 1, -1, -1):
        reversed_str.append(txt[index])
    return ''.join(reversed_str)

print(reverse_str('Sriram'))
print(reverse_str('I am a Little Boy'))


# write a function max of three (a, b, c) that returns the maximum of three numbers

# def max_of_three(a,b,c):
#     return max(a,b,c)

# def prompt(num):
#     return int(input("Enter the " + num + " Number: " ))

# first_num = prompt('First')
# second_num = prompt('Second')
# third_num = prompt('Third')

# print(max_of_three(first_num, second_num, third_num))