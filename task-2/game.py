import random

def number_guessing_game():
   
    secret_number = random.randint(1, 100)
    max_attempts = 7  # You can change this as needed

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")

 
    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if guess < secret_number:
            print("Too low! Try again.\n")
        elif guess > secret_number:
            print("Too high! Try again.\n")
        else:
            print(f"Congratulations! You guessed it right in {attempt} attempt(s)!")
            break
    else:
        print(f"Sorry! You've used all {max_attempts} attempts. The number was {secret_number}.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        print("Running tests...")
    else:
        print("Starting the Number Guessing Game...")
number_guessing_game()
