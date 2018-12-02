#Assign integer to a variable
types_of_people = 10
#Assign a formatted string to a variable
x = f"There are {types_of_people} types of people."

#Assign a string literal to a variable
binary = "binary"
#Assign a string literal to a variable
do_not = "don't"
#Assign a formatted string to a variable
y = f"Those who know {binary} and those who {do_not}."

#Print out a couple variables
print(x)
print(y)

#Print out some formatted strings that contain those variables within them
print(f"I said: {x}")
print(f"I also said: '{y}'")

#Assign a boolean to a variable
hilarious = False
#Assign  a string to a variable that includes a spot for a variable in the .format() syntax later
joke_evaluation = "Isn't that joke so funny?! {}"

#Print that variable, and use the .format() syntax to pass a variable
print(joke_evaluation.format(hilarious))

#Assign some strings to some variables
w = "This is the left side of..."
e = "a string with a right side."

#Print some concatenated variables
print(w + e)