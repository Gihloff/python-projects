# Represents a player (both user and computer) in the Go Fish game
class Player:
    RANK_ORDER = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
              '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    def __init__(self, name):
        self.name = name
        self.hand = []      # Cards in player's hand
        self.books = []     # Books (sets of 4 matching cards) player has

    # Adds card to player's hand
    def add_card(self, card):
        self.hand.append(card)

    # Removes all cards of a given rank from hand and returns them
    def remove_card_by_rank(self, rank):
        matching_cards = [card for card in self.hand if card.rank == rank]
        self.hand = [card for card in self.hand if card.rank != rank]
        return matching_cards
    
    # Implement a binary search algorithm to search for cards in sorted hands
    def has_rank(self, rank):
        return self.binary_search(rank) != -1
    
    # Checks hand for books(4 of a kind) and removes them.
    def check_for_books(self):
        rank_counts = {}
        for card in self.hand:
            rank_counts[card.rank] = rank_counts.get(card.rank, 0) + 1

        books_formed = []
        for rank, count in rank_counts.items():
            if count == 4:
                self.books.append(rank)
                self.hand = [card for card in self.hand if card.rank != rank]
                books_formed.append(rank)
            
        return books_formed
    
    # Returns a formatted string list of cards in hand
    def show_hand(self):
        return [str(card) for card in self.hand]
    
    # Returns the number of books collected by player
    def get_book_count(self):
        return len(self.books)
    
    def get_hand_ranks(self):
        return [card.rank for card in self.hand]
    
    # Sorts the player's hand using bubble sort by rank
    def sort_hand(self):
        # Bubble sort algorithm
        n = len(self.hand)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.RANK_ORDER[self.hand[j].rank] > self.RANK_ORDER[self.hand[j + 1].rank]:
                    # Swap cards if they are in the wrong order
                    self.hand[j], self.hand[j + 1] = self.hand[j + 1], self.hand[j]

    # Binary search to find a rank in hand
    def binary_search(self, target_rank):
        self.sort_hand()    # Make sure hand is sorted before searching
            
        low = 0
        high = len(self.hand) - 1

        while low <= high:
            mid = (low + high) // 2
            mid_rank = self.hand[mid].rank

            if self.RANK_ORDER[mid_rank] == self.RANK_ORDER[target_rank]:
                return mid  # Found
            elif self.RANK_ORDER[mid_rank] < self.RANK_ORDER[target_rank]:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1   # Not found