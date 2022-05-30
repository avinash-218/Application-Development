#game.py

#importing modules and classes
import display
from wallet import Wallet
from black_jack import Black_jack
from deck_of_cards import Deck

def main():
 display.welcome()                                              #welcome note
 display.intro()                                                #intro about black jack

 Black_jack.get_players_number()				#input number of palyers

 players=[]										#to store list of players
 print('\nAll players should open their wallet accounts in casino to play this game')
 for i in range(Black_jack.n):
  players.append(Black_jack())								#appending n objects to the players list
  players[i].status="PLAY"								#assigning status as play
  print('\nPlayer',i+1,':')	
  print('-'*10)
  Wallet.open_account(players[i])							#to open account
 for i in range(Black_jack.n):
  Wallet.display(players[i])

 print('\nPlayers should enter your bet amount before playing:\n')
 for i in range(Black_jack.n):
  print('\n',players[i].name,':')
  print('-'*10)
  players[i].get_bet_amount() 								#get bet amount for all players
  Wallet.withdraw(players[i],players[i].bet)						#withdraw bet amount
  
 print("\nPlayers' Wallet Details:")							#print wallet details
 print('-'*25,end='')
 for i in range(Black_jack.n):
  Wallet.display(players[i])  

#first two cards
 Black_jack.assign_dealer_cards()							#assign dealer cards
 for i in range(Black_jack.n):
  players[i].cards=list()								#creating list for players' cards
  for j in range(2):
   players[i].hit() 									#assign cards for players

 print('Dealer is distributing the cards.....')
 display.pause()					#pause
 Black_jack.display_cards(players)

 for i in range(Black_jack.n):
  players[i].black_jackpot()		#check players who has natural
  if players[i].status=='NATURAL':
   Black_jack.natural_indexes.append(i)		#store index of players who has natural
 
#check if insurance is possible(i.e,if there is a possibility for a natural for dealer
 Black_jack.check_for_insurance()
 if Black_jack.insure==True:	#if dealer has possibility for a natural
  for i in range(Black_jack.n):
   if i in Black_jack.natural_indexes:	#players with natural
    print(players[i].name,',Congrajulations!!!You have a natural.Wait for the dealer to turn up his card') 
    players[i].status='END'						#change status to END
   else:					#players with no natural
    players[i].ask_for_insurance()	#ask if players wish to insure themselves
    if players[i].status=='INSURE':
     Black_jack.insure_indexes.append(i)	#store index of players who insured

#check if dealer has natural
 Black_jack.dealer_black_jackpot()
#dealer with natural
 if Black_jack.natural==True:		#if dealer has natural
  Black_jack.dealer_cards[1]=Black_jack.card_2		#unhiding the card
  Black_jack.display_cards(players)			#display cards after unhiding dealer's card cuz game end once dealer has a natural
  for i in range(Black_jack.n):
  #players with natural
   if i in Black_jack.natural_indexes:		#players with natural ties with dealer since dealer also has natural
    print(players[i].name,',since the dealer too has natural, you ties up with dealer')
    print('Bet amount will be refunded')
    Wallet.deposit(players[i],players[i].bet) 				
  #players without natural
   else:					#players without natural
    if i in Black_jack.insure_indexes:						#non natural players with insurance will get insured bet
     print(players[i].name,",since the dealer has natural and you don't, you lost your bet amount")
     print('But since you have insured yourself, you won your insured bet.The insured bet amount will be refunded soon!')
     Wallet.deposit(players[i],players[i].bet/2)				
    else:								#non natural players without insurance
     print(players[i].name,",since the dealer has natural and you don't, you lost your bet amount")
     print('You should have insured yourself!!!')
   display.pause()
  return None									#game ends
   
#dealer without natural but insure possible
 elif Black_jack.insure==True and Black_jack.natural==False:					#if dealer has no natural
  for i in range(Black_jack.n):
   if i in Black_jack.natural_indexes:		#natural players win 1.5 of the bet and ends the game
    print(players[i].name,",since the dealer don't have natural,you win the bet!")
    print('One and a half of your bet amount will be credited to your wallet account now')
    Wallet.deposit(players[i],players[i].bet*1.5)
   else:					#non natural players
    if i in Black_jack.insure_indexes:			#non natural insured players lose their insured bet
     print(players[i].name,",since the dealer don't have natural,you can continue your game")
     print("Also since you have insured,you lose your insured bet")
    else:						#non natural non insured players continue their game
     print(players[i].name,",since the dealer don't have natural,you can continue your game")
   display.pause()
       
 if Black_jack.natural==False:	#if dealer has no insurance(no natural obviously)
  for i in range(Black_jack.n):
   if players[i].status!='END' and i in Black_jack.natural_indexes:	#natural players win naturally
    print(players[i].name,",since the dealer don't have natural,you win the bet!")
    print('One and a half of your bet amount will be credited to your wallet account now')
    Wallet.deposit(players[i],players[i].bet*1.5)
   else:				#non natural players should choose to double down or split or hit
    if players[i].check_double_down() == True:	
     players[i].ask_double_down()			#ask players who satisfy doubling conditions
     if players[i].status=='DD':
      Black_jack.double_indexes.append(i)			#store index in a list of players who doubles their bet
      players[i].double_down()						#process to do for double down 
      Black_jack.display_cards(players)
    elif players[i].check_split() == True:	
     players[i].ask_split()				#ask players who satisfy splitting conditions
     if players[i].status=='SPLIT':
      Black_jack.split_indexes.append(i)			#store index in a list of players who splits
      players[i].split(players)						#process to do for split
#rest of the players(non splitted and non doubled players (satisfy condition but chose not to split or double), and regular players)
    if players[i].status!='END' and players[i].status!='STAY' :
     Black_jack.display_cards(players)
     players[i].hit_till_stay(players)
    else:
     continue
   display.pause()

#all players' turns ends
#now dealer's turn

 Black_jack.dealer_cards[1]=Black_jack.card_2	#unhiding
 print('Dealer Turns up his face-down card')
 display.pause()
 Black_jack.dealer_cards[1]=Black_jack.card_2
 Black_jack.display_cards(players)                      #displays cards 

 Black_jack.dealer_sum()                                #to calc dealer's total
 while Black_jack.add<17:                                       #dealer should hit until his total is atleast 17
  print("Dealer's total is less than 17...,")
  input('So now the dealer is forced to Hit,Press Enter to continue\n')
  Black_jack.dealer_cards.append(Deck.draw_card_random())               #dealer hits
  Black_jack.dealer_sum()
  Black_jack.display_cards(players)

 if Black_jack.add>21:
  print('Dealer is busted')
  for i in range(Black_jack.n):
   if i in Black_jack.double_indexes and players[i].status=='STAY':
    print(players[i].name,'since you doubled your bet,you win twice of your bet!')
    print('Amount you won and your bet amounts will be credited to your wallet')
    Wallet.deposit(players[i],4*players[i].bet)
   elif i in Black_jack.split_indexes:
    flag=0
    if players[i].status=='STAY':
     flag+=1
    if players[i].status_split=='STAY':
     flag+=1
    if flag!=0:
     print(players[i].name,", you won",flag,'hand(s)')
     print('Amount you won will be credited to your wallet')
     Wallet.deposit(players[i],2*flag*players[i].bet)
   elif players[i].status=='STAY':
    print(players[i].name,", you win")
    print('Your bet amounts and the amount you won will be credited to your wallet')
    Wallet.deposit(players[i],players[i].bet*2)
   display.pause()
  return None

#now check with dealer
 Black_jack.dealer_sum()                        #calc total of dealer
 Black_jack.check_with_dealer(players)

main()
