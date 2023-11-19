##Exercise: Rectangular Write a script that will ask for the sides of a rectangular and print out the area.Provide error messages if either of the sides is negative.
x = input("Enter breadth of rectangle: ")
y = input("Enter length of rectangle: ")
x=int(x)
y=int(y)
if x < 0:
    print("Invalid, please enter a positive no. ")
elif y < 0:
    print("Invalid, please enter a positive no. ")
if x > 0:
    print(x*y ,"Is the total area")
if y > 0:
    print(x*y ,"Is the total area")