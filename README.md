# Simple Blackjack game in python for the cli

#### to execute just run the file and follow the instructions


```hcl
BlackJack y44k0v$ python3 blackjack.py 


Select 1 for new game, 2 for deal and  3 for exit

enter option: 1


Select 1 for new game, 2 for deal and  3 for exit

enter option: 2

Total :4
['[♦️ 4]']


Select 1 for new game, 2 for deal and  3 for exit

enter option: 2

Total :6
['[♦️ 4]', '[♥️ 2]']


Select 1 for new game, 2 for deal and  3 for exit

enter option: 2

Total :11
['[♦️ 4]', '[♥️ 2]', '[♥️ 5]']


Select 1 for new game, 2 for deal and  3 for exit

enter option: 2
************************
        YOU WIN!!
************************

Total :21
['[♦️ 4]', '[♥️ 2]', '[♥️ 5]', '[♠️ K]']


Select 1 for new game, 2 for deal and  3 for exit

enter option: 1


Select 1 for new game, 2 for deal and  3 for exit

enter option: 2

Total :4
['[♥️ 4]']


Select 1 for new game, 2 for deal and  3 for exit

enter option: 2

Total :7
['[♥️ 4]', '[♣️ 3]']


Select 1 for new game, 2 for deal and  3 for exit

enter option: 2

Total :17
['[♥️ 4]', '[♣️ 3]', '[♦️ K]']


Select 1 for new game, 2 for deal and  3 for exit

enter option: 2

Total :20
['[♥️ 4]', '[♣️ 3]', '[♦️ K]', '[♠️ 3]']


Select 1 for new game, 2 for deal and  3 for exit

enter option: 2


!!!YOU LOSE!!!

Total :24
['[♥️ 4]', '[♣️ 3]', '[♦️ K]', '[♠️ 3]', '[♣️ 4]']


Select 1 for new game, 2 for deal and  3 for exit

enter option: 
```
#### Only implemented single player, with manual dealing.

```python
# Blackjack card
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.V = ["A", "2", "3" , "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"][value-1]
        self.S = ["♥️","♦️","♠️","♣️"][suit-1] # 1,2,3,4 = ♥️♦️♠️♣️

    def __str__(self):
          return f"[{self.S} {self.V}]"

    def __repr__(self):
          return '\n┌───────┐' + \
                f'\n| {self.V:<2}    |' + \
                '\n|       |'+ \
                f'\n|   {self.S}  |' + \
                '\n|       |' + \
                f'\n|    {self.V:>2} |' + \
                '\n└───────┘' 
        
    def getValue(self):
      return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10 ,10 ][self.value-1]
    
    def __add__(self, other):
      if isinstance(other, Card):
          return self.getValue() + other.getValue()
      else:
          return self.getValue() + other
    
    __radd__ = __add__
    
    
from random import shuffle
# Blackjack deck implementation
class Deck():

  def __init__(self, name):
    self.name = name
    self.cards = [Card(i,j) for j in range(1,5) for i in range(1,14)]
    self.stack = 52
    self.taken = []
    self.picked = []

  def __str__(self):
    d = []
    for i in self.cards:
      d.append(str(i))
    return str(d[:13])+"\n"+str(d[13:26])+"\n"+str(d[26:39])+"\n"+str(d[39:52])+str(f"\nNumber of cards: {self.stack}")

  def shuffle(self):
    shuffle(self.cards)
    return self.cards
  
  def reorder(self):
    self.cards = [Card(i,j) for j in range(1,5) for i in range(1,14)]

  def pick(self, num):
    if self.stack - num >= 0:
      self.picked = []
      for i in range(num):
        self.picked.append(self.cards.pop())
      self.stack -= num
      self.taken += self.picked
      return self.picked
    else:
      print("No more cards")
      
# Blackjack game implementation
class BlackJack():

   def __init__(self):
     self.playerC = []
     self.deckBJ = Deck("blackjack")
     self.deckBJ.shuffle()
     
     self.cnt = 0


   def deal(self):
    total = 0
    self.playerC.append(self.deckBJ.pick(1))
    for card in self.playerC:
      if total <= 10 and card[0].getValue() == 1:
        total += card[0].getValue()+10
      else:
        total += card[0].getValue()
      self.cnt += 1
      if total ==21:
        print("\033[1;32m************************\n\tYOU WIN!!\n************************")
      elif total>21:
        print("\u001b[31m\n\n!!!YOU LOSE!!!")
    print(f"\u001b[0m\nTotal :{total}")
    return self.playerC


def play_blackjack():
  option = 1
  
  while(option):
    print("\n\nSelect 1 for new game, 2 for deal and  3 for exit\n")
    selection = int(input("enter option: "))
    if selection == 1:
      game = BlackJack()
    elif selection == 2: 
      game.deal()
      print([str(c) for c in game.deckBJ.taken])
    else:
      option = 0

play_blackjack()

```
