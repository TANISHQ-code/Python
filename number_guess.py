import random
low = 1
high = 10
num = random.randint(low, high)
guesses = 0

guess = int(input("Guess the number between 1 to 10: "))

while True:
    if guess < 1 or guess > 10:
        print("Out of range, please try again!")
    elif guess != num:
        print("Nope, not the number!!")
        guesses += 1
    else:  # guess == num
        print("Yesss, correct number!")
        guesses += 1
        print(f"You guessed it in {guesses} guesses")
        break
    
    # 🔑 Ask for a new guess after each attempt
    guess = int(input("Try again: "))

