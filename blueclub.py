agecolour = input("What is your age and your favourite colour? (Seperate answers with a coma, eg, 13,blue) ")
agecolour =int(agecolour)
if agecolour >= 12:
    print("You are eligible to join the blue club!")
elif agecolour <= 12:
    print("Sorry, you must be atleast 12 years old and choose blue as your favourite colour to join the blue club.")
# Line 2 doesn't work, I don't know how to make it work either. Error code below:
# ValueError: invalid literal for int() with base 10: '12,blue'
# What's a literal????
# I used the same logic I used in kidsclub.py except for the seperate question with a coma thing because
# the question asks for me to ask it together. Even if I seperated them I would need to add both of the 
# colour and age in the same if statement and compare them with "12,blue" but it doesn't say how to do that in any of my notes