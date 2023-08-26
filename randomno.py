import random

num1 = random.randint(1, 3)
guess = input("Guess the secret number between 1- 3: ")
guess =int(guess)
if guess == num1 :
    print("Congrats!",num1,"was the right answer")
else :
    print("Wrong answer, the correct answer was",num1)