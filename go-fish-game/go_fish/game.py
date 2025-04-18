import random
import os
import time
from deck import Deck
from player import Player

# Function for clearing the terminal screen while running the game
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
# Function for pausing the game until the player presses Enter
def pause():
    input("\nPress Enter to continue...")

suit_symbols = {'Hearts': '♥', 'Diamonds': '♦', 'Clubs': '♣', 'Spades': '♠'}

# Function that formats a card string like '7 of Hearts' to '[7♥]'
def format_card(card_str):
    rank, _, suit = card_str.partition(" of ")
    return f"[{rank}{suit_symbols.get(suit, '?')}]"

# Main game logic and flow control for Go Fish
class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

        self.player = Player("Player 1")
        self.computer = Player("Computer")

        # Deal 7 cards to each player
        for _ in range(7):
            self.player.add_card(self.deck.draw_card())
            self.computer.add_card(self.deck.draw_card())

    # Game ends when all books are formed
    def is_game_over(self):
        total_books = self.player.get_book_count() + self.computer.get_book_count()
        return total_books == 13    # 1 book = 4 cards, 52 cards in deck. 52 cards / 4 cards = 13 books in a deck.
    
    def display_game_state(self):
        print("-" * 50)
        print("\nYour hand:")
        for card in self.player.show_hand():
            print(format_card(card))
        print()
        print("-" * 50)

        print(f"\nYour books: {self.player.get_book_count()}")
        print(f"Computer's books: {self.computer.get_book_count()}\n")
        print(f"Cards left in deck: {len(self.deck.cards)}\n")
        print("-" * 50)
        pause()
        clear_screen()
    
    def play(self):
        clear_screen()
        print("Welcome to Go Fish!\n")
        print("-" * 50)
        print()
        print()
        time.sleep(1)
        print("*" * 40)
        print("\nCreating standard 52-card deck...")
        time.sleep(2.5)
        print("\nShuffling deck...")
        time.sleep(3)
        print("\nDealing 7 cards to each player...\n")
        time.sleep(3)
        print("*" * 40)
        print("\n\nEnjoy playing 'Go Fish'!\n\n")
        print("-" * 50)
        pause()
        clear_screen()

        while not self.is_game_over():
            self.display_game_state()
            self.player_turn()
            if self.is_game_over():
                break
            self.display_game_state()
            self.computer_turn()

        self.display_winner()

    def player_turn(self):
        print("-" * 50)
        print("\nPlayer 1's turn!")
        print(f"Player 1's score: {self.player.get_book_count()}\n")
        print("-" * 50)
        print("\nYour hand:")
        for card in self.player.show_hand():
            print(format_card(card))
        print("")
        print("-" * 50)
        
        # Ask user for a rank
        valid_ranks = [card.rank for card in self.player.hand]
        rank = input("\nAsk for rank: ").strip().upper()

        while rank not in valid_ranks:
            print("Invalid rank. Pick a rank from your hand.")
            rank = input("Ask for rank: ").strip().upper()
        
        print()
        print("-" * 50)
        print(f"\nPlayer 1 asks Computer for {rank}s...\n")
        time.sleep(2.5)

        # search computer's hand for matching cards
        matches = [card for card in self.computer.hand if card.rank == rank]

        if matches:
            print(f"Computer gives: {len(matches)} {rank}(s) to Player 1.")
            cards_taken = self.computer.remove_card_by_rank(rank)
            for card in cards_taken:
                self.player.add_card(card)
        else:
            print("Computer says 'Go Fish!'")
            drawn_card = self.deck.draw_card()
            if drawn_card:
                print(f"You drew: {drawn_card}")
                self.player.add_card(drawn_card)
            else:
                print("Deck is empty, no card drawn.")
        
        print()
        print("-" * 50)

        # Check for new books in Player 1's hand
        self.player.check_for_books()

        pause()
        clear_screen()

    def computer_turn(self):
        print("-" * 50)
        print("\nComputer's turn!")
        print(f"Computer's score: {self.computer.get_book_count()}\n")
        print("-" * 50)
        print("\nComputer's hand is hidden.\n")
        print("\nComputer is thinking...\n")
        print("-" * 50)
        time.sleep(3)

        # Randomly choose a rank from computer's hand
        if not self.computer.hand:
            print("\nComputer has no cards!")
            return
        
        # The computer opponent should choose a random card from it's hand
        available_ranks = [card.rank for card in self.computer.hand]
        rank = random.choice(available_ranks)
        print(f"\nComputer asks Player 1 for {rank}s.\n")
        time.sleep(2)

        matches = [card for card in self.player.hand if card.rank == rank]

        if matches:
            print(f"Player 1 gives {len(matches)} {rank}(s) to Computer.")
            cards_taken = self.player.remove_card_by_rank(rank)
            for card in cards_taken:
                self.computer.add_card(card)
        else:
            print("Player 1 says 'Go Fish!'")
            drawn_card = self.deck.draw_card()
            if drawn_card:
                print(f"Computer draws a card.")
                self.computer.add_card(drawn_card)
            else:
                print("Deck is empty, no card drawn.")
        
        print()
        print("-" * 50)

        self.computer.check_for_books()

        pause()
        clear_screen()
    
    def display_winner(self):
        player_books = self.player.get_book_count()
        computer_books = self.computer.get_book_count()

        print("-" * 50)
        print("\nGame over!\n")
        print("-" * 50)

        if player_books > computer_books: 
            print(f"\nPlayer 1 wins with {player_books} books!\n")
        elif computer_books > player_books:
            print(f"\nComputer wins with {computer_books} books!\n")
        else:
            print("\nIt's a tie!\n")
        
        print("-" * 50)
        print(f"\nPlayer 1: {player_books} books")
        print(f"Computer: {computer_books} books")
        print()
        print("-" * 50)