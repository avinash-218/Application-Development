#black_jack

#importing modules
import bank_account as bank
import deck_of_cards as deck


class Black_jack:
 player_cards=[]
 dealer_cards=[]
 
 def get_bet_amount():			 #getting bet amount
  Black_jack.bet=''
  while not (Black_jack.bet.isdigit() and eval(Black_jack.bet)<=bank.Account.balance):
   Black_jack.bet=input('Enter your betting amount in numbers which is withdrawable.\n')
  Black_jack.bet=eval(Black_jack.bet)	#to store original bet amount
   
 def get_input():			#to ask for stay or hit
  move=''
  while move.upper()!='HIT' or move!='STAY':
   move=input('Enter your move-Hit or Stay')
  print('\n'*5)

 def assign_cards():			#to assign non-duplicate cards to player's hand and dealer's hand
  flag=1
  while flag!=4:
   temp=deck.Deck.draw_card_random()
   if temp not in Black_jack.player_cards and temp not in Black_jack.dealer_cards:
    if flag==1 or flag==3:
     Black_jack.player_cards.append(temp)
    elif flag==2:
     Black_jack.dealer_cards.append(temp)
    flag+=1
  Black_jack.dealer_cards.append('???')
 
 def black_jackpot(cards):							#to check if the game ends in natural blackjack for the given cards
  if ('A' in cards[0]) or ('A' in cards[1]):
   for i in deck.Deck.face[9:]:
    if i in cards[0] or i in cards[1]:
     return True								#the cards has a natural jackpot
  return False									#the cards does not have natural jackopt

 def  check_for_insurance():	#to check for insurance
  for i in deck.Deck.face[9:]:
   if i in Black_jack.dealer_cards[0] or 'A' in Black_jack.dealer_cards[0]:     #check if A,10,K,Q,J is present in the dealer's faced up card
    return True			#ask for insurance		
  return False			#insurance is not possible

 def ask_for_insurance():		#to ask if player needs to insure or not.
  inp=''
  while inp.upper()!='YES' and inp.upper()!='NO':
   inp=input('Do you want to insure yourself? Yes or No?\n')
  if inp.upper()=='YES':
   bank.Account.withdraw(Black_jack.bet/2)	#withdraw insurance bet 
  inp=inp.upper()
  return inp					#returning player's wish to insure or not to main

 def calc_sum(cards):			#change for ace value
  add=0
  for i in cards:
   val=i[i.index('-')+1:] 
   add+=deck.Deck.values[val]

#every player will decide that if their sum is 10 and his total excluding an ace less than 10,will choose one of the ace to hold a value of 11
#only one ace can posses the value 11 without getting busted
  for i in cards:		
   if i[i.index('-')+1:]=='A' and add<=11:
    add+=10
    break
  return add

 def display_cards():			#to display cards of player and dealer
  print('\t'*10,'-'*33)
  print('\t'*10,'|\t       Player\t\t |')
  print('\t'*10,'-'*33)

  print('\t'*10,'|','\t\t\t\t','|')
  for i in Black_jack.player_cards:
   print('\t'*10,'\t     ',i,'\t')
   print('\t'*10,'|','\t\t\t\t','|')

  print('\t'*10,'-'*32)

  print('\t'*10,'|','\t\t\t\t','|')
  for i in Black_jack.dealer_cards:
   print('\t'*10,'\t     ',i,'\t')
   print('\t'*10,'|','\t\t\t\t','|')

  print('\t'*10,'-'*33)
  print('\t'*10,'|\t       Dealer\t\t |')
  print('\t'*10,'-'*33)
 
 def hit_or_stay():			#ask player if he wish to hit or stay
  inp=''
  while inp.upper() != 'HIT' and inp.upper()!= 'STAY':
   inp=input('Hit or Stay ?\n')
  return inp.upper()

 def hit(cards):			#hit
  while True:
   temp=deck.Deck.draw_card_random()
   if temp not in Black_jack.player_cards and temp not in Black_jack.dealer_cards:
    cards.append(temp)
    return cards
 
 def bust(cards):			#bust
  if Black_jack.calc_sum(cards)>21:
   return 'BUST'

