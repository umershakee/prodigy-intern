import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        user_guess = int(input("Enter your guess (between 1 and 100): "))
        attempts += 1

        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the right number {number_to_guess} in {attempts} attempts.")
            break

if __name__ == "__main__":
    guessing_game()

