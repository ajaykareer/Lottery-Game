import random
from game.user import user_scores
from game.scoreboard import view_scoreboard

def play_lottery(user):
    """Runs the lottery game and updates the user's win/loss score."""
    print(f"\n--- Welcome to the Lottery Game, {user}! ---")
    print("Type 'm' to return to the main menu at any time.")
    print("-" * 40)

    while True:
        user_input = input("\nEnter your number (1 to 5), or 's' to view scoreboard, or 'm' to return to the main menu: ").lower()
        
        if user_input == 'm':
            print("Returning to the main menu...")
            break
        
        if user_input == 's':
            view_scoreboard(user)
            continue
        
        if not user_input.isdigit() or not (1 <= int(user_input) <= 5):
            print("\n😵 Whoa! That's not a valid choice! You have to pick a number between 1 and 5. Or maybe 'm' to go back to the menu. Try again!")
            continue
        
        user_pick = int(user_input)
        winning_number = random.randint(1, 5)
        print(f"\nThe winning number is: {winning_number}")
        
        if user_pick == winning_number:
            print("🎉 Congratulations! You won! 🎉")
            user_scores[user]['wins'] += 1
        else:
            print("😞 Sorry, you lost. Better luck next time.")
            user_scores[user]['losses'] += 1
