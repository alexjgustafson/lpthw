name = 'Alex J. Gustafson'
age = 31 # not a lie
height = 75 # inches
height_in_cm = height * 2.54 # 2.54 centimeters in an inche
weight = 274 # lbs, too high i know
weight_in_kg = weight * 0.453592 # 0.453592 kilograms in a pound
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"That's about { round( height_in_cm )} centimeters.")
print(f"He's {weight} pounds heavy.")
print(f"That's about {round( weight_in_kg ) } kilograms.")
print("It's too heavy, but he's working on it.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")