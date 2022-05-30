#black_jack

#importing modules
from deck_of_cards import Deck 
from wallet import Wallet
import display

class Black_jack:
 dealer_cards=[]				
 #n-number of players
 #card_2-hidden card of dealer
 #natural-if natural for dealer T or F
 #insure- True or False if insure is possible or not
 split_indexes=[]	#list to store index of players who wish to split
 natural_indexes=[]	#list to store index of players who has natural
 insure_indexes=[]	#list t store index of players who insured
 double_indexes=[]	#list to store doubling players
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
  print('\n'*45)
  Black_jack.display_dealer_cards()							#to display dealer cards
  Black_jack.display_player_cards(players)							#to display player cards

 @staticmethod
 def display_dealer_cards():                    #to display dealer cards
  print('\t'*10,'-'*33)
  print('\t'*10,'  D E A L E R ')
  print('\t'*10,'-'*33)

  print('\t'*10,'|','\t\t\t\t','|')
  for i in Black_jack.dealer_cards:
   print('\t'*10,'\t     ',i)
   print('\t'*10,'|','\t\t\t\t','|')
  print('\t'*10,'-'*33)

 @staticmethod
 def display_player_cards(players):                     #to display players' cards
  for i in range(Black_jack.n):
   if i in Black_jack.split_indexes:			#splitted players(print both hands one after other)
    for k in range(2):				#two loops for two hands
     hand=['Left','Right']	#used for printing purpose
     print('\t'*10,' ',' '.join(players[i].name),"'s",hand[k],'Hand')
     print('\t'*10,'-'*33)
           
     print('\t'*10,'|','\t\t\t\t','|')
     for j in players[i].cards:
      print('\t'*10,'\t     ',j)
      print('\t'*10,'|','\t\t\t\t','|')
     print('\t'*10,'-'*33)
     players[i].swap_split()			#swap hands
   else:				#non splitted players
    print('\t'*10,' ',' '.join(players[i].name))
    print('\t'*10,'-'*33)
           
    print('\t'*10,'|','\t\t\t\t','|')
    for j in players[i].cards:
     print('\t'*10,'\t     ',j)
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
   if (i in Black_jack.dealer_cards[0]) or ('A' in Black_jack.dealer_cards[0]):     #check if A,10,K,Q,J is present in the dealer's faced up card
    Black_jack.insure=True
    return None
  Black_jack.insure=False

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
  Black_jack.add=0
  for i in Black_jack.dealer_cards:
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
   print(self.name,',do you want to insure yourself? Yes or No?')
   self.status=input().upper()
   print()
  if self.status=='YES':
   if Wallet.balance(self)< self.bet/2:			#if wallet balance is insufficient
    print('Your balance is low.Add money to your casino wallet')
    recharge=''
    while not (recharge.isdigit() and eval(recharge)>=self.bet/2):	#recharge atleast to take this insurance
     recharge=input('Enter money atleast sufficient to recharge your casino wallet\n')
    print('\nRecharging...')
    Wallet.deposit(self,eval(recharge))		#recharging
   Wallet.withdraw(self,self.bet/2)			#withdrawing insurance amount
   self.change_status('INSURE')
  else:
   self.change_status('NOINSURE')

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
  self.status=''
  while self.status != 'HIT' and self.status != 'STAY':
   print(self.name,end=', ')
   self.status=input('Hit or Stay ?\n').upper()
 
 def hit(self):			#hit once
  self.cards.append(Deck.draw_card_random())

 def hit_till_stay(self,players):		#hit continuously until player wishes to stay
  while True:
   self.hit_or_stay()                           #to ask hit or stay
   if self.status=='STAY':
    self.change_status('STAY')
    break
   self.hit()
    
   Black_jack.display_cards(players)                  #to display cards
    
   if self.stop_21()==True:                     #if tot=21
    input('Press Enter to continue\n') 
    self.change_status('STAY')
    break                                             #no more hits
    
   self.bust()
   if self.status=='BUST':                      #if player is bust
    print('You are busted')
    input('Press Enter to continue\n')
    self.status='END'
    break

 def stop_21(self):		#to stop if total becomes 21
  return self.calc_sum()==21		#True if tot=21 else False

 def bust(self):			#bust
  if self.calc_sum()>21:
   self.status="BUST"

 def change_status(self,status):
  self.status=status

 def check_split(self):			#check if split is possible
  if self.cards[0][self.cards[0].index('-')+1:]==self.cards[1][self.cards[1].index('-')+1:]:
   return True

 def ask_split(self):			#check and ask the player if he wish to split pair
  while (self.status!='YES' and self.status!='NO'):
   print(self.name,end=', ')
   self.status=input('Do you wish to split?, Yes or No?\n').upper()
  if self.status=='YES':
   if Wallet.balance(self)< self.bet:			#if wallet balance is insufficient
    print('Your balance is low.Add money to your casino wallet')
    recharge=''
    while not (recharge.isdigit() and eval(recharge)>=self.bet):	#recharge atleast to split
     recharge=input('Enter money atleast sufficient to recharge your casino wallet\n')
    print('Recharging...')
    Wallet.deposit(self,eval(recharge))         #recharging
   Wallet.withdraw(self,self.bet)                     #withdrawing split amount
   self.change_status('SPLIT')			#change status to "SPLIT"
   self.cards_split=[self.cards[0]]		#another hand
   self.status_split='SPLIT'			#assigning status of another hand as "PLAY"
   self.add_split=0				#assigning add of another hand as 0
   self.cards=[self.cards[0]]			#removing second element
  else:
   self.change_status('NOSPLIT')

