#!/usr/bin/env python 3.10


value = int(input ("Enter a Integer Number: "))

if value % 5 == 0 and value % 3 == 0:
    print ("FizzBuzz")
elif value % 3 == 0:
    print ("Fizz")
elif value % 5 == 0:
    print ("Buzz")
else:
    print (value)
    