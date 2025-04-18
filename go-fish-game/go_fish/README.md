
# Go Fish – Python Project

A fun, text-based implementation of the classic card game **Go Fish.** built with Python! Play against a computer opponent, collect books (sets of four cards of the same rank), and enjoy a fun and clear terminal output.


## 🎮 How to Play

- You and the computer are each dealt 7 cards from a standard 52-card deck.
- Take turns asking your opponent for cards of a specific rank.
- If they have any cards of that rank, they must give them to you. You get another turn.
- If they don’t, they say "Go Fish!" and you draw a card from the deck.
- When a player collects four cards of the same rank, they earn a book.
- The game ends when all 13 books have been collected.
- The player with the most books at the end wins!

## 🔧 Features

- Complete playable version of Go Fish
- Supports 2 players (1 human and 1 AI opponent)
- Full implementation of Go Fish rules
- Fisher-Yates shuffle algorithm for deck randomness
- Text-based command-line interface with clear formatting
- Bubble sort and binary search used to demonstrate algorithm concepts
- Hidden computer hand for fair gameplay
- Clear game state display and instructions

## 📂 Project Structure

```
go_fish/
│
├── card.py       # Card class to represent a playing card
├── deck.py       # Deck class that builds and shuffles a 52-card deck
├── player.py     # Player class representing both the user and the computer
├── game.py       # Game class containing main game logic and flow
├── main.py       # Entry point that launches the game
└── README.md     # You're here!
```

## ▶️ Setup

1. Make sure you have Python 3 installed.
2. Clone this repository or download the files.

```
git clone https://github.com/atlas-school-classroom/cs1500-assignment-go-fish-Gihloff.git
cd go_fish
```

3. Run the game using the command:

```
python main.py
```

## 💡 Educational Value
This project helps practice:
- Object-oriented programming (OOP) concepts
- Sorting and searching algorithms (Bubble Sort, Binary Search)
- Game design with state tracking
- Input validation and user interaction
- Working with multiple Python files and modules
Great for beginners learning Python in a hands-on, fun way!

# 🧠 Future Improvements
- GUI version using Tkinter or PyGame
- Multiplayer support
- Smarter computer AI
- Score tracking across multiple rounds
- Add load/save game functionality

