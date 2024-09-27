from game.user import user_scores

def view_scoreboard(user):
    """Displays the scoreboard for the current user."""
    if user_scores[user]['wins'] == 0 and user_scores[user]['losses'] == 0:
        print("\n🤔 Hmm... You haven't played yet! How about giving the game a try first before checking the scoreboard? 😄")
    else:
        wins = user_scores[user]['wins']
        losses = user_scores[user]['losses']
        print("\n" + "="*30)
        print(f"   SCOREBOARD for {user}   ")
        print("="*30)
        print(f"Total Wins  : {wins}")
        print(f"Total Losses: {losses}")
        print("="*30)


def view_high_score():
    """Displays the player with the highest wins."""
    if all(user_scores[user]['wins'] == 0 for user in user_scores):
        print("\n😅 Looks like no one has played yet! Maybe start a round before going for the high score, champ!")
        return

    # Find the player with the highest wins
    highest_winner = max(user_scores, key=lambda user: user_scores[user]['wins'])
    high_score = user_scores[highest_winner]['wins']
    
    # Calculate the dynamic length for the decoration
    highest_winner_text = f"Player with the highest wins: {highest_winner}"
    max_length = max(len(f"HIGHEST WINS: {high_score}"), len(highest_winner_text))
    decoration = "=" * (max_length + 4)  # Add extra padding for spaces

    print(f"\n{decoration}")
    print(f"   HIGHEST WINS: {high_score}   ")
    print(decoration)
    print(f"   {highest_winner_text}   ")
    print(decoration)
