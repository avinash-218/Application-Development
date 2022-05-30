#game.py

#importing modules
import display
import black_jack as bj

def main():
 display.welcome()						#welcome note
 display.intro()
  
 bj.Black_jack.get_bet_amount()					#to get bet amount from the player
 bj.bank.Account.withdraw(bj.Black_jack.bet)			#to withdraw bet amount from bank account to symbolize that the bet is placed
  
 bj.Black_jack.assign_cards()					#to assign cards between the player and the dealer
 bj.Black_jack.display_cards()					#to display cards assigned to the player and the dealer(dealer's hidden card is hidden from the player)
 
 if bj.Black_jack.black_jackpot(bj.Black_jack.player_cards)==True:			#to check for a natural black-jack for the player
  print("You have a natural BLACK JACK!!!\n\n")
  print('Dealer turns up his hidden card')
  input('Press any key to continue')
  bj.Black_jack.dealer_cards.pop()                                        			#removing the hidden element of dealer
  bj.Black_jack.dealer_cards=bj.Black_jack.hit(bj.Black_jack.dealer_cards)      			#adding new element to symbolise as if the hidden card is shown to the user
  bj.Black_jack.display_cards()								#display cards after facing up
  if bj.Black_jack.black_jackpot(bj.Black_jack.dealer_cards)==False:                    #to check for a natural black-jack for the dealer
   print('Dealer does not have natural black jack')
   display.black_jack_win()								#to display result for black-jack-win
   bj.bank.Account.deposit(bj.Black_jack.bet*1.5)					#to deposit amount to player's account	
   return None
  elif bj.Black_jack.black_jackpot(bj.Black_jack.dealer_cards)==True:			#black-jack tie
   display.black_jack_tie()								#to display result for black-jack-tie
   bj.bank.Account.deposit(bj.Black_jack.bet)						#bet amount deposited back	
   return None

 #insurance 
 #control flows here only when player has no black jack
 if bj.Black_jack.check_for_insurance()==True:					#to check if dealer can get a natural black jack(i.e,player can get an insurance)
  bj.Black_jack.dealer_cards.pop()						#to pop hidden element
  bj.Black_jack.hit(bj.Black_jack.dealer_cards)					#hitting to symbolise that the dealer is facing up the hidden card to see if he got a natural black jack
  if bj.Black_jack.ask_for_insurance()=='YES':					#player wishes to insure 
   if bj.Black_jack.black_jackpot(bj.Black_jack.dealer_cards)==True:		#dealer has a natural jack pot
    bj.Black_jack.display_cards()						#dealer's cards are displayed if he has a natural black jack	
    print('Congrajulations!!You Have won your insured bet!')
    print('But You have lost your original bet')
    bj.bank.Account.deposit(1.5*bj.Black_jack.bet)				#player wins 1.5 of the bet amount
    return None
   else:
    bj.Black_jack.dealer_cards[1]='???'						#changing again the second card to a hidden card
    print('Dealer does not have a natural black jack')
    print('You have lost your insured bet.')
  else:										#player wishes not to insure
   if bj.Black_jack.black_jackpot(bj.Black_jack.dealer_cards)==True:            #dealer has a natural jack pot
    bj.Black_jack.display_cards()						#dealer's cards are displayed if he has a natural black jack
    print('The Dealer has a natural Black Jack')
    print('You have lost your original bet')
    return None
   else:
    bj.Black_jack.dealer_cards[1]='???'						#changing again the second card to a hidden card
    print("Dealer doesn't have a natural Black Jack!")
 
 while bj.Black_jack.hit_or_stay()!='STAY':			#to continuously 'Hit' until player choose to stay 
  bj.Black_jack.hit(bj.Black_jack.player_cards)						#calling 'Hit' function
  bj.Black_jack.display_cards()
  if bj.Black_jack.calc_sum(bj.Black_jack.player_cards)==21:	#any player would choose to stay if the total equals 21
   break
  if bj.Black_jack.bust(bj.Black_jack.player_cards)=='BUST':	#to check if player is busted after hitting
   display.bust_player()					#to display result for busted player
   return None

 #when control-flow flows in this statement it means player decided to 'Stay'
 #removing hidden element and adding a new element...to symbolise that dealer now turns the faced down card up
  
 bj.Black_jack.dealer_cards.pop()				#poping the hidden element
 
 #calling hit function to add the second element(symbolises that the second element was the hidden card which is now turned up)
 bj.Black_jack.hit(bj.Black_jack.dealer_cards)			#adding a card in the place of hidden card
 print('Dealer turns up his hidden card')
 bj.Black_jack.display_cards()                                  #display cards
 while bj.Black_jack.calc_sum(bj.Black_jack.dealer_cards)<=16:	#if total of dealer is <=16 he must hit
  display.dealer_force_hit()					#displays that dealer must force hit
  input()							#to pause between two hits
  bj.Black_jack.hit(bj.Black_jack.dealer_cards)			#hit
  bj.Black_jack.display_cards()					#display cards
 
 if bj.Black_jack.calc_sum(bj.Black_jack.dealer_cards)>21:	#to check if dealer will bust
  display.bust_dealer()						#to display that the dealer is busted
  bj.bank.Account.deposit(bj.Black_jack.bet)			#to deposit back the bet amount
  return None

#control flows here only when player is not busted and dealer stops hitting   
 if bj.Black_jack.calc_sum(bj.Black_jack.player_cards)>bj.Black_jack.calc_sum(bj.Black_jack.dealer_cards):	#to check if player's total>dealer's total
  display.player_win()												#display that player has won
  bj.bank.Account.deposit(bj.Black_jack.bet)                    						#to deposit back the bet amount
  return None

 if bj.Black_jack.calc_sum(bj.Black_jack.player_cards)<bj.Black_jack.calc_sum(bj.Black_jack.dealer_cards):	#to check if player's total < dealer's total
  display.player_lose()												#to display that plyer has lose
  return None  
  
 if bj.Black_jack.calc_sum(bj.Black_jack.player_cards)==bj.Black_jack.calc_sum(bj.Black_jack.dealer_cards):	#to check if player's total == dealer's total
  display.match_draw()												#to display that match is draw
  bj.bank.Account.deposit(bj.Black_jack.bet)                    		 				#to deposit back the bet amount








main()
