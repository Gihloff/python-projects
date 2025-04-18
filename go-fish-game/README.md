[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/mxnkxPd8)
# Assignment: Go Fish

## Introduction

In this assignment, you'll apply the Python programming skills and DSA concepts you've learned throughout this course to build a complete, playable implementation of the classic card game "Go Fish." This project brings together multiple important concepts—from implementing shuffle algorithms and search techniques to designing object-oriented class structures and managing game state. You'll create a command-line application where players can compete against a computer opponent. By completing this project, you'll demonstrate your ability to translate theoretical computer science concepts into practical, working software.

## Learning Objectives

- Implement a card shuffling algorithm (Fisher-Yates shuffle)
- Implement search algorithms for card matching
- Practice working with data structures
- Build a complete interactive program with game logic

## Project Requirements

### 1. Card and Deck Implementation

- Create a `Card` class with suit and rank attributes
- Implement a `Deck` class that contains a standard 52-card deck
- Create a Fisher-Yates shuffle algorythm method for shuffling the deck

### 2. Player Implementation

- Design a `Player` class (for both human and computer players)
- Implement methods to:

  - Add cards to hand
  - Remove cards from hand
  - Search for matching cards in hand
  - Form and count "books" (sets of 4 matching cards)

### 3. Game Logic

- Implement the rules of Go Fish:
  - Deal 7 cards to each player initially (2 players)
  - Players take turns asking for cards of a specific rank
  - If opponent has requested cards, they must give them all
  - If not ("Go Fish"), player draws from the deck
  - When a player collects all 4 cards of one rank, they form a "book"
  - Game ends when all books are formed
  - Winner has the most books

### 4. Algorithm Requirements

- Implement a sorting algorithm of your choice to sort the hunan and ai player's hands
- Implement a binary search algorithm to search for cards in sorted hands
- Implement the Fisher-Yates shuffle algorythm

### 5. Computer AI

- The computer opponent should choose a random card from it's hand

### 6. User Interface

- Create a text-based interface in the command line
- Display clear game state information
- Show the player's hand, number of books, and remaining cards in deck
- Provide win/loss notification at the end

### Output examples

#### Player's turn

```plaintext
Player 1's turn!
Player 1's score: 0
Your hand:
2 of Diamonds
3 of Clubs
8 of Clubs
9 of Spades
A of Clubs
J of Clubs
Q of Spades
Ask for a rank: Q
Player 1 asks Computer for Qs.
Computer gives 1 Q(s) to Player 1.
```

#### Computer's turn

```plaintext
Computer's turn!
Computer's score: 0
Computer's hand is hidden.
Computer is thinking...
Computer asks Player 1 for 8s.
Player 1 says 'Go Fish!'
```

#### Game Over

```plaintext
Game over! Player 1 wins with 7 books!
Player 1: 7 books
Computer: 6 books
```

### Example project structure

```plaintext
go_fish/
├── README.md
├── main.py
├── card.py
├── deck.py
├── player.py
└── game.py
```
