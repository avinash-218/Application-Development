#deck_of_cards

#importing modules
import random

class Deck():
 suits=('Diamonds','Hearts','Spades','Clubs')
 face=('A','2','3','4','5','6','7','8','9','10','Jack','Queen','King')
 values={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Jack':10,'Queen':10,'King':10}

 def draw_card_random():
  Deck.card_suit=Deck.suits[random.randint(0,3)]
  Deck.card_face=Deck.face[random.randint(0,12)]
  return (str(Deck.card_suit)+'-'+str(Deck.card_face))

 def value_of_the_card():
  return Deck.values[Deck.card_face]


