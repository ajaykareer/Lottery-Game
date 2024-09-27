from game.user import ask_for_user_name, change_user
from game.lottery import play_lottery
from game.scoreboard import view_scoreboard, view_high_score
from game.file_manager import save_scores_to_file
from game.utils import display_menu

def main():
    """Main function to run the lottery game with a menu system."""
    print("\n🎉🎲 Welcome to the Advanced Lottery Game! 🎲🎉")
    
    # Start by asking for the user's name
    user = ask_for_user_name()
    
    while True:
        display_menu()
        user_choice = input("\nChoose an option (1, 2, 3, 4, 5, or 6): ").strip()

        if user_choice == '1':
            play_lottery(user)
        elif user_choice == '2':
            view_scoreboard(user)
        elif user_choice == '3':
            user = change_user()
        elif user_choice == '4':
            view_high_score()
        elif user_choice == '5':
            save_scores_to_file()
        elif user_choice in ['6', 'quit', 'exit']:
            print("\nThanks for playing! Goodbye! 👋")
            # Add footer after the exit message
            print("\n" + "="*30)
            print("   Created by Ajay Kareer    ")
            print("="*30)
            break
        else:
            print("\n🤨 Whoops! That's not a valid option! Did you press the wrong button? It's okay, but let's keep it between 1 and 6, okay? Try again!")

if __name__ == "__main__":
    main()
