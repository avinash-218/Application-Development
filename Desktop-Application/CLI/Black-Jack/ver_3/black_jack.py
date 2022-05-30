#black_jack

#importing modules
from deck_of_cards import Deck 
from wallet import Wallet

class Black_jack:
 dealer_cards=[]				
 #n-number of players
 #card_2-hidden card of dealer
 #natural-if natural for dealer
 #insure-CAN or CANT if insure is possible or not
 split_indexes=[]	#list to store index of players who wish to split
 add=0			#to store total of Dealer's card

 def __init__(self):
  self.cards=[]

#static methods 

 @staticmethod					
 def get_players_number():                      #to get number of players
  Black_jack.n=''
  while not(Black_jack.n.isdigit() and eval(Black_jack.n) in [1,2,3,4,5]):
   Black_jack.n=input('Enter number of players (1-5)\n')
  Black_jack.n=eval(Black_jack.n)

 @staticmethod
 def display_cards(players):                            				#to display cards
  Black_jack.display_dealer_cards()							#to display dealer cards
  Black_jack.display_player_cards(players)							#to display player cards

 @staticmethod
 def display_dealer_cards():                    #to display dealer cards
  print('\t'*10,'-'*33)
  print('\t'*10,'| D E A L E R\t\t\t |')
  print('\t'*10,'-'*33)

  print('\t'*10,'|','\t\t\t\t','|')
  for i in Black_jack.dealer_cards:
   print('\t'*10,'\t     ',i,'\t')
   print('\t'*10,'|','\t\t\t\t','|')
  print('\t'*10,'-'*33)

 @staticmethod
 def display_player_cards(players):                     #to display players' cards
  for i in range(Black_jack.n):
   if i in Black_jack.split_indexes:			#splitted players(print both hands one after other)
    for i in range(2):				#two loops for two hands
     print('\t'*10,' ',' '.join(players[i].name),'\t\t ')
     print('\t'*10,'-'*33)
           
     print('\t'*10,'|','\t\t\t\t','|')
     for j in players[i].cards:
      print('\t'*10,'\t     ',j,'\t')
      print('\t'*10,'|','\t\t\t\t','|')
     print('\t'*10,'-'*33)
     players[i].swap_split()			#swap hands
   else:				#non splitted players
    print('\t'*10,' ',' '.join(players[i].name),'\t\t ')
    print('\t'*10,'-'*33)
           
    print('\t'*10,'|','\t\t\t\t','|')
    for j in players[i].cards:
     print('\t'*10,'\t     ',j,'\t')
     print('\t'*10,'|','\t\t\t\t','|')
    print('\t'*10,'-'*33)

 @staticmethod
 def assign_dealer_cards():                                             #assign cards for dealer
  Black_jack.dealer_cards.extend([Deck.draw_card_random(),'???'])       #one card hidden
  Black_jack.card_2=Deck.draw_card_random()                             #to assign the hidden card of dealer to card_2 attribute

 @staticmethod
 def dealer_black_jackpot():
  if ('A' in Black_jack.dealer_cards[0]) or ('A' in Black_jack.card_2):
   for i in Deck.face[9:]:
    if (i in Black_jack.dealer_cards[0] or i in Black_jack.card_2):      #the cards has a natural or not
     Black_jack.natural=True
     Black_jack.dealer_cards[1],Black_jack.card_2=Black_jack.card_2,Black_jack.dealer_cards[1]		#if dealer has a natural,his cards must be shown no matter what,so unhiding card  
     return None
  Black_jack.natural=False  

 @staticmethod
 def check_for_insurance():                                                     #to check for insurance
  for i in Deck.face[9:]:
   if i in Black_jack.dealer_cards[0] or 'A' in Black_jack.dealer_cards[0]:     #check if A,10,K,Q,J is present in the dealer's faced up card
    Black_jack.insure='CAN'
  Black_jack.insure='CANT'

 @staticmethod
 def check_status(players):			#to check if atleast one player(or another hand of a player who had split) did not end his game
  for i in range(Black_jack.n):
   if players[i].status!='END':			#check all players
    return True					#returns TRUE if atleast one player has to play
  
  for i in Black_jack.split_indexes:		#to check other hands of splitted players
   if players[i].split_status!='END':		#check other hands
    return True					#returns True if atleast one-other hand of a player has to play

 @staticmethod
 def dealer_sum():			#to calc total of dealer and return
  for i in range(Black_jack.dealer_cards):
   val=i[i.index('-')+1:] 
   Black_jack.add+=Deck.values[val]
    


 def get_bet_amount(self):			 #getting bet amount
  self.bet=''
  while not(self.bet.isdigit() and eval(self.bet)>0 and eval(self.bet)<=self.balance):
   self.bet=input('Enter your betting amount in numbers which is withdrawable.\n')
  self.bet=eval(self.bet)	#to store original bet amount
   
 def black_jackpot(self):						#to check if there is a natural for the given cards
  if ('A' in self.cards[0]) or ('A' in self.cards[1]):
   for i in Deck.face[9:]:
    if (i in self.cards[0] or i in self.cards[1]):			#the cards has a natural or not
     self.change_status('NATURAL')

 def change_status(self,status):						#change status from "PLAY" to player's position(end,insure,hit,stay,etc...)
  self.status=status

 def ask_for_insurance(self):							#to ask if player needs to insure or not.
  self.status=''
  while self.status!='YES' and self.status!='NO':
   self.status=input('Do you want to insure yourself? Yes or No?\n').upper()
  if self.status=='YES':
   Wallet.withdraw(self,self.bet/2)						#withdraw insurance bet 
   self.status='INSURE'
  else:
   self.status='NOINSURE'

 def calc_sum(self):							#change for ace value
  self.add=0
  for i in self.cards:
   val=i[i.index('-')+1:] 
   self.add+=Deck.values[val]

