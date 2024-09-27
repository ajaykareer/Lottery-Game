# Lottery Game
# 🎲 Advanced Lottery Game 🎲

Welcome to the **Advanced Lottery Game**! This is an interactive, command-line-based lottery game where users can guess numbers, compete against each other, and track wins and losses. The game is designed with a playful, humorous touch to make the experience more fun.

## 🏆 Features

- **Play the Lottery**: Guess a number between 1 and 5 and see if you can beat the odds!
- **Score Tracking**: Keep track of how many games you’ve won or lost.
- **High Score**: View the player with the highest number of wins and try to beat them!
- **Change Players**: Easily switch between different users during gameplay.
- **Save Scores**: Save all user scores to a text file (`lottery_scores.txt`) for future reference.
- **Fun and Humor**: The game comes with playful, fun messages to make the experience more enjoyable!

## 📂 Project Structure

This project is split into multiple modules for better organization and maintainability.


### 🛠 Modules Overview

- **`main.py`**: The entry point for the game. It controls the game flow and user interactions.
- **`lottery.py`**: Handles the core lottery game mechanics (e.g., picking numbers, generating random winning numbers).
- **`scoreboard.py`**: Manages score tracking and displays the user scoreboard or high score.
- **`user.py`**: Manages user login, switching, and keeps track of user scores.
- **`file_manager.py`**: Handles file operations to save scores into a text file.
- **`utils.py`**: Contains utility functions like displaying the game menu.

## 🎮 How to Play

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ajaykareer/LOTTERY-GAME

2. **Navigate to the project directory**:
    cd lottery_game

3. **Run the game**:
    python3 main.py

3. **Choose an option from the menu**:

    1: Play the lottery by guessing a number between 1 and 5.
    2: View your scoreboard (wins/losses).
    3: Change the player.
    4: View the player with the highest wins.
    5: Save your scores to a file (lottery_scores.txt).
    6: Quit the game.

## 📝 Saving Scores
At any time, you can save the current scores of all players to a file by selecting Option 5 from the main menu. This will create or update the lottery_scores.txt file, which contains a record of wins and losses for each player.

## 💡 Contributions
Feel free to contribute to the project by submitting issues or creating pull requests. Whether you want to add new features, improve the code, or just report a bug, all contributions are welcome! 🎉

## 📄 License
This project is licensed under the MIT License.