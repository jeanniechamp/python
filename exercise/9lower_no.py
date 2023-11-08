##Exercise: Write a program to find the lowest number out of two numbers excepted from user.
x =input("Enter no. 1: ")
y =input("Enter no. 2: ")
x =int(x)
y =int(y)
if x < y:
    print(x,"is smaller than",y)
else:
    print(y,"is smaller than",x)