#every player will decide that if their sum is 10 and his total excluding an ace less than 10,will choose one of the ace to hold a value of 11
#only one ace can posses the value 11 without getting busted
  for i in self.cards:		
   if i[i.index('-')+1:]=='A' and self.add<=11:
    self.add+=10
    break
  return self.add
 
 def hit_or_stay(self):			#ask player if he wish to hit or stay
  while self.status != 'HIT' and self.status != 'STAY':
   self.status=input('Hit or Stay ?\n').upper()
 
 def hit(self):			#hit
  self.cards.append(Deck.draw_card_random())
 
 def stop_21(self):		#to stop if total becomes 21
  return self.calc_sum(self.cards)==21		#True if tot=21 else False

 def bust(self):			#bust
  if self.calc_sum(self.cards)>21:
   self.status="BUST"

 def check_split(self):			#check if split is possible
  if self.cards[0]==self.cards[1]:
   self.ask_split()			#ask player wish to split or not

 def ask_split(self):			#check and ask the player if he wish to split pair
  if self.cards[0]==self.cards[1]:		#split is possible
   self.split=''
   while not(self.split=='YES' and self.split=='NO'):
    self.split=input('Do you wish to split?, Yes or No?').upper()
  if self.split=='YES':
   self.change_status('SPLIT')			#change status to "SPLIT"
   Wallet.withdraw(self,self.bet)		#placing another bet on other half
   self.cards_split=[self.cards[1]] 		#copying second card to another hand
   self.status_split='PLAY'			#assigning status of another hand as "PLAY"
   self.add_split=0				#assigning add of another hand as 0
   self.cards.pop()				#removing second card
  else:
   self.change_status('NOSPLIT')

#two hands of player after split differs only in status,total,cards
 def swap_split(self):					#swap both hands' cards ,status,total(add)
  self.cards,self.cards_split=self.cards_split,self.cards	#swap cards
  self.status,self.status_split=self.status_split,self.status	#swap status
  self.add,self.add_split=self.add_split,self.add		#swap total(add)

 def check_double_down(self):			#check if double down is possible
  self.calc_sum()				#calling calc_sum function to calc total of player
  if self.add in [9,10,11]:
   self.ask_double_down()			#call method that asks user if he wish to double down

 def ask_double_down(self):			#ask player if he wishes to double down
  self.double_down=''
  while not(self.double_down=='YES' and self.double_down=='NO'):
   self.double_down=input('Do you wish to split?, Yes or No?').upper()
  if self.double_down=='YES':
   Wallet.withdraw(self,self.bet)		#withdraw another bet(for double down)
   self.status="DD"				#change status to DD(double down)
  else:
   self.status="NDD"				#change status to NDD(no double down)
 
 def check_with_dealer(self):			#check players total with dealer
  if self.add>Black_jack.add:	#player wins
   print('Congrajulation!!! You Win')
   if self.status=='DD':		#if player doubled his bet
    print('Also since you have doubled yuor bet,you win twice the doubled bet...')
    Wallet.deposit(self,self.bet*4)	#4 times original bet
   else:				#splitted players and stayed players
    Wallet.deposit(self,self.bet*2)	#2 times the original bet
   self.change_status('END')		#change status
  elif self.add<Black_jack.add:	#players lose
   print('You Lose')
  else:				#tie
   display.match_draw()
   if self.status=='DD':	#if player doubled his bet
    print('Since you have also doubled your bet,you are refunded with doubled amount')
    Wallet.deposit(self,self.bet*2)	#refunded
   else:				#splitted and stayed players
    Wallet.deposit(self,self.bet)	#refunded
   self.change_status('END')		#change status

 
