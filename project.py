import random  # Import random module for generating random numbers

def perfect_guess_game():
    best_score = None  # Store best score in the current session (None means no score yet)

    while True:  # Outer loop: allows the game to restart after finishing
        print("\n🎯 Welcome to The Perfect Guess Game!")
        print("Choose difficulty level:")
        print("1. Easy (1-50)")
        print("2. Medium (1-100)")
        print("3. Hard (1-200)")

        choice = input("Enter 1, 2 or 3: ")  # Take difficulty choice from user

        # Assign random number and max number based on difficulty
        if choice == '1':
            target = random.randint(1, 50)   # Easy: number between 1 and 50
            max_num = 50
        elif choice == '2':
            target = random.randint(1, 100)  # Medium: number between 1 and 100
            max_num = 100
        elif choice == '3':
            target = random.randint(1, 200)  # Hard: number between 1 and 200
            max_num = 200
        else:
            print("Invalid choice! Please select again.")
            continue  # Go back to start of loop if input is invalid

        guess_count = 0  # Track number of attempts for this round

        print(f"\nGuess the number between 1 and {max_num}!")

        # Inner loop: keeps asking until the player guesses correctly
        while True:
            try:
                # Take guess as integer
                guess = int(input("Enter your guess: "))
                guess_count += 1  # Increment number of tries
            except ValueError:
                # Handle invalid input (non-numeric)
                print("❌ Please enter a valid number!")
                continue  # Skip rest and ask again

            # Compare guess with target
            if guess > target:
                print("📉 Lower number please!")  # Guess is too high
            elif guess < target:
                print("📈 Higher number please!")  # Guess is too low
            else:
                # Correct guess
                print(f"🎉 Correct! You guessed it in {guess_count} tries.")

                # Check if best score needs updating
                if best_score is None or guess_count < best_score:
                    best_score = guess_count
                    print(f"🏆 New Best Score: {best_score} guesses!")
                else:
                    print(f"Best Score so far: {best_score} guesses.")
                break  # Exit inner loop when guessed correctly

        # Ask player if they want to play again
        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again != 'yes':
            # If answer is anything other than "yes", exit the game
            print("👋 Thanks for playing! Goodbye!")
            break  # Exit outer loop and end the game

# Start the game
perfect_guess_game()
