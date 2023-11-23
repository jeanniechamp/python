import random

n = random.randint(1, 20)
guess = input("Guess the secret number between 1- 20: ")
guess =int(guess)
if guess == n:
    print("Your guess is correct!")
elif guess > n:
    print("Your guess is", guess - n ,"less")
elif guess < n:
    print("Your guess is", n - guess ,"greater")
print ("the number was",n)