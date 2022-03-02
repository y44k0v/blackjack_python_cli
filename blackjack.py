# https://stackoverflow.com/questions/31011395/python-print-unicode-character
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
    print("\n\n1 - new game\n2 - deal\n3 - exit\n\n")
    selection = int(input("select an option: "))
    if selection == 1:
      game = BlackJack()
    elif selection == 2: 
      game.deal()
      print([str(c) for c in game.deckBJ.taken])
    else:
      option = 0

play_blackjack()