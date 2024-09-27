user_scores = {}

def ask_for_user_name():
    """Prompts the user to enter their name and initializes their scores."""
    user = input("Please enter your name: ").strip().title()
    
    if user not in user_scores:
        # Initialize new user with 0 wins and losses
        user_scores[user] = {'wins': 0, 'losses': 0}
    
    print(f"\n🎮 Welcome, {user}! Let's start the game!")
    return user

def change_user():
    """Allows the user to change players without exiting the game."""
    return ask_for_user_name()
