from game.user import user_scores

def save_scores_to_file():
    """Saves the scorecards of all users to a text file."""
    file_name = "lottery_scores.txt"
    with open(file_name, 'w') as file:
        for user, scores in user_scores.items():
            file.write(f"User: {user}, Wins: {scores['wins']}, Losses: {scores['losses']}\n")
    print(f"\nScores saved to {file_name}")
