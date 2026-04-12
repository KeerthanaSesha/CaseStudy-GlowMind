from mood import log_mood
from journal import write_journal, view_journal, search_journal
from challenge_generator import get_challenge
from game import play_game
from workourtracker import log_workout, view_workouts


def main_menu():
    while True:
        print("\n====== 🌟 Glow Mind App 🌟 ======")
        print("1. Log Mood")
        print("2. Write Journal")
        print("3. View Journal")
        print("4. Search Journal")
        print("5. Get Daily Challenge")
        print("6. Play Game")
        print("7. Log Workout")
        print("8. View Workouts")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            log_mood()

        elif choice == "2":
            write_journal()

        elif choice == "3":
            view_journal()

        elif choice == "4":
            search_journal()

        elif choice == "5":
            get_challenge()

        elif choice == "6":
            play_game()

        elif choice == "7":
            log_workout()

        elif choice == "8":
            view_workouts()

        elif choice == "9":
            print("👋 Goodbye! Take care of yourself 💙")
            break

        else:
            print("❌ Invalid choice. Try again.")


# Run the app
main_menu()
