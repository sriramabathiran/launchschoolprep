def foo(bar, qux) # declaring function object with two parameters as input
    print(bar) # printing the local variable bar
    print(qux) # printing the local variable qux

foo(42,3.141592,2,718) # passing 3 arguments to a function in which two parameters are required, should throw an error
# bcoz it only needs 2 argument.