#Justin Moore -- Deck of Cards
import random
class Card:
    def __init__(self, rank, suit):
                self.rank = rank
                self.suit = suit
#Builds the deck of cards, assigning attributes to the cards to be called for the application.
class Deck:
    def __init__(self):
        self.ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.reset()

    def reset(self):
        self.deck = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        if len(self.deck) == 0:
             return None
        return self.deck.pop()

    def count(self):
         return len(self.deck)
#Heading for the application.
print("Welcome to the Card Dealer!")
print("There is a Stack of 52 cards.")
#Create a Deck of Cards.
deck = Deck()
#Shuffle the Deck of Cards.
deck.shuffle()
#Ask user for the number of cards to be dealt.
num_cards_to_deal = int(input("How Many Cards Would You Like to Deal? "))
dealt_cards = []
#Deal the requested amount of cards.
for _ in range(num_cards_to_deal):
    card = deck.deal()
    if card is not None:
          dealt_cards.append(f"{card.rank} of {card.suit}")
    else:
        print("No More Cards in the Deck.")

        break
#Display the dealt cards.
if dealt_cards:
     print("Dealt cards:")
     for card in dealt_cards:
          print(card)
#Display remaining card count.
remaining_count = deck.count()
print(f"Remaining Cards in the Deck:  {remaining_count}")

print("Good Luck!")