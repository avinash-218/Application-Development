#game.py

#importing modules and classes
import display
from wallet import Wallet
from black_jack import Black_jack

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
  
 print('\nPlayers should enter your bet amount before playing:\n')
 for i in range(Black_jack.n):
  print('\nPlayer',i+1,':')
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
 Black_jack.display_cards(players)							#display cards for players and dealers

 for i in range(Black_jack.n):
  players[i].black_jackpot()                            #assign natural attribute of players as True or False

#INSURE AND NATURAL
 Black_jack.check_for_insurance()			#checking if insurance is possible for players
 if Black_jack.insure=='CAN':				#if insure is possible
  for i in range(Black_jack.n):
   if players[i].status!='NATURAL':			#and if player doesn't have natural
    players[i].ask_for_insurance()			#ask player for insurance(who doesn't have blackjack)     

 Black_jack.dealer_black_jackpot()			#assign if natural is present for dealer
 
 if Black_jack.natural==True:				#if dealer has natural
  for i in range(Black_jack.n):
   if players[i].status=='NATURAL':			#players having natural
    print('Conrajulations!!! You have a Natural!!!')
    print("Now the dealer will check his card.You will win if he doesn't have a natural.If he has a natural,the match is Draw!")
    display.pause()
    print('Dealer too has Natural!!!')
    print('Match is a natural Tie for you')
    players[i].change_status('END')			#change player status to 'END'
    Wallet.deposit(players[i],players[i].bet)		#refund bet amount
    Wallet.display(players[i])				#print wallet details
   else:						#players who doesn't have natural
    print('Dealer has a natural but you do not have a natural')
    print('You lose your bet naturally')
    for i in range(Black_jack.n):
     players[i].change_status('END')		#change players' status to "END"
     if players[i].status=='INSURE':		#if the players is insured or not
      print('Since you have insured yourself...you have won the insured bet.')
      Wallet.deposit(players[i],players[i].bet)	#depositing insured bet amount
      Wallet.display(players[i])		#print wallet details of the players
 else:							#if dealer has no natural
  for i in range(Black_jack.n):
   if players[i].status=='NATURAL':			#if players have natural
    print('Conrajulations!!! You have a Natural!!!')
    print("Now the dealer will check his card.You will win if he doesn't have a natural.If he has a natural,the match is Draw!")
    display.pause()
    print('Dealer does not have Natural.So you WIN naturally!!!') 
    players[i].change_status('END')				#changing players' status to end
    Wallet.deposit(players[i],1.5*players[i].bet)	#depositing natural bet
   else:						#players don't have natural
    print('Dealer does not have Natural')
    if players[i].status=='INSURE':			#insured players
     print('So,you lost your insured bet.But...')
    print('You can continue your game')

#blackjack and insurance over
#control flows here only 
# 1)when insurance is possible but dealer has no natural and player has no natural(may or maynot insured)
# 2)when insurance is not possible,players has no natural 

#SPLIT AND DOUBLE DOWN AND REGULAR PLAY
#from now on only players whose status is not 'END' will be playing
#split and doube down is similar to playing in regular way except bet amount differs and hiiting frequency alters

 for i in range(Black_jack.n):
  if players[i].status=='PLAY':				#players who did not end their game
   players[i].check_double_down()			#check double down is possible and get player's wish
   players[i].check_split()				#check if split is possible and get players' wish
#condition for split and double down doesn't coincide so calling check_split and check_double_down doesn't cause problem 

#DOUBLE DOWN
   if players[i].status=='DD':							#players who chosen to double down
    print('Since you have choosen to Double Down...you can draw only one card')
    players[i].hit()								#player drawing one card
    Black_jack.display_cards(players)						#to display cards
    players[i].bust()								#to check if player is busted
    if players[i].status=='BUST':				#if player is busted
     display.bust_player()
     players[i].change_status('END')				#change status to "END"
     print('You lose your Doubled Bet')
      
#SPLIT
         
   elif players[i].status=='SPLIT':			#players who chosen to split
    Black_jack.split_indexes.append(i)		#storing players' indexes who wishes to split
    for _ in range(2):					#two loops for two hands
     if 'A' in players[i].cards[0]:				#if the two cards are Aces player gets only one card for each
      players[i].hit()						#one hit
      Black_jack.display_cards(players)				#to display cards
      players[i].black_jackpot()					
      if players[i].status=='NATURAL':				#to check if the player has a natural after splitting
       Wallet.deposit(players[i],players[i].bet*2)		#only bet amount
       players[i].change_status('END')				#change status to "END"
           
#condition for bust and natural doesn't coincide so calling both function next to other doesn't cause problem
         
      players[i].bust()						
      if players[i].status=='BUST':				#to check if th player is busted
       display.bust_player()
       players[i].change_status('END')				#change status to "END"
       print('You lost this hand.')
           
     else:            						#if no Ace,hit until stay
      while players[i].status!='STAY':				#if no natural,no bust,ask until stay
       players[i].hit()
       Black_jack.display_cards(players)			#to display cards
       if players[i].stop_21()==True:				#if tot=21
        break							#no more hits(and player can't be busted since tot is only 21(not exeeds 21))
       players[i].bust()
       if players[i].status=='BUST':				#if player is bust
        display.bust_player()
        print('You Lost this hand.')
        players[i].change_status('END')				#change status to "END"
     self.swap_split()						#swap both hands' details(status,card,add)
          
#REGULAR PLAY
            
   else:   							#NDD NOSPLIT players(means REGULAR PLAY)
    while players[i].status!='STAY':			#hit until stay
     players[i].hit()
     Black_jack.diplay_cards(players)			#to display cards
     if players[i].stop_21()==True:			#if tot=21
      break						#no more hits
     players[i].bust()
     if players[i].status=='BUST':			#if player is bust
      display.bust_player()
      players[i].change_status('END')			#change status to "END"
          

#All players' turns ends
#now it is Dealer's turn
 
 Black_jack.dealer_cards[1]=Black_jack.card_2		#dealer now turns up his hidden card
 print('Dealer Turns up his face-down card')
 Black_jack.display_cards(players)			#displays cards 
 
 if Black_jack.check_status(players)==True:			#if game did not end
  while Black_jack.add<17:					#dealer should hit until his total is atleast 17
   print("Dealer's total is less than 17...So,")
   input('now the dealer is forced to Hit,Press Enter to continue\n')
   Black_jack.dealer_cards.append(Deck.draw_card_random()) 		#dealer hits
   Black_jack.dealer_sum()					#to calc total of dealer
   Black_jack.display_cards(players)					#to display cards
 else:								#game ends
  print('\n     \t\t\t\t\t\t\t\t\t\tGame Over\n')

#control flows here only if game did not end
#to check stayed players and splitted players(other hand also) and double downed players

 Black_jack.dealer_sum()			#calc total of dealer
 for i in range(Black_jack.n):
  if players[i].status in ['DD','STAY']:		#out of DD STAY SPLIT players considering DD and STAY now
   players[i].calc_sum()				#to calc total of player
   players[i].check_with_dealer()			#check player total with dealer
  elif players[i].status=='SPLIT':			#splitted players
   print('Since you have splitted,You first play the hand to your left')
   for i in range(2):			#two loops for two hands
    players[i].calc_sum()
    players[i].check_with_dealer()	#check player's total with dealer's
    players[i].swap_split()		#swap splitted hands














main()
