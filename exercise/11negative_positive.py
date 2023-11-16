##Exercise: Write a program to check whether a number (accepted from user) is positive or negative.
x = input("Enter a number: ")
x=int(x)
if x < 0:
    print("This number is negative")
elif x:
    print("This number is positive")