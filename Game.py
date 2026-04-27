import random

# Let the player pick a difficulty level
def select_level():
    print("\nSelect a difficulty level:")
    print("1) Easy   -> range 1 to 50")
    print("2) Medium -> range 1 to 100")
    print("3) Hard   -> range 1 to 200")

    user_choice = input("Your choice: ").strip().lower()

    if user_choice in ["1", "easy"]:
        return 1, 50
    elif user_choice in ["2", "medium"]:
        return 1, 100
    elif user_choice in ["3", "hard"]:
        return 1, 200
    else:
        print("Invalid choice. Defaulting to Medium.")
        return 1, 100


# Keep asking until a valid number is entered
def read_guess(low, high):
    while True:
        user_input = input(f"Guess a number between {low} and {high}: ")

        try:
            value = int(user_input)

            if low <= value <= high:
                return value
            else:
                print("That number is out of range.")

        except ValueError:
            print("Please enter a valid integer.")


# Runs one full round of the game
def run_round():
    print("\n=== Number Guessing Game ===")

    low, high = select_level()
    secret_number = random.randint(low, high)

    tries = 0

    while True:
        guess = read_guess(low, high)
        tries += 1

        if guess < secret_number:
            print("Too low — go higher.")
        elif guess > secret_number:
            print("Too high — go lower.")
        else:
            print("Correct! Congratulations!")
            print(f"You guessed it in {tries} tries.")
            break


# Main loop to replay the game
def main():
    while True:
        run_round()

        again = input("Play again? (y/n): ").strip().lower()

        if again not in ["y", "yes"]:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
