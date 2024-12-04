############# (PROJECT 2) NUMBER GUESSING GAME ###############

import random  # Import the random module to generate a random number

def main():
    count = 0  # Initialize the attempt counter
    random_num = random.randint(1, 100)  # Generate a random number between 1 and 100

    # Introduction message to the player
    print("Welcome to the Number Guessing Game!\nTry to guess the number between 1 and 100.\n")

    # Infinite loop to keep asking for user input until the correct guess
    while True:
        try:
            count += 1  # Increment the attempt counter with each guess
            guess_num = input("Enter your guess: ")  # Take user input as a guess

            # Check if the input is a valid number
            if not guess_num.isdigit():
                raise ValueError  # Raise a ValueError if input is not a number
            else:
                int_guess_num = int(guess_num)  # Convert the input to an integer
                
                # Compare the user's guess with the random number
                if int_guess_num < random_num:
                    print("Too low!\n")  # Inform the user that the guess is too low
                    continue  # Continue to the next iteration
                elif int_guess_num > random_num:
                    print("Too high!\n")  # Inform the user that the guess is too high
                    continue  # Continue to the next iteration
                else:
                    # If the guess is correct, congratulate the user and display the attempt count
                    print(f"Congratulations! You've guessed the number in {count} attempts.\n")
                    break  # Exit the loop once the correct number is guessed

        # Handle invalid input (i.e., if the input is not a number)
        except ValueError:
            print("Please enter a number (1,3,6,2,...etc) only!\n")  # Inform the user to enter valid numbers

# This ensures that the game starts when the script is run directly
if __name__ == "__main__":
    main()