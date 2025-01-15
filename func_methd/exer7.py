def foo(bar, qux): # fucntion obj is declaare and two postional parameters are required when fucntion is invoked
    print(bar) # value pointed by the internal variable is printed
    print(foo) # value pointed by the internal variable is printed

foo('hello') # error will be thrown that 2nd positional argument is missing.