# what happens when you run the following program? why do we get that result?

def set_foo(): ## function object is declared
    foo = 'bar' # assigning a value to internal variable

set_foo() # calling the function, no outputs wil be printed
print(foo) # will get an error because foo is an internal variable