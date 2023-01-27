import random

EASY = 10
HARD = 5

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
user_input = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

number_guess = random.randint(1, 100)

should_continue = True
while should_continue:
    def check_guess():
        if number_input == number_guess:
            print("You won the game.")
        elif number_input < number_guess:
            print("Too low.")
        elif number_input > number_guess:
            print("Too high.")

    if user_input == "easy":
        print(f"You have {EASY} attempts remaining to guess the number.")
        number_input = int(input("Make a guess: "))
        check_guess()
        if number_input != number_guess:
            EASY = EASY - 1
            if EASY == 0:
                print("You lose")
                print(f"The number is {number_guess}")
                should_continue = False
            else:
                print("Guess agian.")
        elif number_input == number_guess:
            should_continue = False
    elif user_input == "hard":
        print(f"You have {HARD} attempts remaining to guess the number.")
        number_input = int(input("Make a guess: "))
        check_guess()
        if number_input != number_guess:
            HARD = HARD - 1
            if HARD == 0:
                print("You lose")
                print(f"The number is {number_guess}")
                should_continue = False
            else:
                print("Guess agian.")
        elif number_input == number_guess:
            should_continue = False
    else:
        print("Please enter a valid difficulty level. 'Easy' or 'Hard: ")
        user_input = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
