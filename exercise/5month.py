#Exercise: Write a program to accept a number from 1 to 12 and display name of the month and days in that month like 1 for January and number of days 31 and so on
month = input("Enter a number from 1-12: ")
month=int(month)
if month > 12:
    print("not valid, pick a number from 1-12.")
elif month == 1:
    print("January, 31 days")
elif month == 2:
    print("February, 28/29 days")
elif month == 3:
    print("March, 30 days")
elif month == 4:
    print("April, 31 days")
elif month == 5:
    print("May, 30 days")
elif month == 6:
    print("June, 31 days")
elif month == 7:
    print("July, 30 days")
elif month == 8:
    print("August, 31 days")
elif month == 9:
    print("September, 30 days")
elif month == 10:
    print("October, 31 days")
elif month == 11:
    print("November, 30 days")
elif month == 12:
    print("December, 31 days")