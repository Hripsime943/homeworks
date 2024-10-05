import random
secret_numb = random.randint(1,100)
while True:
    guess = int(input("Enter your guess: "))
    if guess < 1 or guess > 100:
        print("Please guess a number between 1 and 100.")
    else:
        print("Congratulations! You guessed the number.")
        break