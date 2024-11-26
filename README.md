# Higher Lower Game
## Description
This project emulates a simple Higher Lower game, inspired by the online game available at [higherlowergame.com](https://www.higherlowergame.com/). The player is tasked with guessing which entity (person, brand, etc.) has more followers on their respective platform.

---

## How to Play
1. The game presents two entities (A and B) along with their descriptions.
2. Guess which entity has more followers by typing 'A' or 'B'.
3. If your guess is correct, your score increases, and the game continues.
4. If your guess is incorrect, the game ends, and your final score is displayed.

---

## Features
* **Randomized Entities**: Each round, new entities are fetched to keep the game engaging.
* **Simple User Input**: Guess by entering a single character (A or B).
* **Score Tracking**: Keep track of your score as you play.
* **Clean Interface**: The screen is cleared between rounds for a better user experience.

---

## Prerequisites
To run this game locally, you need:
* Python 3.6 or higher
* The following Python modules:
  * `os`
  * `random`
    
The project also relies on two additional files for its functionality:
* `art.py` - Contains ASCII art for the game's visuals.
* `functions.py` - Contains helper functions to:
  * Fetch a random account (`get_random_account`)
  * Format the account details (`format_account`)
  * Determine the winner based on follower count (`more_followers`).

---
## Setup and Installation
1. Clone this repository:
    ```shell
    git clone https://github.com/shrabhay/Higher-Lower.git
    cd higher-lower-game
    ```

2. Ensure all required files (`art.py`, `functions.py`) are present in the directory.
3. Run the game:
    ```shell
    python3 higher_lower_game.py
    ```

---

## Example Gameplay
```
Welcome to the Higher Lower Game!

Compare A: Instagram, a social media platform, with 346 million followers.
VS
Against B: Cristiano Ronaldo, a footballer, with 500 million followers.

Who has more followers? Type 'A' or 'B': b

You're right! Current score: 1.
```

---

## Future Enhancements
* Add more diverse entities to compare.
* Introduce difficulty levels based on the difference in follower counts.
* Implement a leaderboard to track high scores.

---

## License
This project is licensed under the MIT License. Feel free to use and modify the game for personal or educational purposes.
