# formatter is a string, just a string, but meant to accept 4 arguments using .format()
formatter = "{} {} {} {}"

#print formatter, passing different values into the format() method
#integers
print(formatter.format(1, 2, 3, 4))
#strings
print(formatter.format("one", "two", "three", "four"))
#booleans
print(formatter.format(True, False, False, True))
#variables, which in this case hold strings which perhaps confusing is the same string we're calling :)
print(formatter.format(formatter, formatter, formatter, formatter))
#More strings but with longer text -- using this for some experimentation
print(formatter.format(
    "Try your",
    "Own text here.",
    "If you add a fifth argument it will be ignored because 'formatter' only has space for four.",
    "Error occurs if you don't have all four arguments.",
    "fifth argument"
))

#This also works because it just prints the string literal of `{} {} {} {}` stored in the variable
print(formatter)