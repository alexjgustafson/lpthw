from sys import argv

# Define a function to print out some text about cheese and crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

#Call the cheese and crackers function and pass through two integers as arguments
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# Assign some integers to variables
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# Call the cheese and crackers function and pass through the 
# two variables as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#Call the cheese and crackers function doing math within the arguments
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

#Call the cheese and crackers function doing math within the arguments
#And the math includes the variables, too!
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def fortune_cookie_joke( string = '' ):
    joke = f"{string} in bed."
    print( joke )
    return joke

# 1 pass a string literal
fortune_cookie_joke("You will find true love on Flag Day")

# 2 Store a string in a variable and pass the variable
fortune_cookie = "Your friends need your kindness"
fortune_cookie_joke( fortune_cookie )

# 3 Call the function passing the same function as the argument
fortune_cookie_joke( fortune_cookie_joke( 'Howdy' ) )

# 4 If you pass an integer it'll get put in the string
fortune_cookie_joke( 27 )

# 5 If you pass a boolean it'll get put in the string
fortune_cookie_joke( False )

# 6 Add some escape characters in our string literal
fortune_cookie_joke( "Stop with the joke...\n..." )

# 7 formatted string
fortune_cookie_joke( f"\'{fortune_cookie}\' is a repeated fortune" )

# 8 no arguments, rely on the default value
fortune_cookie_joke()

# 9 Use user input
fortune_cookie_joke( input("What's your favorite fortune cookie? > ") )

# 10 We imported argv, let's call that
fortune_cookie_joke( argv[0] )