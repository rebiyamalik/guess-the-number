import random

def choose_difficulty():
    print("\nChoose Difficulty Level:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")
    
    while True:
        choice = input("Enter 1, 2 or 3: ")
        if choice == '1':
            return 1, 50, 10
        elif choice == '2':
            return 1, 100, 7
        elif choice == '3':
            return 1, 200, 5
        else:
            print("❌ Invalid choice. Try again.")

def play_game():
    print("\n🎲 Welcome to the Guess the Number Game!")

    low, high, max_attempts = choose_difficulty()
    secret_number = random.randint(low, high)
    attempts = 0

    print(f"\nI'm thinking of a number between {low} and {high}...")
    print(f"You have {max_attempts} attempts to guess it!")

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}: Enter your guess: "))
            attempts += 1

            if guess < low or guess > high:
                print(f"⚠️ Please guess a number between {low} and {high}.")
                continue

            if guess < secret_number:
                print("📉 Too low!")
            elif guess > secret_number:
                print("📈 Too high!")
            else:
                print(f"🎉 Correct! The number was {secret_number}.")
                print(f"You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("❌ Please enter a valid number.")
    else:
        print(f"\n💥 Out of attempts! The number was {secret_number}.")

def main():
    while True:
        play_game()
        again = input("\n🔁 Do you want to play again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("👋 Thanks for playing! Goodbye!")
            break

# Run the game
main()
