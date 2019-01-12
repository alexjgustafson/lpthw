#Import the argv module
from sys import argv

#Unpack a couple variables from the arguments provided when users calls this script
script, input_file = argv

#A function that takes a file as a parameter and prints the entirety of that file
def print_all(f):
    print(f.read())

#A function that takes a file as a parameter and sets the read/write point to the beginning of the file
def rewind(f):
    f.seek(0)

#A function that takes a number and file as parameters. Print the number, then also print the content at that line number in the file.
def print_a_line(line_count, f):
    print(line_count, f.readline(), end = "")

#Open the file the user provides when script is called and store the returned file object into a variable
current_file = open(input_file)

#Print text for benefit of the user
print("First let's print the whole file:\n")

#Call the print_all function, passing the file user provided as argument
print_all(current_file)

#Print some new text for the benefit of the user
print("Now let's rewind, kind of like a tape.")

#Call the rewind function, passing the file user provided as argument
rewind(current_file)

#Printing more text for benefit of the user
print("Let's print three lines:")

# Call the print_a_line function, selecting Line 1 of the user-provided file
current_line = 1
print_a_line(current_line, current_file) # current_line is 1

# Call the print_a_line function, selecting Line 2 of the user-provided file
current_line += 1
print_a_line(current_line, current_file) # current_line is 2

# Call the print_a_line function, selecting Line 3 of the user-provided file
current_line += 1
print_a_line(current_line, current_file) # current_line is 3

print("\n")