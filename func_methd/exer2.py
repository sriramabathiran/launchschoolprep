foo = 'bar' # value is assigned to a variable (external)

def set_foo(): # function object is declared
    foo = 'qux' #internal variable foo is called

set_foo() # functional is called, no output will be printed
print(foo) # value will be printed from external variable