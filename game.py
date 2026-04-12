import random

def play_game():
    print("\n🎮 Welcome to the Guess Game!")
    number = random.randint(1, 10)

    attempts = 3

    while attempts > 0:
        try:
            guess = int(input("Guess a number (1-10): "))

            if guess == number:
                print("🎉 Correct! You win!")
                return
            else:
                print("❌ Wrong guess.")
                attempts -= 1
                print("Attempts left:", attempts)

        except ValueError:
            print("Enter a valid number.")

    print(f"😢 You lost. The number was {number}")
