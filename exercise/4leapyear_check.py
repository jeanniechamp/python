#Exercise: Write a program to check whether an years is leap year or not.
ly = input("Enter a year to find if its a leap year: ")
ly =int(ly)
print(ly%4)
if ly%4 == 0:
    print("this year is a leap year!")
else:
    print("not a leap year!")