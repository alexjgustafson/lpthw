from sys import argv
#read the WYSS section for how to run this
script, first = argv

#According to pydoc, argv[0] is the script pathname if its known
#That's why script worked in this example

second = input("Second variable: ")
third = input("Third variable: ")

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

