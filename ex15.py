# This is how modules get included in python. 
# Here we're importing "argv" from the "sys" module
from sys import argv

# Argv is a way of accepting arguments from when the script is called
# This line unpacks information from argv and stores it into two variables
script, filename = argv

# The open() method is the preferred way to open a file
# When open() opens the file, it returns its file object
# Here we store that returned file object into a variable
txt = open(filename)

#Print a formatted string that includes the filename argument user supplied
print(f"Here's your file {filename}:")
#Remember that file object? This calls its read() method and prints the returned value
print(txt.read())

#Replacing this section with a new way
txt_again = open( input( 'Type the filename again:\n> ') )

#Call the read() method on that file and print the value
print(txt_again.read())

#We opened files, let's close them too
txt.close();
txt_again.close();