#two hands of player after split differs only in status,total,cards
 def swap_split(self):					#swap both hands' cards ,status,total(add)
  self.cards,self.cards_split=self.cards_split,self.cards	#swap cards
  self.status,self.status_split=self.status_split,self.status	#swap status
  self.add,self.add_split=self.add_split,self.add		#swap total(add)

 def split(self,players):
  Black_jack.display_cards(players)           #to display cards
  for k in range(2):                                  #two loops for two hands
   hand=['Left','Right']                      #just to display
   print(self.name,',you are now playing your',hand[k],'hand')
    
   if 'A' in self.cards[0]:                             #if the two cards are Aces player gets only one card for each
    print('Since you got an ACE ,you can hit only once')
    display.pause()                           #pause
    self.hit()                  #one hit
    self.calc_sum()
    if k==1:
     self.swap_split()
     Black_jack.display_cards(players)
     self.swap_split()
    else:
     Black_jack.display_cards(players)
      
    self.black_jackpot()    
    if self.status=='NATURAL':                          #to check if the player has a natural after splitting
     print('Congrajulations!!!This hand has a natural.')
     Wallet.deposit(self,self.bet*2)              #only bet amount
     Wallet.display(self)                               #display wallet details
     self.change_status('END')                          #change status to "END"
    else:
     self.change_status('STAY')
#Note:Player who splitted(A-A) bet can't get busted(check the maximum total he can get(only 21 is possible)
   else:                                                      #if no Ace,hit until stay
    while True:
     self.hit_or_stay()
     if self.status=='STAY':
      self.change_status('STAY') 
      break
     self.hit()
     
     if k==1:
      self.swap_split()
      Black_jack.display_cards(players)
      self.swap_split()
     else:
      Black_jack.display_cards(players)
     
     if self.stop_21()==True:
      input('Press Enter to continue\n')
      self.change_status('STAY')
      break
      
     self.bust()
     if self.status=='BUST':
      print('You are busted')
      input('Press Enter to continue\n')
      self.change_status('END')
      break
           
