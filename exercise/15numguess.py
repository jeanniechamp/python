import random

n = random.randint(1, 20)
guess = input("Guess the no. between 1- 20: ")
guess =int(guess)
if guess == n:
    print("Your guess is correct!")
elif guess > n:
    print("Your guess is less than the secret no. ")
elif guess < n:
    print("Your guess is greater than the secret no.")
print ("the number was",n)