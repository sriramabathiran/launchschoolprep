def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)
foo(42)

# What is the result of running this code?

# we will get syntax error because we have to pass default arguments for all postional arguments
# after the one we have intiated to give default values - her  we had given for second identifier
# but not for the third one. so it will end up in syntax error