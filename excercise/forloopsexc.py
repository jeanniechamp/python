#Print numbers from 1 to 10 using range().
for x in range(1,11):
    print (x)
#Print numbers from 10 to 1 in reverse order using range()
for x in range(1,10,-1):
    print (x)
#Print only the even numbers from 1 to 20
for x in range(1, 21):
    if x % 2 == 0:  
        print(x)
#Print only the odd numbers from 1 to 20.
for x in range (1,21):
    if x%2 != 0 :
        print(x)
#Sum all the numbers from 1 to 50.
for x in range (1,51):


    total = 0
for i in range(1, 51):
    total += i
print(total)

#Find the product of all the numbers from 1 to 10.

for x in range (1,11):


    total = 1
    for i in range(1, 11):
        total *= i
print(total)
