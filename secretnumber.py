secret_number = 7 
guess = input("Guess the secret number (between 1 and 10): ")
guess = int(guess)
if guess == secret_number:
    print("Congratulations! You guessed it right!")
else:
    print("Sorry, try again.")