def foo(first, second=3, third=2): # function object is declared with 3 params as input and two has default value
    print(first) # print function is caled with a single local variable
    print(second) # print function is caled with a single local variable
    print(third) # # print function is caled with a single local variable

foo(42,3.141592,2.718) # function is called with 3 arguments

#output
# 42
# 3.141592
# 2.718