#to prevent displaying cards -collapsing hand error-logically correcting
    if k==1:
     self.swap_split()
     Black_jack.display_cards(players)
     self.swap_split()
          
    if self.stop_21()==True:                           #if tot=21
     self.change_status('STAY')
       
    self.bust()
    if self.status=='BUST':                            #if player is bust
     print('You are busted so you Lost this hand.')
     self.change_status('END')                         #change status to "END"
           
   self.swap_split()                                            #swap both hands' details(status,card,add)
      
 def check_double_down(self):			#check if double down is possible
  self.calc_sum()				#calling calc_sum function to calc total of player
  if self.add in [9,10,11]:
   return True 

 def ask_double_down(self):			#ask player if he wishes to double down
  self.status=''
  while (self.status!='YES' and self.status!='NO'):
   print(self.name,end=', ')
   self.status=input('Do you wish to double your bet?, Yes or No?\n').upper()
  if self.status=='YES':
   if Wallet.balance(self) < self.bet:		#if wallet balance is insufficient
    print('Your balance is low.Add money to your casino wallet')
    recharge=''
    while not (recharge.isdigit() and eval(recharge)>=self.bet):      #recharge atleast to double the bet
     recharge=input('Enter money atleast sufficient to recharge your casino wallet\n')
    print('Recharging...')
    Wallet.deposit(self,eval(recharge))         #recharging
   Wallet.withdraw(self,self.bet)		#withdraw another bet(for double down)
   self.change_status("DD")				#change status to DD(double down)
  else:
   self.change_status=("NDD")				#change status to NDD(no double down)
 
 def double_down(self):					#for double down players 
  print(self.name,',since you have choosen to Double Down...you can draw only one card')
  input('Press Enter to Hit\n')               #pause
  self.hit()			#player drawing one card
  self.change_status('STAY')                     #change status
 
 @staticmethod
 def check_with_dealer(players):			#check players total with dealer
  for i in range(Black_jack.n):
   players[i].calc_sum()
   if i in Black_jack.double_indexes:	#doubled players
    if players[i].add>Black_jack.add:		#won
     print(players[i].name,", you won")
     print('Also, since you have doubled your bet, your bet amounts and amount you won will be credited to your account')
     Wallet.deposit(players[i],players[i].bet*4)
    elif players[i].add<Black_jack.add:		#lose
     print(players[i].name,", you lose your doubled bet")
    else:					#tie
     print(players[i].name,", you tie with the dealer")
     print('So your bet amount(considering your doubled amount) will be refunded to your wallet account soon!!')
     Wallet.deposit(players[i],players[i].bet*2)
          
   elif i in Black_jack.split_indexes:	#splitted players
    hand=['Left','Right']
    for k in range(2):				#two loops for two hands
     if players[i].status=='STAY':		
      if players[i].add>Black_jack.add:			#won hand	
       print(players[i].name,", you won your",hand[k],'hand')
       print('Your bet amounts along with the amount you won in the bet will be credited to your wallet account soon!!!')
       Wallet.deposit(players[i],players[i].bet*2)
      elif players[i].add<Black_jack.add:		#lost hand
       print(players[i].name,", you lose your",hand[k],'hand')
      else:						#did draw hand
       print(players[i].name,", your",hand[k],"hand tie up with dealer")
       print('So your bet amount for this hand will be refunded to your wallet account soon!!!')
       Wallet.deposit(players[i],players[i].bet)
     players[i].swap_split()       
            
   else:				#regular players
    if players[i].status=='STAY':
     if players[i].add>Black_jack.add:			#won 
      print(players[i].name,", you won")
      print('Your bet amounts and amount you won will be credited to your account')
      Wallet.deposit(players[i],players[i].bet*2)
     elif players[i].add<Black_jack.add:			#lose
      print(players[i].name,", you lose")
     else:						#tie
      print(players[i].name,", you tie up with the dealer")
      print('So your bet amount will be refunded to your wallet account soon!!!')
      Wallet.deposit(players[i],player[i].bet)
